import astropy.io.fits as fits
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as p
import numpy as n

from cycler import cycler
# 1. Setting prop cycle on default rc parameter
p.rc('lines', linewidth=0.7)
p.rc('axes', prop_cycle=cycler('color', ["#638bd9", "#e586b6", "#dd7c25", "#598664", "#9631a9", "#cff159", "#534f55", "#ab1519", "#89dbde"]) )

import os
import sys

from scipy.stats import norm

m_bins = n.arange(-4,4,0.1)

#path_2_spec = os.path.join(os.environ['DATA_DIR'], 'spm', 'v1_1_0', '26', 'stellarpop', '0266', 'spFly-0266-51602-0004.fits')
#path_2_figure = os.path.join(os.environ['DATA_DIR'], 'spm', 'v1_1_0', '26', 'stellarpop', '0266', 'spFly-0266-51602-0004.png')
# /data42s/comparat/firefly/v1_1_0/26/stellarpop/????/
path_2_spec = sys.argv[1]
path_2_figure = path_2_spec[:-5]+'.png'

d = fits.open(path_2_spec)

title = "PLATE="+d[0].header['PLATE']+", MJD="+d[0].header['MJD']+", FIBERID="+d[0].header['FIBERID'][:-5]+", z="+str(n.round(d[0].header['REDSHIFT'],3))

y_data = d[1].data['original_data']
y_err = d[1].data['flux_error']

# A4 figure
fig = p.figure(0, (8.2, 11.7), frameon=False )

#fig.add_subplot(111, title=title, frameon=False)


# panel top left: spectrum + models
fig.add_subplot(411, title=title, xlabel='wavelength [Angstrom, rest frame]', ylabel=r'Flux [$f_\lambda 10^{-17}$ erg cm$^{-2}$ s$^{-1}$ A$^{-1}$]')
p.plot(d[1].data['wavelength'], y_data, color='grey', lw=0.4)
for ii in n.arange(1, len(d), 1):
	p.plot(d[ii].data['wavelength'], d[ii].data['firefly_model'], label=d[ii].header['IMF']+" "+d[ii].header['MODEL']+r", N$_{SSP}$="+str(d[ii].header['ssp_number']))

p.legend(loc=1, fontsize=9)

## panel top right: residuals
fig.add_subplot(412, xlabel='(data-model)/error', ylabel='Normed distribution', xlim=((-2.5,2.5)))
for ii in n.arange(1, len(d), 1):
	chis = (d[ii].data['original_data']-d[ii].data['firefly_model'])/d[ii].data['flux_error']
	ok = (d[ii].data['original_data']>0)
	p.hist(chis[ok], bins=m_bins, normed=True, histtype='step')

p.plot(m_bins, norm.pdf(m_bins, loc=0, scale=1), label=r'$\mathcal{N}(0,1)$', ls='dashed', lw=2)
p.legend( frameon=False)#, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
p.grid()

# panel top right: residuals
#fig.add_subplot(412, xlabel='wavelength [Angstrom, rest frame]', ylabel='data/model', ylim=((0.5,1.5)))
#for ii in n.arange(1, len(d), 1):
	#YY = (d[ii].data['original_data']/d[ii].data['firefly_model'])
	#ok = (d[ii].data['original_data']>0)
	#p.plot(d[ii].data['wavelength'][ok], YY[ok], lw=0.4)


#p.plot(d[ii].data['wavelength'][ok], 1+abs(d[ii].data['flux_error'][ok]/d[ii].data['original_data'][ok]), lw=0.4, ls='dashed', color='k')

#p.plot(d[ii].data['wavelength'][ok], 1-abs(d[ii].data['flux_error'][ok]/d[ii].data['original_data'][ok]), lw=0.4, ls='dashed', color='k', label='uncertainty')

#p.legend(loc=1, frameon=False)
#p.grid()


# age metal
# log10 light weighted age [Gyr] 
fig.add_subplot(4,4,9, xlabel='Z [$\log_{10}(Z/Z_\odot)$]', ylabel='age  [$\log_{10}(age/yr)$]')
for ii in n.arange(1, len(d), 1):
	x  = n.array([ d[ii].header['metallicity_massW']    ])
	xe = n.array([ d[ii].header['metallicity_massW_up_1sig'], d[ii].header['metallicity_massW_low_1sig']       ])
	y  = n.log10(10**9 * 10**n.array([ d[ii].header['age_massW']    ])  )
	ye = n.log10(10**9 * 10**n.array([ d[ii].header['age_massW_up_1sig'], d[ii].header['age_massW_low_1sig']       ]) )
	p.plot(n.array([x, x]), ye, lw=1)

for ii in n.arange(1, len(d), 1):
	x  = n.array([ d[ii].header['metallicity_massW']    ])
	xe = n.array([ d[ii].header['metallicity_massW_up_1sig'], d[ii].header['metallicity_massW_low_1sig']       ])
	y  = n.log10(10**9 * 10**n.array([ d[ii].header['age_massW']    ])  )
	ye = n.log10(10**9 * 10**n.array([ d[ii].header['age_massW_up_1sig'], d[ii].header['age_massW_low_1sig']       ]) )
	p.plot(xe, n.array([y, y]), lw=1)

p.grid()

