#!/bin/bash 
#SBATCH --partition=he2srvMediumP 
#SBATCH --time=2000:00:00 
#SBATCH --nodes=1 
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=1 
#SBATCH --job-name=p_0709 
#SBATCH --error=/home/comparat/software/linux/firefly_explore/bin/bin_spectra/plot_result_file_run_dir/p_0709.err 
#SBATCH --output=/home/comparat/software/linux/firefly_explore/bin/bin_spectra/plot_result_file_run_dir/p_0709.out 
 
. /home_local/4FSOpsim/py36he2srv/bin/activate 
export LD_LIBRARY_PATH=/home_local/4FSOpsim/py36he2srv/lib$LD_LIBRARY_PATH 
 
cd /home/comparat/software/linux/firefly_explore/bin/bin_spectra 
 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0001.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0002.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0006.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0007.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0008.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0009.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0010.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0011.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0012.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0018.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0019.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0021.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0022.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0023.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0024.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0029.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0031.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0032.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0034.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0036.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0037.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0038.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0039.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0041.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0042.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0044.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0045.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0048.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0050.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0051.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0052.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0053.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0054.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0055.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0056.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0057.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0058.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0059.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0061.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0062.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0063.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0065.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0066.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0072.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0079.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0082.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0087.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0089.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0092.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0093.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0095.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0099.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0101.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0103.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0105.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0108.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0109.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0111.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0115.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0116.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0123.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0124.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0126.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0129.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0130.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0132.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0135.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0136.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0139.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0140.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0141.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0143.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0144.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0145.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0146.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0152.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0154.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0155.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0156.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0158.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0160.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0161.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0164.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0165.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0167.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0168.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0169.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0171.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0173.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0175.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0176.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0178.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0182.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0184.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0185.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0187.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0188.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0189.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0191.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0192.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0194.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0195.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0196.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0197.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0199.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0200.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0202.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0204.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0206.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0214.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0215.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0217.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0219.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0222.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0224.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0226.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0229.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0230.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0232.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0233.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0235.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0239.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0240.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0243.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0245.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0246.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0249.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0250.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0252.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0254.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0260.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0263.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0264.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0274.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0281.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0289.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0292.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0293.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0299.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0300.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0303.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0304.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0306.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0307.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0310.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0311.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0312.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0314.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0315.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0317.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0319.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0320.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0324.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0326.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0327.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0329.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0332.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0333.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0335.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0340.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0341.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0343.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0344.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0345.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0350.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0352.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0353.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0354.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0359.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0360.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0361.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0362.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0365.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0369.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0370.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0371.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0375.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0376.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0377.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0378.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0379.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0382.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0387.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0388.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0389.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0391.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0397.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0398.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0399.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0402.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0403.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0404.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0405.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0406.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0409.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0410.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0413.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0415.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0416.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0417.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0419.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0425.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0426.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0427.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0432.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0433.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0434.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0435.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0436.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0439.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0442.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0444.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0446.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0447.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0449.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0450.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0454.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0455.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0456.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0457.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0458.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0459.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0461.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0462.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0463.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0465.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0466.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0468.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0472.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0473.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0479.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0482.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0486.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0490.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0491.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0492.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0493.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0494.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0496.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0497.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0500.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0502.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0503.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0505.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0506.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0508.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0512.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0513.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0518.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0520.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0523.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0525.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0527.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0529.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0531.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0533.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0534.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0536.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0538.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0539.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0542.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0543.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0548.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0549.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0550.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0555.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0556.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0562.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0563.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0565.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0566.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0568.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0569.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0570.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0576.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0580.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0581.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0584.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0586.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0587.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0589.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0590.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0591.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0592.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0593.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0597.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0600.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0601.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0604.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0606.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0608.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0610.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0611.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0613.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0615.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0616.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0618.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0619.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0620.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0621.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0623.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0626.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0627.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0628.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0630.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0632.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0709/spFly-0709-52205-0640.fits 
 