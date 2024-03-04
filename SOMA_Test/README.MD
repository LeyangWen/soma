This contains the example c3d inputs used in [solve_labeled_mocap tutorial](https://github.com/nghorbani/soma/blob/main/src/tutorials/solve_labeled_mocap.ipynb)

Some file structures are listed in [run_soma_on_soma_dataset](https://github.com/nghorbani/soma/blob/main/src/tutorials/run_soma_on_soma_dataset.ipynb)
### File structure after extraction 
base folder is `SOMA_Test/support_files`
```tree
├── evaluation_mocaps
│   └── original
│       └── SOMA_manual_labeled
│           ├── soma_subject1
│           │   ├── clap_001.c3d
│           │   ├── clap_002.c3d
│           │   ├── clap_003.c3d
│           │   ├── dance_001.c3d
│           │   ├── dance_002.c3d
│           │   ├── dance_003.c3d
│           │   ├── jump_001.c3d
│           │   ├── jump_002.c3d
│           │   ├── jump_003.c3d
│           │   ├── kick_001.c3d
│           │   ├── kick_002.c3d
│           │   ├── kick_003.c3d
│           │   ├── lift_001.c3d
│           │   ├── lift_002.c3d
│           │   ├── lift_003.c3d
│           │   ├── random_001.c3d
│           │   ├── random_002.c3d
│           │   ├── random_003.c3d
│           │   ├── run_001.c3d
│           │   ├── run_002.c3d
│           │   ├── run_003.c3d
│           │   ├── settings.json
│           │   ├── sit_001.c3d
│           │   ├── sit_002.c3d
│           │   ├── sit_003.c3d
│           │   ├── squat_001.c3d
│           │   ├── squat_002.c3d
│           │   ├── squat_003.c3d
│           │   ├── throw_001.c3d
│           │   ├── throw_002.c3d
│           │   ├── throw_003.c3d
│           │   ├── walk_001.c3d
│           │   ├── walk_002.c3d
│           │   └── walk_003.c3d
│           └── soma_subject2
│               ├── clap_001.c3d
│               ├── clap_002.c3d
│               ├── clap_003.c3d
│               ├── dance_001.c3d
│               ├── dance_002.c3d
│               ├── dance_003.c3d
│               ├── dance_004.c3d
│               ├── dance_005.c3d
│               ├── jump_001.c3d
│               ├── jump_002.c3d
│               ├── jump_003.c3d
│               ├── kick_001.c3d
│               ├── kick_002.c3d
│               ├── kick_003.c3d
│               ├── lift_001.c3d
│               ├── lift_002.c3d
│               ├── lift_003.c3d
│               ├── random_001.c3d
│               ├── random_002.c3d
│               ├── random_003.c3d
│               ├── random_004.c3d
│               ├── run_001.c3d
│               ├── run_002.c3d
│               ├── run_003.c3d
│               ├── settings.json
│               ├── sit_001.c3d
│               ├── sit_002.c3d
│               ├── sit_003.c3d
│               ├── squat_001.c3d
│               ├── squat_002.c3d
│               ├── squat_003.c3d
│               ├── throw_001.c3d
│               ├── throw_002.c3d
│               ├── throw_003.c3d
│               ├── walk_001.c3d
│               ├── walk_002.c3d
│               └── walk_003.c3d
├── marker_layouts
│   └── SOMA
│       └── soma_subject1
│           ├── clap_001.c3d
│           ├── clap_001_smplx_finetuned.json
│           ├── clap_001_smplx_finetuned.ply
│           └── moshpp_smplx
│               ├── clap_001.json
│               └── clap_001.log
├── smplx
│   ├── amass_neutral
│   ├── APose.npz
│   ├── body_dataset
│   ├── body_mean_values.npz
│   ├── extra_smplx_data.tar.bz2
│   ├── female
│   │   ├── model.npz
│   │   └── model.pkl
│   ├── male
│   │   ├── model.npz
│   │   └── model.pkl
│   ├── neutral
│   │   ├── model.npz
│   │   └── model.pkl
│   ├── pose_body_prior.pkl
│   ├── pose_hand_prior.npz
│   └── smplx_locked_head.tar.bz2
└── ssm_head_marker_corr.npz

```