# mass, age
fig.add_subplot(4,4,10, xlabel='mass [$\log_{10}(M/M_\odot)$]') # , ylabel='age  [$\log_{10}(age/yr)$]'
for ii in n.arange(1, len(d), 1):
	y  = n.log10(10**9 * 10**n.array([ d[ii].header['age_massW']    ])  )
	ye = n.log10(10**9 * 10**n.array([ d[ii].header['age_massW_up_1sig'], d[ii].header['age_massW_low_1sig']       ]) )
	x  = n.array([ d[ii].header['stellar_mass'] ])
	xe = n.array([ d[ii].header['stellar_mass_up_1sig'], d[ii].header['stellar_mass_low_1sig'] ])
	p.plot(n.array([x, x]), ye, lw=1)

for ii in n.arange(1, len(d), 1):
	y  = n.log10(10**9 * 10**n.array([ d[ii].header['age_massW']    ])  )
	ye = n.log10(10**9 * 10**n.array([ d[ii].header['age_massW_up_1sig'], d[ii].header['age_massW_low_1sig']       ]) )
	x  = n.array([ d[ii].header['stellar_mass'] ])
	xe = n.array([ d[ii].header['stellar_mass_up_1sig'], d[ii].header['stellar_mass_low_1sig'] ])
	p.plot(xe, n.array([y, y]), lw=1)

p.grid()

# mass metal
fig.add_subplot(4,4,13, xlabel='Z [$\log_{10}(Z/Z_\odot)$]', ylabel='mass [$\log_{10}(M/M_\odot)$]')
for ii in n.arange(1, len(d), 1):
	y  = n.array([ d[ii].header['stellar_mass'] ])
	ye = n.array([ d[ii].header['stellar_mass_up_1sig'], d[ii].header['stellar_mass_low_1sig'] ])
	x  = n.array([ d[ii].header['metallicity_massW']    ])
	xe = n.array([ d[ii].header['metallicity_massW_up_1sig'], d[ii].header['metallicity_massW_low_1sig']       ])
	
	p.plot(n.array([x, x]), ye, lw=1)

for ii in n.arange(1, len(d), 1):
	y  = n.array([ d[ii].header['stellar_mass'] ])
	ye = n.array([ d[ii].header['stellar_mass_up_1sig'], d[ii].header['stellar_mass_low_1sig'] ])
	x  = n.array([ d[ii].header['metallicity_massW']    ])
	xe = n.array([ d[ii].header['metallicity_massW_up_1sig'], d[ii].header['metallicity_massW_low_1sig']       ])
	p.plot(xe, n.array([y, y]), lw=1)

p.grid()


# mass EBV
fig.add_subplot(4,4,14, xlabel='E(B-V)')#, ylabel='mass [$\log_{10}(M/M_\odot)$]')
for ii in n.arange(1, len(d), 1):
	y  = n.array([ d[ii].header['stellar_mass'] ])
	x  = n.array([ d[ii].header['EBV']    ])
	ye = n.array([ d[ii].header['stellar_mass_up_1sig'], d[ii].header['stellar_mass_low_1sig'] ])
	p.plot(n.array([x, x]), ye, lw=1)

p.grid()
# weigths age
fig.add_subplot(4,2,6, xlabel='age  [$\log_{10}(age/yr)$]', ylabel='mass weight', ylim=((0.,1.)))
for ii in n.arange(1, len(d), 1):
	
	weightM = n.array([ d[ii].header['weightMass_ssp_'+str(jj)] for jj in n.arange(d[ii].header['ssp_number'])])
	#weightL = n.array([ d[ii].header['weightLight_ssp_'+str(jj)] for jj in n.arange(d[ii].header['ssp_number'])])
	age = n.array([ n.log10(10**9 * 10**d[ii].header['log_age_ssp_'+str(jj)]) for jj in n.arange(d[ii].header['ssp_number'])])
	#metal = n.array([ d[ii].header['metal_ssp_'+str(jj)] for jj in n.arange(d[ii].header['ssp_number'])])
	iiid=n.argsort(age)
	p.plot(age[iiid], weightM[iiid], marker='+', lw=1.5)#, ls='none')

p.grid()

# weigths age
fig.add_subplot(4,2,8	, xlabel='Z [$\log_{10}(Z/Z_\odot)$]', ylabel='mass weight', ylim=((0.,1.)))
for ii in n.arange(1, len(d), 1):
	
	weightM = n.array([ d[ii].header['weightMass_ssp_'+str(jj)] for jj in n.arange(d[ii].header['ssp_number'])])
	#weightL = n.array([ d[ii].header['weightLight_ssp_'+str(jj)] for jj in n.arange(d[ii].header['ssp_number'])])
	#age = n.array([ n.log10(10**9 * 10**d[ii].header['log_age_ssp_'+str(jj)]) for jj in n.arange(d[ii].header['ssp_number'])])
	metal = n.array([ d[ii].header['metal_ssp_'+str(jj)] for jj in n.arange(d[ii].header['ssp_number'])])
	iiid=n.argsort(metal)
	p.plot(metal[iiid], weightM[iiid], marker='+', lw=1.5)#, ls='none')


p.grid()


p.tight_layout()
p.savefig(path_2_figure)
p.clf()

