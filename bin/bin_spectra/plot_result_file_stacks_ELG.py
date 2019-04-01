import astropy.io.fits as fits
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as p
import numpy as n

from cycler import cycler
# 1. Setting prop cycle on default rc parameter
p.rc('lines', linewidth=1.3)
p.rc('axes', prop_cycle=cycler('color', ["#638bd9", "#e586b6", "#dd7c25"]) )#, "#598664", "#9631a9", "#cff159", "#534f55", "#ab1519", "#89dbde"]) )

import os
import sys

from scipy.stats import norm
from scipy.interpolate import interp1d
m_bins = n.arange(-4,4,0.1)

import glob
path_2_spec_dir = os.path.join(os.environ['HOME'], 'wwwDir/sdss/elg/stacks/v2/')
path_2_fly_dir = os.path.join(os.environ['HOME'], 'wwwDir/sdss/elg/stacks/v2/firefly/')
file_list = n.array(glob.glob(os.path.join(path_2_fly_dir,'spFly*.stack')))
file_list.sort()
baseNames = n.array([ os.path.basename(bn)[6:] for bn in file_list ])
#path_2_spec = os.path.join(os.environ['DATA_DIR'], 'spm', 'v1_1_0', '26', 'stellarpop', '0266', 'spFly-0266-51602-0004.fits')
#path_2_figure = os.path.join(os.environ['DATA_DIR'], 'spm', 'v1_1_0', '26', 'stellarpop', '0266', 'spFly-0266-51602-0004.png')
# /data42s/comparat/firefly/v1_1_0/26/stellarpop/????/
# spFly-0266-51602-0004
# python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0266/spFly-0266-51602-0004.fits 
# python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/v5_10_0/stellarpop/3586/spFly-3586-55181-0003.fits

ii = 0
path_2_spec = os.path.join( path_2_spec_dir, baseNames[ii] )#sys.argv[1]
path_2_spFly = os.path.join( path_2_fly_dir, 'spFly-'+baseNames[ii] )#sys.argv[1]
path_2_figure = os.path.join( path_2_fly_dir, 'spFly-'+baseNames[ii]+'.png')
title = baseNames[ii][10:-6]

