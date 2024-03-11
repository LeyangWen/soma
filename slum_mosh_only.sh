#!/bin/bash -l
#SBATCH --job-name=Moshpp-debug
#SBATCH --output=output_slurm/log_0.txt
#SBATCH --error=output_slurm/error_0txt
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=8g
#SBATCH --partition=standard
##SBATCH --partition=debug
#SBATCH --time=00:30:00
#SBATCH --account=shdpm0
##### END preamble

my_job_header
module load python3.10-anaconda
module load cuda/11.8.0
module load cudnn/11.8-v8.7.0
module load cupti/11.8.0
module load python/3.10.4
module load pytorch/2.0.1
module load eigen tbb
module list

conda activate soma
mkdir output_slurm

slurm_name=$SLURM_JOB_NAME
#API_KEY="API_KEY"
python -u src/tutorials/solve_labeled_mocap.py \
--wandb_name $slurm_name \
--slurm_id ${SLURM_JOB_ID} > "output_slurm/${SLURM_JOB_ID}_output.out"

#--debug_mode \

module load python3.10-anaconda
module load python/3.10.4
module load cuda/11.6.2
module load pytorch/1.12.1
