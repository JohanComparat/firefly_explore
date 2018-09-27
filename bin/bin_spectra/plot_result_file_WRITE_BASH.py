import sys
import os
from os.path import join                                                                                                             
import glob                                                                                                                          
import numpy as n

run_dir = '/home/comparat/software/linux/firefly_explore/bin/bin_spectra/run_bash/'

def writeScript(plateN):
  name = "p_"+str(plateN)
  plate_dir = '/data42s/comparat/firefly/v1_1_0/26/stellarpop/'+plateN
  spec_files = n.array(glob.glob(os.path.join( plate_dir, 'spFly-*.fits')))
  spec_files.sort()
  print(spec_files)
  f=open(run_dir + name+".sh",'w')
  f.write("#!/bin/bash \n")
  f.write(" \n")
  f.write("cd /home/comparat/software/linux/firefly_explore/bin/bin_spectra \n")
  f.write(" \n")
  for spec_f in spec_files:
      #if os.path.isfile(spec_f[:-5]+'.png')==False:
      f.write("python3.6 plot_result_file.py "+spec_f+" \n")

  f.write(" \n")
  f.close()

for pl in os.listdir('/data42s/comparat/firefly/v1_1_0/26/stellarpop/'):
	print(pl)
	writeScript(pl)


def writeScript(plateN):
  name = "p_"+str(plateN)
  plate_dir = '/data42s/comparat/firefly/v1_1_0/v5_10_0/stellarpop/'+plateN
  spec_files = n.array(glob.glob(os.path.join( plate_dir, 'spFly-*.fits')))
  spec_files.sort()
  f=open(run_dir + name+".sh",'w')
  f.write("#!/bin/bash \n")
  f.write(" \n")
  f.write("cd /home/comparat/software/linux/firefly_explore/bin/bin_spectra \n")
  f.write(" \n")
  for spec_f in spec_files:
    f.write("python3.6 plot_result_file.py "+spec_f+" \n")
  f.write(" \n")
  f.close()

for pl in os.listdir('/data42s/comparat/firefly/v1_1_0/v5_10_0/stellarpop/'):
	print(pl)
	writeScript(pl)