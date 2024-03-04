#!/bin/bash
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
module list

conda activate soma
mkdir output_slurm

slurm_name=$SLURM_JOB_NAME
#API_KEY="API_KEY"
python -u src/tutorials/solve_labeled_mocap.py \
--wandb_name $slurm_name \
--slurm_id ${SLURM_JOB_ID} > "output_slurm/${SLURM_JOB_ID}_output.out"

#--debug_mode \
