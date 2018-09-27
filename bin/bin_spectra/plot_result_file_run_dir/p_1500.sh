#!/bin/bash 
#SBATCH --partition=he2srvMediumP 
#SBATCH --time=2000:00:00 
#SBATCH --nodes=1 
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=1 
#SBATCH --job-name=p_1500 
#SBATCH --error=/home/comparat/software/linux/firefly_explore/bin/bin_spectra/plot_result_file_run_dir/p_1500.err 
#SBATCH --output=/home/comparat/software/linux/firefly_explore/bin/bin_spectra/plot_result_file_run_dir/p_1500.out 
 
. /home_local/4FSOpsim/py36he2srv/bin/activate 
export LD_LIBRARY_PATH=/home_local/4FSOpsim/py36he2srv/lib$LD_LIBRARY_PATH 
 
cd /home/comparat/software/linux/firefly_explore/bin/bin_spectra 
 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0004.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0007.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0008.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0010.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0021.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0023.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0027.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0032.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0033.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0038.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0039.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0041.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0043.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0046.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0048.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0049.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0050.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0054.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0055.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0058.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0062.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0063.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0067.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0071.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0072.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0073.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0078.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0080.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0081.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0083.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0085.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0087.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0089.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0100.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0101.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0103.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0104.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0105.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0106.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0107.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0110.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0112.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0114.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0116.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0117.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0119.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0120.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0121.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0122.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0123.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0124.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0127.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0129.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0132.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0133.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0134.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0135.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0136.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0138.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0139.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0140.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0141.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0147.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0148.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0155.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0156.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0157.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0158.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0159.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0161.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0164.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0170.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0176.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0178.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0180.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0182.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0184.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0188.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0189.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0191.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0194.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0195.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0196.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0197.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0200.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0204.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0207.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0210.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0211.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0215.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0217.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0221.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0222.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0223.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0226.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0232.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0233.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0236.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0238.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0239.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0244.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0245.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0246.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0249.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0251.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0252.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0255.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0257.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0261.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0265.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0268.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0269.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0271.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0274.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0276.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0279.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0282.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0285.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0287.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0292.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0293.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0294.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0295.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0297.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0298.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0302.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0305.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0310.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0311.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0316.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0317.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0318.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0321.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0324.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0327.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0328.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0329.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0331.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0347.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0348.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0351.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0352.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0354.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0356.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0362.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0365.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0367.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0369.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0373.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0375.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0379.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0382.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0388.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0389.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0390.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0396.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0398.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0399.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0402.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0403.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0409.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0413.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0414.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0418.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0421.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0422.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0426.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0428.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0429.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0430.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0433.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0435.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0437.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0445.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0451.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0454.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0461.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0465.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0467.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0470.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0472.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0474.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0478.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0479.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0481.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0488.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0490.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0492.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0497.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0498.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0501.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0503.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0504.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0511.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0513.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0517.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0533.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0534.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0536.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0540.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0542.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0551.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0556.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0558.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0564.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0565.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0567.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0569.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0574.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0578.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0582.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0584.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0585.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0594.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0595.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0596.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0598.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0602.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0604.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0607.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0609.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0610.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0615.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0620.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0622.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0624.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0628.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0631.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0634.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0636.fits 
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/1500/spFly-1500-53730-0638.fits 
 