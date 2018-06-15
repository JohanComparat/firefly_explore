
import os, sys
import glob
import numpy as n

run_dir = '/home/comparat/software/linux/firefly_explore/bin/bin_spectra/plot_result_file_run_dir/'

scripts = n.array(glob.glob( os.path.join(run_dir, 'p_*.sh' )))
scripts.sort()

for script in scripts:
  print(script)
  os.system('sbatch '+script)

