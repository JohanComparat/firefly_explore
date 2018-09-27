#!/bin/bash 
#SBATCH --partition=he2srvMediumP 
#SBATCH --time=2000:00:00 
#SBATCH --nodes=1 
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=1 
#SBATCH --job-name=p_2277 
#SBATCH --error=/home/comparat/software/linux/firefly_explore/bin/bin_spectra/plot_result_file_run_dir/p_2277.err 
#SBATCH --output=/home/comparat/software/linux/firefly_explore/bin/bin_spectra/plot_result_file_run_dir/p_2277.out 
 
. /home_local/4FSOpsim/py36he2srv/bin/activate 
export LD_LIBRARY_PATH=/home_local/4FSOpsim/py36he2srv/lib$LD_LIBRARY_PATH 
 
cd /home/comparat/software/linux/firefly_explore/bin/bin_spectra 
 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0004.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0005.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0008.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0010.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0012.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0013.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0015.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0018.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0020.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0021.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0022.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0023.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0024.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0025.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0027.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0028.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0029.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0030.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0031.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0032.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0035.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0037.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0038.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0039.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0041.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0042.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0044.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0045.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0049.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0050.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0053.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0054.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0056.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0057.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0059.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0060.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0061.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0062.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0065.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0066.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0067.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0068.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0070.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0071.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0073.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0075.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0076.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0078.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0080.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0081.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0083.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0089.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0091.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0092.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0093.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0094.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0095.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0096.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0097.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0098.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0100.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0102.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0103.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0104.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0105.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0106.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0108.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0110.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0111.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0112.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0113.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0115.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0116.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0117.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0118.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0120.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0122.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0125.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0128.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0129.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0130.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0131.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0132.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0134.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0137.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0140.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0141.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0142.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0144.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0148.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0150.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0152.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0153.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0154.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0156.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0159.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0161.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0162.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0163.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0169.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0170.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0171.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0172.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0173.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0174.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0176.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0177.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0178.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0179.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0181.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0182.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0186.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0187.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0191.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0192.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0193.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0198.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0199.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0200.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0203.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0204.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0206.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0208.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0209.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0211.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0213.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0216.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0217.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0223.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0224.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0227.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0231.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0232.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0233.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0234.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0236.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0237.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0238.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0240.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0241.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0242.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0243.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0244.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0245.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0247.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0248.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0250.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0251.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0252.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0253.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0255.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0257.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0258.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0259.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0261.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0264.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0265.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0266.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0267.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0268.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0269.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0271.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0274.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0276.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0277.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0279.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0281.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0282.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0283.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0284.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0286.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0287.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0293.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0295.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0296.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0299.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0307.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0308.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0309.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0310.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0311.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0314.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0316.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0317.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0318.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0323.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0326.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0327.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0328.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0330.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0332.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0335.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0337.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0339.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0341.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0345.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0348.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0349.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0350.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0351.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0352.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0353.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0354.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0355.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0356.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0359.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0360.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0361.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0365.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0366.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0367.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0370.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0371.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0373.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0375.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0376.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0378.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0386.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0390.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0391.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0392.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0396.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0399.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0401.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0402.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0404.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0405.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0406.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0410.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0411.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0414.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0415.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0417.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0418.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0419.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0420.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0424.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0428.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0430.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0431.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0435.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0436.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0437.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0438.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0439.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0440.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0444.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0445.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0447.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0448.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0449.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0450.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0453.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0457.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0458.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0459.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0462.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0463.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0465.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0466.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0469.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0470.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0472.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0475.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0476.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0477.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0478.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0479.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0481.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0482.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0485.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0489.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0491.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0492.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0494.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0496.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0498.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0499.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0500.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0501.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0502.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0503.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0504.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0506.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0508.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0509.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0512.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0514.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0515.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0516.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0518.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0521.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0523.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0524.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0528.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0530.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0534.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0539.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0541.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0542.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0543.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0546.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0547.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0553.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0554.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0555.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0557.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0561.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0564.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0565.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0566.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0567.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0569.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0571.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0572.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0574.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0575.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0577.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0578.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0580.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0582.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0585.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0586.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0589.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0592.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0593.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0594.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0595.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0596.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0597.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0598.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0602.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0604.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0607.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0608.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0609.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0610.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0611.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0612.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0613.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0614.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0616.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0617.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0619.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0620.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0621.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0622.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0623.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0624.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0627.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0629.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0631.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0632.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0633.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0635.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0639.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/2277/spFly-2277-53705-0640.fits 
 
