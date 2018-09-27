#!/bin/bash 
#SBATCH --partition=he2srvMediumP 
#SBATCH --time=2000:00:00 
#SBATCH --nodes=1 
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=1 
#SBATCH --job-name=p_2689 
#SBATCH --error=/home/comparat/software/linux/firefly_explore/bin/bin_spectra/plot_result_file_run_dir/p_2689.err 
#SBATCH --output=/home/comparat/software/linux/firefly_explore/bin/bin_spectra/plot_result_file_run_dir/p_2689.out 
 
. /home_local/4FSOpsim/py36he2srv/bin/activate 
export LD_LIBRARY_PATH=/home_local/4FSOpsim/py36he2srv/lib$LD_LIBRARY_PATH 
 
cd /home/comparat/software/linux/firefly_explore/bin/bin_spectra 
 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2689/spFly-2689-54149-0190.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2689/spFly-2689-54149-0226.fits 
 
