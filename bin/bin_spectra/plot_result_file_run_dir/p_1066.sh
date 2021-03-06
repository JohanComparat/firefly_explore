#!/bin/bash 
#SBATCH --partition=he2srvMediumP 
#SBATCH --time=2000:00:00 
#SBATCH --nodes=1 
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=1 
#SBATCH --job-name=p_1066 
#SBATCH --error=/home/comparat/software/linux/firefly_explore/bin/bin_spectra/plot_result_file_run_dir/p_1066.err 
#SBATCH --output=/home/comparat/software/linux/firefly_explore/bin/bin_spectra/plot_result_file_run_dir/p_1066.out 
 
. /home_local/4FSOpsim/py36he2srv/bin/activate 
export LD_LIBRARY_PATH=/home_local/4FSOpsim/py36he2srv/lib$LD_LIBRARY_PATH 
 
cd /home/comparat/software/linux/firefly_explore/bin/bin_spectra 
 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0009.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0012.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0022.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0025.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0033.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0041.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0042.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0046.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0047.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0048.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0049.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0053.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0054.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0060.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0066.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0068.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0081.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0083.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0086.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0089.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0093.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0095.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0107.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0112.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0122.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0125.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0127.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0128.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0130.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0134.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0135.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0137.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0144.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0147.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0148.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0150.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0151.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0154.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0157.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0158.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0159.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0160.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0168.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0174.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0176.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0179.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0181.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0184.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0185.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0196.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0206.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0207.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0221.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0222.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0228.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0234.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0239.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0245.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0247.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0249.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0256.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0261.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0272.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0274.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0278.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0279.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0280.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0281.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0284.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0291.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0298.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0307.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0308.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0314.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0320.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0328.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0331.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0333.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0336.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0338.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0347.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0348.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0350.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0351.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0352.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0355.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0357.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0358.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0360.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0362.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0365.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0367.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0368.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0369.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0370.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0375.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0380.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0382.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0384.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0396.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0399.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0400.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0403.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0405.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0412.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0421.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0422.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0425.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0426.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0434.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0435.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0441.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0450.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0453.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0454.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0458.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0459.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0468.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0482.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0483.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0485.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0492.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0493.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0494.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0500.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0502.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0505.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0509.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0516.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0518.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0521.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0528.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0529.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0533.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0535.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0542.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0549.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0555.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0559.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0562.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0564.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0567.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0568.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0572.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0577.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0598.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0609.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0611.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1066/spFly-1066-52589-0613.fits 
 
