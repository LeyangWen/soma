from typing import List

import numpy as np
from loguru import logger

from moshpp.marker_layout.edit_tools import marker_layout_write
from moshpp.marker_layout.labels_map import general_labels_map
from moshpp.marker_layout.marker_vids import all_marker_vids, marker_type_labels
# copy and replace moshpp/src/moshpp/marker_layout/create_marker_layout_for_mocaps.py
# changing distance from skin surface

def marker_labels_to_marker_layout(chosen_markers: List[str],
                                   marker_layout_fname: str,
                                   surface_model_type: str,
                                   labels_map: dict = general_labels_map,
                                   wrist_markers_on_stick: bool = False,
                                   separate_types=None) -> bool:
    """
    Given labels mocap sequences will produce a marker layout file for the set of unique labels

    :param marker_layout_fname: output marker layout file name
    :param surface_model_type: smplx/smpl/smplh/mano/etc
    :param labels_map: mapping between jungle of used labels for actually the same marker
    :param wrist_markers_on_stick: whether wrist markers are placed on stick; e.g. CMU dataset
    :param separate_types:
    :return:

    """

    if separate_types is None:
        separate_types = ['body', 'face', 'finger']

    assert surface_model_type in all_marker_vids.keys(), \
        ValueError(f'No suitable database of labels found for surface_model_type: {surface_model_type}')

    logger.debug(f'Preparing marker layout for surface_model_type: {surface_model_type}')

    # mean_dist_from_skin = {'wrist': 0.039,
    #                        'body': 0.0095,
    #                        'face': 0.0002,
    #                        'finger_right': 0.0002,
    #                        'finger_left': 0.0002,
    #                        }
    marker_distance_VEHS = 0.009  # for 14mm vicon markers
    mean_dist_from_skin = {'wrist': marker_distance_VEHS,
                           'body': marker_distance_VEHS,
                           'face': marker_distance_VEHS,
                           'finger_right': marker_distance_VEHS,
                           'finger_left': marker_distance_VEHS,
                           }

    has_face = surface_model_type in ['smplx', 'flame'] and 'face' in separate_types
    has_finger = surface_model_type in ['smplh', 'smplx', 'mano'] and 'finger' in separate_types
    has_body = surface_model_type not in ['mano', 'flame']

    unique_labels = list(set([labels_map.get(l, l) for l in chosen_markers]))

    # logger.debug('Unique labels: {}'.format(unique_labels))

    marker_vids = {}
    unknown_labels = []
    for l in sorted(unique_labels):
        if l not in all_marker_vids[surface_model_type]:
            unknown_labels.append(l)
            continue

        marker_vids[l] = all_marker_vids[surface_model_type][l]
    if unknown_labels:
        logger.error(f'Unknown marker label(s) for surface_model_type {surface_model_type} skipped: {unknown_labels}.')

    marker_type_mask = {}
    if has_face:
        marker_type_mask['face'] = np.zeros(len(marker_vids), dtype=np.bool)
    if has_finger:
        marker_type_mask['finger_left'] = np.zeros(len(marker_vids), dtype=np.bool)
        marker_type_mask['finger_right'] = np.zeros(len(marker_vids), dtype=np.bool)
    if has_body: marker_type_mask['body'] = np.zeros(len(marker_vids), dtype=np.bool)
    if wrist_markers_on_stick: marker_type_mask['wrist'] = np.zeros(len(marker_vids), dtype=np.bool)

    logger.debug(
        f'has_face: {has_face}, has_finger: {has_finger}, has_body: {has_body}, wrist_markers_on_stick: {wrist_markers_on_stick}')

    for lId, l in enumerate(marker_vids):
        if has_face and l in marker_type_labels['face']:
            marker_type_mask['face'][lId] = True
        elif has_finger and l in marker_type_labels['finger_left']:
            marker_type_mask['finger_left'][lId] = True
        elif has_finger and l in marker_type_labels['finger_right']:
            marker_type_mask['finger_right'][lId] = True
        elif wrist_markers_on_stick and l in marker_type_labels['wrist']:
            marker_type_mask['wrist'][lId] = True
        elif has_body:
            marker_type_mask['body'][lId] = True
        else:
            raise ValueError(f'Marker {l} could not be assigned to any marker type.')

    marker_layout_write({'marker_vids': marker_vids,
                         'marker_type_mask': {k: v for k, v in marker_type_mask.items() if v.sum() != 0},
                         'm2b_distance': {k: mean_dist_from_skin[k] for k, v in marker_type_mask.items() if
                                          v.sum() != 0},
                         'surface_model_type': surface_model_type
                         },
                        marker_layout_fname)

    logger.info(f'Created marker layout: {marker_layout_fname}')

    return True
