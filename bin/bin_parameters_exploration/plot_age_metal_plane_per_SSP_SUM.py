import astropy.io.fits as fits
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams.update({'font.size': 14})
import matplotlib.pyplot as p

from cycler import cycler
# 1. Setting prop cycle on default rc parameter
p.rc('lines', linewidth=0.9)
p.rcParams.update({'font.size': 14})
p.rc('axes', prop_cycle=cycler('color', ["#638bd9", "#e586b6", "#dd7c25", "#598664", "#9631a9", "#cff159", "#534f55", "#ab1519", "#89dbde"]) )


import numpy as n
import os
import sys
import glob
imfs = ["Chabrier_ELODIE_", "Chabrier_MILES_", "Chabrier_STELIB_", "Kroupa_ELODIE_", "Kroupa_MILES_", "Kroupa_STELIB_",  "Salpeter_ELODIE_", "Salpeter_MILES_", "Salpeter_STELIB_" ]

a_bins = n.arange(6.5, 10.5, 0.1)
z_bins = n.arange(-3,3,0.1)
XX, YY = n.meshgrid((z_bins[1:]+z_bins[:-1])/2., 0.5*(a_bins[1:]+a_bins[:-1]))

in_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images', 'az')

out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images', 'az_ssp')

for imf in imfs:

	h_list = n.array(glob.glob(os.path.join(in_dir, "age_metallicity_"+imf+"*_eboss_04.data" )))
	h_list.sort()

	HH_i=[]
	for h_i in h_list:
		HH_i.append(n.loadtxt(h_i))

	HH = n.sum(HH_i, axis=0)

	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	p.scatter(XX[HH>1], YY[HH>1], c=n.log10(HH[HH>1]), s=40, edgecolors='none', marker='s', vmin=1, vmax=4 )
	p.xlim((-2.2,0.5))
	p.ylim((7.3,10.5))
	p.ylabel(r'$\log_{10}(Age/yr)$')
	p.xlabel(r'$\log_{10}(Z/Z_\odot)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N \times w_M)$')
	p.legend(loc=0, frameon = False)
	p.grid()
	p.text(-2.1, 7.5,'eBOSS '+imf.split('_')[0] )
	p.tight_layout()
	p.savefig(os.path.join(out_dir, "age_metallicity_"+imf+"eboss_04.png" ))
	p.clf()


	h_list = n.array(glob.glob(os.path.join(in_dir, "age_metallicity_"+imf+"*_sdss_04.data" )))
	h_list.sort()

	HH_i=[]
	for h_i in h_list:
		HH_i.append(n.loadtxt(h_i))

	HH = n.sum(HH_i, axis=0)

	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	p.scatter(XX[HH>1], YY[HH>1], c=n.log10(HH[HH>1]), s=40, edgecolors='none', marker='s', vmin=1, vmax=4 )
	p.xlim((-2.2,0.5))
	p.ylim((7.3,10.5))
	p.ylabel(r'$\log_{10}(Age/yr)$')
	p.xlabel(r'$\log_{10}(Z/Z_\odot)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N \times w_M)$')
	p.legend(loc=0, frameon = False)
	p.grid()
	p.text(-2.1, 7.5,'SDSS '+imf.split('_')[0]  )
	p.tight_layout()
	p.savefig(os.path.join(out_dir, "age_metallicity_"+imf+"sdss_04.png" ))
	p.clf()
	#


	h_list = n.array(glob.glob(os.path.join(in_dir, "age_metallicity_"+imf+"*_deep2_04.data" )))
	h_list.sort()

	HH_i=[]
	for h_i in h_list:
		HH_i.append(n.loadtxt(h_i))

	HH = n.sum(HH_i, axis=0)


	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	p.scatter(XX[HH>1], YY[HH>1], c=n.log10(HH[HH>1]), s=40, edgecolors='none', marker='s' , vmin=1, vmax=2.5)
	p.xlim((-2.2,0.5))
	p.ylim((7.3,10.5))
	p.ylabel(r'$\log_{10}(Age/yr)$')
	p.xlabel(r'$\log_{10}(Z/Z_\odot)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	p.legend(loc=0, frameon = False)
	p.text(-2.1, 7.5,'DEEP2 '+imf.split('_')[0]   )
	p.grid()
	p.tight_layout()
	p.savefig(os.path.join(out_dir, "age_metallicity_"+imf+"deep2_04.png" ))
	p.clf()