def plot_it(path_2_spec, path_2_spFly, path_2_figure, title):
	print(path_2_figure)
	d = fits.open(path_2_spec)
	m = fits.open(path_2_spFly)

	sel = (d[1].data['NspectraPerPixel']>0.5*n.max(d[1].data['NspectraPerPixel']))&(d[1].data['medianStack']>0)
	x_data = d[1].data['wavelength'][sel]
	y_data = d[1].data['medianStack'][sel]
	y_err = d[1].data['jackknifStackErrors'][sel]
	N_spec = d[1].data['NspectraPerPixel'][sel]

	x_model = m[2].data['wavelength']
	y_model = m[2].data['firefly_model']

	# A4 figure
	fig = p.figure(0, (8.2, 11.7), frameon=False )

	# panel top left: spectrum + models
	fig.add_subplot(411, 
					title=title, 
					xlabel='wavelength [Angstrom, rest frame]', 
					ylabel=r'Flux [$f_\lambda 10^{-17}$ erg cm$^{-2}$ s$^{-1}$ A$^{-1}$]',
					ylim=((n.min(y_data)*0.9,1.1* n.max(y_data))),
					xlim=((n.min(x_data)*0.99,1.01* n.max(x_data))) )

	p.plot(x_data, y_data, color='grey', lw=0.4, label='data')
	p.plot(x_model, y_model, label='model')
	p.legend(loc=2, fontsize=12, frameon=False)

	## panel top right: residuals
	fig.add_subplot(412, ylabel='(data-model)/error', xlabel='wavelength [Angstrom, rest frame]')#, xlim=((-2.5,2.5)))

	XMIN = n.max(n.array([n.min(x_model), n.min(x_data)]))
	XMAX = n.min(n.array([n.max(x_model), n.max(x_data)]))

	s_model = (x_model > XMIN) & (x_model < XMAX)
	s_data  = (x_data  > XMIN) & (x_data  < XMAX)

	itp_model = interp1d( x_model[s_model], y_model[s_model] )
	itp_data  = interp1d( x_data[s_data], y_data[s_data] )

	chis = (y_data[s_data]-itp_model(x_data[s_data]))/y_err[s_data]

	p.plot(x_data[s_data], chis)
	#p.legend( frameon=False)#, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	p.grid()

	# age metal
	# log10 light weighted age [Gyr] 
	fig.add_subplot(4,4,9, xlabel='Z [$\log_{10}(Z/Z_\odot)$]', ylabel='age  [$\log_{10}(age/yr)$]')
	for ii in n.arange(1, len(d), 1):
		x  = n.array([ m[2].header['metallicity_massW']    ])
		xe = n.array([ m[2].header['metallicity_massW_up_1sig'], m[2].header['metallicity_massW_low_1sig']       ])
		y  = n.log10(10**9 * 10**n.array([ m[2].header['age_massW']    ])  )
		ye = n.log10(10**9 * 10**n.array([ m[2].header['age_massW_up_1sig'], m[2].header['age_massW_low_1sig']       ]) )
		p.plot(n.array([x, x]), ye, lw=1)

	for ii in n.arange(1, len(d), 1):
		x  = n.array([ m[2].header['metallicity_massW']    ])
		xe = n.array([ m[2].header['metallicity_massW_up_1sig'], m[2].header['metallicity_massW_low_1sig']       ])
		y  = n.log10(10**9 * 10**n.array([ m[2].header['age_massW']    ])  )
		ye = n.log10(10**9 * 10**n.array([ m[2].header['age_massW_up_1sig'], m[2].header['age_massW_low_1sig']       ]) )
		p.plot(xe, n.array([y, y]), lw=1)

	p.grid()

	# mass, age
	fig.add_subplot(4,4,10, xlabel='mass [$\log_{10}(M/M_\odot)$]') # , ylabel='age  [$\log_{10}(age/yr)$]'
	for ii in n.arange(1, len(d), 1):
		y  = n.log10(10**9 * 10**n.array([ m[2].header['age_massW']    ])  )
		ye = n.log10(10**9 * 10**n.array([ m[2].header['age_massW_up_1sig'], m[2].header['age_massW_low_1sig']       ]) )
		x  = n.array([ m[2].header['stellar_mass'] ])
		xe = n.array([ m[2].header['total_mass_up_1sig'], m[2].header['total_mass_low_1sig'] ])
		p.plot(n.array([x, x]), ye, lw=1)

	for ii in n.arange(1, len(d), 1):
		y  = n.log10(10**9 * 10**n.array([ m[2].header['age_massW']    ])  )
		ye = n.log10(10**9 * 10**n.array([ m[2].header['age_massW_up_1sig'], m[2].header['age_massW_low_1sig']       ]) )
		x  = n.array([ m[2].header['stellar_mass'] ])
		xe = n.array([ m[2].header['total_mass_up_1sig'], m[2].header['total_mass_low_1sig'] ])
		p.plot(xe, n.array([y, y]), lw=1)

	p.grid()

	# mass metal
	fig.add_subplot(4,4,13, xlabel='Z [$\log_{10}(Z/Z_\odot)$]', ylabel='mass [$\log_{10}(M/M_\odot)$]')
	for ii in n.arange(1, len(d), 1):
		if m[2].header['IMF']=='Chabrier':
			y  = n.array([ m[2].header['stellar_mass'] ])
			ye = n.array([ m[2].header['total_mass_up_1sig'], m[2].header['total_mass_low_1sig'] ])
			x  = n.array([ m[2].header['metallicity_massW']    ])
			xe = n.array([ m[2].header['metallicity_massW_up_1sig'], m[2].header['metallicity_massW_low_1sig']       ])
			p.plot(n.array([x, x]), ye, lw=1)

	for ii in n.arange(1, len(d), 1):
		if m[2].header['IMF']=='Chabrier':
			y  = n.array([ m[2].header['stellar_mass'] ])
			ye = n.array([ m[2].header['total_mass_up_1sig'], m[2].header['total_mass_low_1sig'] ])
			x  = n.array([ m[2].header['metallicity_massW']    ])
			xe = n.array([ m[2].header['metallicity_massW_up_1sig'], m[2].header['metallicity_massW_low_1sig']       ])
			p.plot(xe, n.array([y, y]), lw=1)

	p.grid()


	# mass EBV
	fig.add_subplot(4,4,14, xlabel='E(B-V)')#, ylabel='mass [$\log_{10}(M/M_\odot)$]')
	for ii in n.arange(1, len(d), 1):
		if m[2].header['IMF']=='Chabrier':
			y  = n.array([ m[2].header['stellar_mass'] ])
			x  = n.array([ m[2].header['EBV']    ])
			ye = n.array([ m[2].header['total_mass_up_1sig'], m[2].header['total_mass_low_1sig'] ])
			p.plot(n.array([x, x]), ye, lw=1)

	p.grid()
	# weigths age
	fig.add_subplot(4,2,6, xlabel='age  [$\log_{10}(age/yr)$]', ylabel='mass weight SSP', ylim=(-0.02,1.02) )
	for ii in n.arange(1, len(d), 1):
		weightM = n.array([ m[2].header['weightMass_ssp_'+str(jj)] for jj in n.arange(m[2].header['ssp_number'])])
		#weightL = n.array([ m[2].header['weightLight_ssp_'+str(jj)] for jj in n.arange(m[2].header['ssp_number'])])
		age = n.array([ n.log10(10**9 * 10**m[2].header['log_age_ssp_'+str(jj)]) for jj in n.arange(m[2].header['ssp_number'])])
		#metal = n.array([ m[2].header['metal_ssp_'+str(jj)] for jj in n.arange(m[2].header['ssp_number'])])
		iiid=n.argsort(age)
		p.plot(age[iiid], weightM[iiid], marker='+', ls='', markersize=12)

	p.grid()

	# weigths metallicity
	fig.add_subplot(4,2,8	, xlabel='Z [$\log_{10}(Z/Z_\odot)$]', ylabel='mass weight SSP', ylim=(-0.02,1.02) )
	for ii in n.arange(1, len(d), 1):
		weightM = n.array([ m[2].header['weightMass_ssp_'+str(jj)] for jj in n.arange(m[2].header['ssp_number'])])
		#weightL = n.array([ m[2].header['weightLight_ssp_'+str(jj)] for jj in n.arange(m[2].header['ssp_number'])])
		#age = n.array([ n.log10(10**9 * 10**m[2].header['log_age_ssp_'+str(jj)]) for jj in n.arange(m[2].header['ssp_number'])])
		metal = n.array([ m[2].header['metal_ssp_'+str(jj)] for jj in n.arange(m[2].header['ssp_number'])])
		iiid=n.argsort(metal)
		p.plot(metal[iiid], weightM[iiid], marker='+', ls='', markersize=12)

	p.grid()
	p.tight_layout()
	p.savefig(path_2_figure)
	p.clf()


for ii in range(len(baseNames)):
	path_2_spec = os.path.join( path_2_spec_dir, baseNames[ii] )#sys.argv[1]
	path_2_spFly = os.path.join( path_2_fly_dir, 'spFly-'+baseNames[ii] )#sys.argv[1]
	path_2_figure = os.path.join( path_2_fly_dir, 'spFly-'+baseNames[ii]+'.png')
	title = baseNames[ii][10:-6]
	plot_it(path_2_spec, path_2_spFly, path_2_figure, title)