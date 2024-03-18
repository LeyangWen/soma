## SOMA: Solving Optical Marker-Based MoCap Automatically, ICCV'21

This repository contains the official PyTorch implementation of:

SOMA: Solving Optical Marker-Based MoCap Automatically\
Nima Ghorbani and Michael J. Black\
[Paper](https://download.is.tue.mpg.de/soma/SOMA_ICCV21.pdf) | [Supp.Mat.](https://download.is.tue.mpg.de/soma/SOMA_Suppmat.pdf) | [Video](https://www.youtube.com/watch?v=BEFCqIefLA8&t=1s&ab_channel=MichaelBlack) | [Project website](https://soma.is.tue.mpg.de/) | [Poster](https://download.is.tue.mpg.de/soma/SOMA_Poster.pdf)

![alt text](https://download.is.tue.mpg.de/soma/tutorials/soma_github_teaser.gif "mocap point clouds (black dots in the back) turned into labeled markers (colored dots)")

SOMA **automatically transforms raw marker-based mocap point clouds** (black dots in the back) into **solved SMPL-X bodies** and **labeled markers** (colored dots).

## Installation

### Wen note
* Make sure it is run on 3.7 since some packages are not compatible
* To use your own moshpp marker vertex id mapping, replace the `marker_vids.py` before make 
* When running in slurm,
  * Add `--user` after `python setup.py xxx` commands if encounter write permission issues
  * `module load eigen tbb`
  * Skip sudo apt install steps
  * For mesh install
    * Boot include dir: `$BOOST_INCLUDE`
    * i.e., `BOOST_INCLUDE_DIRS=$BOOST_INCLUDE make all`
    * or `BOOST_ROOT=$BOOST_ROOT make all `
  * For moshpp install
    * Change `/soma/moshpp/src/moshpp/scan2mesh/mesh_distance/sample2meshdist.h` line 4 to `#include "Eigen/Core"`
    * `cd moshpp/src/moshpp/scan2mesh/mesh_distance` to `make`
    * `cd ../../../..` to `python setup.py install --user`
  * For blender
    * Load from module
    * rename bpy-2.83-20200908 to bpy

### Original

SOMA is originally developed in Python 3.7, PyTorch 1.8.2 LTS, for Ubuntu 20.04.2 LTS. 
Below we prepare the python environment using [Anaconda](https://www.anaconda.com/products/individual), 
however, we opt for a simple pip package manager for installing dependencies.

````
sudo apt install libatlas-base-dev
sudo apt install libpython3.7
sudo apt install libtbb2

conda create -n soma python=3.7 
conda install -c conda-forge ezc3d

pip3 install torch==1.8.2+cu102 torchvision==0.9.2+cu102 torchaudio==0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html

````
ezc3d installation is currently not supported by pip.

Assuming that you have already cloned this repository to your local drive 
go to the root directory of SOMA code and run
````
pip install -r requirements.txt
python setup.py develop
````
If you encounter permission issues in slurm, add --user to the end of the python setup command.

Copy the precompiled 
[smpl-fast-derivatives](https://download.is.tue.mpg.de/download.php?domain=soma&sfile=smpl-fast-derivatives.tar.bz2) 
into your python site-packages folder, i.e. ````anaconda3/envs/soma/lib/python3.7/site-packages````.
The final directory should look like ````anaconda3/envs/soma/lib/python3.7/site-packages/psbody/smpl````.

Install the psbody.mesh library following the instructions in [https://github.com/MPI-IS/mesh](https://github.com/MPI-IS/mesh).
Hint (not a good hint, just follow mesh instructions): clone the mesh repository and run the following from the anaconda environment:  ````python setup.py install ````.

To use the rendering capabilities first install an instance of Blender-2.83 LTS on your machine.
Afterward uncompress contents of the precompiled 
[bpy-2.83](https://download.is.tue.mpg.de/download.php?domain=soma&sfile=blender/bpy-2.83-20200908.tar.bz2) 
keep the outter folder as bpy-2.83xxx and copy 
into your python site-packages folder, i.e. ````anaconda3/envs/soma/lib/python3.7/site-packages````. 

Last but not least, the current SOMA code relies on [MoSh++](https://github.com/nghorbani/moshpp) mocap solver. 
* Before make step, replace the `marker_vids.py` with your own mapping
```bash
  cp support_data/Test-Leyang/marker_vids.py moshpp/src/moshpp/marker_layout/marker_vids.py
  cp support_data/Test-Leyang/create_marker_layout_for_mocaps.py moshpp/src/moshpp/marker_layout/create_marker_layout_for_mocaps.py
```

Please install MoSh++ following the guidelines in its repository.

Leyang: Done

## Using SOMA
There are multiple main parts of the codebase that we try to explain in the [Tutorials](src/tutorials):
- [Run SOMA On MoCap Point Cloud Data](src/tutorials/run_soma_on_soma_dataset.ipynb)
- [Label Priming an Unknown Marker Layout](src/tutorials/label_priming.ipynb)
- [SOMA Ablative Studies](src/tutorials/ablation_study.ipynb)
- [Solve Already Labeled MoCaps With MoSh++](src/tutorials/solve_labeled_mocap.ipynb)

## Citation

Please cite the following paper if you use this code directly or indirectly in your research/projects:

```
@inproceedings{SOMA:ICCV:2021,
  title = {{SOMA}: Solving Optical Marker-Based MoCap Automatically},
  author = {Ghorbani, Nima and Black, Michael J.},
  booktitle = {Proceedings of IEEE/CVF International Conference on Computer Vision (ICCV)},
  month = oct,
  year = {2021},
  doi = {},
  month_numeric = {10}}
```

## License

Software Copyright License for **non-commercial scientific research purposes**. Please read carefully
the [terms and conditions](./LICENSE) and any accompanying documentation before you download and/or
use the SOMA data and software, (the "Data & Software"), software, scripts, and animations. 
By downloading and/or using the Data & Software (including downloading, cloning, installing, and any other use of this repository), 
you acknowledge that you have read these terms
and conditions, understand them, and agree to be bound by them. If you do not agree with these terms and conditions, you
must not download and/or use the Data & Software. 
Any infringement of the terms of this agreement will automatically terminate
your rights under this [License](./LICENSE).

## Contact

The code in this repository is developed by [Nima Ghorbani](https://nghorbani.github.io/) 
while at [Max-Planck Institute for Intelligent Systems, Tübingen, Germany](https://is.mpg.de/person/nghorbani).

If you have any questions you can contact us at [soma@tuebingen.mpg.de](mailto:amass@tuebingen.mpg.de).

For commercial licensing, contact [ps-licensing@tue.mpg.de](mailto:ps-licensing@tue.mpg.de)
