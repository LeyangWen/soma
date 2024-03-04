import os.path as osp
from glob import glob
import wandb
import numpy as np
from loguru import logger
import argparse
from soma.amass.mosh_manual import mosh_manual

# todo: change file path again
# todo: modify settings.json to include gender info
# todo: set marker layout template?


def parse_args():
    # Create the parser
    parser = argparse.ArgumentParser(description='Moshpp-VEHS-7M')
    # Add the arguments
    parser.add_argument('--soma_work_base_dir', type=str, default='/home/leyang/Documents/soma/SOMA_Test', help='The base directory for SOMA work')
    # parser.add_argument('--support_base_dir', type=str, default=None, help='The base directory for support files')
    # parser.add_argument('--mocap_base_dir', type=str, default=None, help='The base directory for mocap files')
    # parser.add_argument('--work_base_dir', type=str, default=None, help='The base directory for work files')
    parser.add_argument('--target_ds_names', nargs='+', default=['SOMA_manual_labeled',], help='Target dataset names')

    parser.add_argument('--wandb_project', default='Moshpp-VEHS-7M', help='wandb project name')
    parser.add_argument('--wandb_name', default='Debug', help='wandb run name')
    parser.add_argument('--slurm_id', default=0, type=int, help='The slurm id of this run')
    parser.add_argument('--debug_mode', action='store_false')  # default: False if store_true
    parser.add_argument('--arg_notes', default="Empty", type=str, help='notes for this run, will be stored in wandb')

    # Parse the arguments
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    soma_work_base_dir = args.soma_work_base_dir
    support_base_dir = osp.join(soma_work_base_dir, 'support_files')
    mocap_base_dir = osp.join(support_base_dir, 'evaluation_mocaps/original')
    work_base_dir = osp.join(soma_work_base_dir, 'running_just_mosh')
    target_ds_names = args.target_ds_names

    wandb_run = wandb.init(project=args.wandb_project, name=args.wandb_name, notes=args.arg_notes)

    for ds_name in target_ds_names:
        mocap_fnames = glob(osp.join(mocap_base_dir, ds_name,  '*/*.c3d'))

        logger.info(f'#mocaps found for {ds_name}: {len(mocap_fnames)}')

        mosh_manual(
            mocap_fnames,
            mosh_cfg={
                'moshpp.verbosity': 1, # set to 2 to visulaize the process in meshviewer
                'dirs.work_base_dir': osp.join(work_base_dir, 'mosh_results'),
                'dirs.support_base_dir': support_base_dir,
            },
            render_cfg={
                'dirs.work_base_dir': osp.join(work_base_dir, 'mp4_renders'),
                'render.render_engine': 'eevee',  # eevee / cycles,
                # 'render.render_engine': 'cycles',  # eevee / cycles,
                'render.show_markers': True,
                # 'render.save_final_blend_file': True
                'dirs.support_base_dir': support_base_dir,

            },
            parallel_cfg={
                'pool_size': 1,
                'max_num_jobs': 1,
                'randomly_run_jobs': True,
            },
            run_tasks=[
                'mosh',
                'render',
            ],
            fast_dev_run=args.debug_mode,
        )
    wandb_run.finish()