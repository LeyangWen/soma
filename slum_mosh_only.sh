#!/bin/bash -l
#SBATCH --job-name=Moshpp-S03-00
#SBATCH --output=output_slurm/log_0.txt
#SBATCH --error=output_slurm/error_0txt
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --mem=128g
#SBATCH --partition=standard
##SBATCH --partition=debug
#SBATCH --time=24:00:00
#SBATCH --account=shdpm0
##### END preamble

my_job_header

conda activate soma3.7

module load clang/2022.1.2
module load gcc/10.3.0
module load gcc/13.2.0
module load intel/2022.1.2
module load boost/1.78.0
module load eigen tbb
module load blender
module list


mkdir output_slurm

subject_name="S03"
slurm_name=$SLURM_JOB_NAME
#API_KEY="API_KEY"

python -u src/tutorials/solve_labeled_mocap.py \
--soma_work_base_dir /nfs/turbo/coe-shdpm/leyang/SOMA/VEHS-7M/ \
--mocap_base_dir /nfs/turbo/coe-shdpm/leyang/VEHS-7M/ \
--target_ds_names c3d \
--target_subject_names $subject_name \
--wandb_project Moshpp-VEHS-7M-slurm \
--wandb_name $slurm_name \
--slurm_id ${SLURM_JOB_ID}

#> "output_slurm/${SLURM_JOB_ID}_output.out"

#--debug_mode \

