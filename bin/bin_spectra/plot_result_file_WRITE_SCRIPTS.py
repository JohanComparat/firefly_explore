import sys
import os
nside = sys.argv[1]

from os.path import join                                                                                                             
import glob                                                                                                                          
import numpy as n

run_dir = '/home/comparat/software/linux/firefly_explore/bin/bin_spectra/plot_result_file_run_dir/'

def writeScript(plateN):
  name = "p_"+str(plateN)
  
  plate_dir = '/data42s/comparat/firefly/v1_1_0/26/stellarpop/'+plateN
  spec_files = n.array(glob.glob(os.path.join( plate_dir, 'spFly*.fits')))
  spec_files.sort()
  
  f=open(run_dir + name+".sh",'w')
  f.write("#!/bin/bash \n")
  f.write("#SBATCH --partition=he2srvLowP \n")
  f.write("#SBATCH --time=2000:00:00 \n")
  f.write("#SBATCH --nodes=1 \n")
  f.write("#SBATCH --ntasks=1 \n")
  f.write("#SBATCH --cpus-per-task=1 \n")
  f.write("#SBATCH --job-name="+name+" \n")
  f.write("#SBATCH --error="+run_dir+name+".err \n")
  f.write("#SBATCH --output="+run_dir+name+".out \n")
  f.write(" \n")
  f.write(". /home_local/4FSOpsim/py36he2srv/bin/activate \n")
  f.write("export LD_LIBRARY_PATH=/home_local/4FSOpsim/py36he2srv/lib$LD_LIBRARY_PATH \n")
  f.write(" \n")
  f.write("cd /home/comparat/software/linux/firefly_explore/bin/bin_spectra \n")
  f.write(" \n")
  for spec_f in spec_files:
    f.write("python3.6 plot_result_file.py "+spec_f+" \n")
  f.write(" \n")
  f.close()


]
