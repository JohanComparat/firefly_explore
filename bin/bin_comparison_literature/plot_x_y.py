import astropy.io.fits as fits
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams.update({'font.size': 14})
import matplotlib.pyplot as p

from cycler import cycler
# 1. Setting prop cycle on default rc parameter
p.rc('lines', linewidth=1.5)
p.rcParams.update({'font.size': 14})
p.rc('axes', prop_cycle=cycler('color', ["#638bd9", "#e586b6", "#dd7c25", "#598664", "#9631a9", "#cff159", "#534f55", "#ab1519", "#89dbde"]) )


import numpy as n
import os
import sys
ll_dir = os.path.join(os.environ['OBS_REPO'], 'spm')

# comparison with wisconsin 

d = fits.open( os.path.join(ll_dir, 'Firefly_wisconsin-26.fits') )[1].data
prefix = 'Kroupa_MILES_'

z_agree =  ( d['Z_ERR_1']>0 )& ( d['Z_ERR_2']>0 )& (abs(d['Z_1'] - d['Z_2'])<0.001 )&( d['Z_1']>0 )&( d['Z_2']>0 )

converged = (d[prefix+'stellar_mass'] < 10**14. ) & (d[prefix+'stellar_mass'] > 0 )  & (d[prefix+'stellar_mass'] > d[prefix+'stellar_mass_low_1sig'] ) & (d[prefix+'stellar_mass'] < d[prefix+'stellar_mass_up_1sig'] ) & ( - n.log10(d[prefix+'stellar_mass_low_1sig'])  + n.log10(d[prefix+'stellar_mass_up_1sig']) < 0.8 )& (d['Kroupa_MILES_spm_EBV']<0.2)

ok = ( converged ) & (d['MSTELLAR_MEDIAN']>0)

DM = d['MSTELLAR_MEDIAN']-n.log10(d['Kroupa_MILES_stellar_mass'])

out_dir = os.path.join(os.environ['HOME'],'wwwDir', 'stuff')
#out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images/literature')

p.figure(1, (4.5, 4.5))
p.axes([0.18,0.18,0.8,0.73])
p.plot(d['MSTELLAR_MEDIAN'][ok], n.log10(d['Kroupa_MILES_stellar_mass'][ok]), 'k,'  , alpha=0.2, rasterized= True)
#p.plot(d['LOGMASS'][ok & ebv_agree], n.log10(d['Kroupa_MILES_stellar_mass'][ok & ebv_agree]), 'r,'  , alpha=0.2, rasterized= True, label=r'$\Delta (E(B-V))<0.02$')
p.plot(n.arange(6,13,0.1), n.arange(6,13,0.1), label='x=y', ls='dashed')
p.xlabel(r'$\log_{10}(M/M_\odot)$ (Wi DR12)')
p.ylabel(r'$\log_{10}(M/M_\odot)$ (FF DR14)')
p.xlim((7,12.5))
p.ylim((7,12.5))
p.title('SDSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "sdss_WI_MFF.png" ))
p.clf()


# DR12 boss


d = fits.open( os.path.join(ll_dir, 'Firefly_wisconsin-v5_10_0.fits') )[1].data
prefix = 'Kroupa_MILES_'

z_agree =  ( d['Z_ERR_NOQSO']>0 )& ( d['Z_ERR_2']>0 )& (abs(d['Z_NOQSO'] - d['Z_2'])<0.001 )&( d['Z_NOQSO']>0 )&( d['Z_2']>0 )

converged = (d[prefix+'stellar_mass'] < 10**14. ) & (d[prefix+'stellar_mass'] > 0 )  & (d[prefix+'stellar_mass'] > d[prefix+'stellar_mass_low_1sig'] ) & (d[prefix+'stellar_mass'] < d[prefix+'stellar_mass_up_1sig'] ) & ( - n.log10(d[prefix+'stellar_mass_low_1sig'])  + n.log10(d[prefix+'stellar_mass_up_1sig']) < 0.8 )& (d['Kroupa_MILES_spm_EBV']<0.2)

ok = ( converged ) & (d['MSTELLAR_MEDIAN']>0)

DM = d['MSTELLAR_MEDIAN']-n.log10(d['Kroupa_MILES_stellar_mass'])

out_dir = os.path.join(os.environ['HOME'],'wwwDir', 'stuff')
#out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images/literature')

p.figure(1, (4.5, 4.5))
p.axes([0.18,0.18,0.8,0.73])
p.plot(d['MSTELLAR_MEDIAN'][ok], n.log10(d['Kroupa_MILES_stellar_mass'][ok]), 'k,'  , alpha=0.2, rasterized= True)
#p.plot(d['LOGMASS'][ok & ebv_agree], n.log10(d['Kroupa_MILES_stellar_mass'][ok & ebv_agree]), 'r,'  , alpha=0.2, rasterized= True, label=r'$\Delta (E(B-V))<0.02$')
p.plot(n.arange(6,13,0.1), n.arange(6,13,0.1), label='x=y', ls='dashed')
p.xlabel(r'$\log_{10}(M/M_\odot)$ (Wi DR12)')
p.ylabel(r'$\log_{10}(M/M_\odot)$ (FF DR14)')
p.xlim((7,12.5))
p.ylim((7,12.5))
p.title('BOSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "boss_WI_MFF.png" ))
p.clf()


# comparison with portsmouth 


d = fits.open( os.path.join(ll_dir, 'Firefly_Krou_MILES_portsmouth_starforming_krou-26.fits') )[1].data

prefix = 'Kroupa_MILES_'

z_agree =  ( d['Z_ERR_1']>0 )& ( d['Z_ERR_2']>0 )& (abs(d['Z_1'] - d['Z_2'])<0.001 )&( d['Z_1']>0 )&( d['Z_2']>0 )

converged = (d[prefix+'stellar_mass'] < 10**14. ) & (d[prefix+'stellar_mass'] > 0 )  & (d[prefix+'stellar_mass'] > d[prefix+'stellar_mass_low_1sig'] ) & (d[prefix+'stellar_mass'] < d[prefix+'stellar_mass_up_1sig'] ) & ( - n.log10(d[prefix+'stellar_mass_low_1sig'])  + n.log10(d[prefix+'stellar_mass_up_1sig']) < 1. )

ebv_agree = (z_agree) & ( abs(d['E_BV'] - d['Kroupa_MILES_spm_EBV'])<0.02 ) & ( converged )


ok = ( z_agree ) & (d['LOGMASS']>0)

DM = d['LOGMASS']-n.log10(d['Kroupa_MILES_stellar_mass'])
DA = n.log10(d['AGE']*1e9)-n.log10(d['Kroupa_MILES_age_lightW'])

#out_dir = os.path.join(os.environ['HOME'],'wwwDir', 'stuff')
out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images/literature')

p.figure(1, (4.5, 4.5))
p.axes([0.18,0.18,0.8,0.73])
p.plot(d['LOGMASS'][ok], n.log10(d['Kroupa_MILES_stellar_mass'][ok]), 'k,'  , alpha=0.2, rasterized= True)
#p.plot(d['LOGMASS'][ok & ebv_agree], n.log10(d['Kroupa_MILES_stellar_mass'][ok & ebv_agree]), 'r,'  , alpha=0.2, rasterized= True, label=r'$\Delta (E(B-V))<0.02$')
p.plot(n.arange(6,13,0.1), n.arange(6,13,0.1), label='x=y', ls='dashed')
p.xlabel(r'$\log_{10}(M/M_\odot)$ (PSF DR12)')
p.ylabel(r'$\log_{10}(M/M_\odot)$ (FF DR14)')
p.xlim((7,12.5))
p.ylim((7,12.5))
p.title('SDSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "sdss26_MPSF_MFF.png" ))
p.clf()


p.figure(1, (4.5, 4.5))
p.axes([0.18,0.18,0.8,0.73])
p.plot(n.log10(d['AGE'][ok]*1e9), n.log10(d['Kroupa_MILES_age_lightW'][ok]), 'k,'  , alpha=0.2, rasterized= True)
#p.plot(n.log10(d['AGE'][ok & ebv_agree]*1e9), n.log10(d['Kroupa_MILES_age_lightW'][ok & ebv_agree]), 'r,'  , alpha=0.2, rasterized= True, label=r'$\Delta (E(B-V))<0.02$')
p.plot(n.arange(6,10,0.1), n.arange(6,10,0.1), label='x=y', ls='dashed')
p.xlabel(r'$\log_{10}(Age/yr)$ (PSF DR12)')
p.ylabel(r'$\log_{10}(Age/yr)$ (FF DR14)')
p.xlim((6,10.5))
p.ylim((6,10.5))
p.title('SDSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "sdss26_APSF_AFF.png" ))
p.clf()



d = fits.open( os.path.join(ll_dir, 'Firefly_Krou_MILES_portsmouth_starforming_krou-v5_10_0.fits') )[1].data

prefix = 'Kroupa_MILES_'

z_agree =  ( d['Z_ERR_1']>0 )& ( d['Z_ERR_2']>0 )& (abs(d['Z_1'] - d['Z_2'])<0.001 )&( d['Z_1']>0 )&( d['Z_2']>0 )

converged = (d[prefix+'stellar_mass'] < 10**14. ) & (d[prefix+'stellar_mass'] > 0 )  & (d[prefix+'stellar_mass'] > d[prefix+'stellar_mass_low_1sig'] ) & (d[prefix+'stellar_mass'] < d[prefix+'stellar_mass_up_1sig'] ) & ( - n.log10(d[prefix+'stellar_mass_low_1sig'])  + n.log10(d[prefix+'stellar_mass_up_1sig']) < 0.4 )

ebv_agree = (z_agree) & ( abs(d['E_BV'] - d['Kroupa_MILES_spm_EBV'])<0.02 ) & ( converged )


ok = ( z_agree ) & (d['LOGMASS']>0)

DM = d['LOGMASS']-n.log10(d['Kroupa_MILES_stellar_mass'])
DA = n.log10(d['AGE']*1e9)-n.log10(d['Kroupa_MILES_age_lightW'])

out_dir = os.path.join(os.environ['HOME'],'wwwDir', 'stuff')
#out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images/literature')

#p.figure(1, (4.5, 4.5))
#p.axes([0.18,0.18,0.8,0.73])
#p.plot(d['E_BV'][ok], d['Kroupa_MILES_spm_EBV'][ok], 'k,'  , alpha=0.2, rasterized= True)
##p.plot(d['LOGMASS'][ok & ebv_agree], n.log10(d['Kroupa_MILES_stellar_mass'][ok & ebv_agree]), 'r,'  , alpha=0.2, rasterized= True, label=r'$\Delta (E(B-V))<0.02$')
##p.plot(n.arange(6,13,0.1), n.arange(6,13,0.1), label='x=y', ls='dashed')
#p.xlabel('E(B-V) (PSF DR12)')
#p.ylabel('E(B-V) (FF DR14)')
#p.xlim((0,1.5))
#p.ylim((0,1.5))
#p.title('BOSS')
#p.legend(loc=0)
#p.grid()
#p.savefig(os.path.join(out_dir, "bossv5100_EBV_PSF_FF.png" ))
#p.clf()

p.figure(1, (4.5, 4.5))
p.axes([0.18,0.18,0.8,0.73])
p.plot(d['LOGMASS'][ok], n.log10(d['Kroupa_MILES_stellar_mass'][ok]), 'k,'  , alpha=0.2, rasterized= True, label='all')
#p.plot(d['LOGMASS'][ok & ebv_agree], n.log10(d['Kroupa_MILES_stellar_mass'][ok & ebv_agree]), 'r,'  , alpha=0.2, rasterized= True, label=r'$\Delta (E(B-V))<0.02$')
p.plot(n.arange(6,13,0.1), n.arange(6,13,0.1), label='x=y', ls='dashed')
p.xlabel(r'$\log_{10}(M/M_\odot)$ (PSF DR12)')
p.ylabel(r'$\log_{10}(M/M_\odot)$ (FF DR14)')
p.xlim((7,12.5))
p.ylim((7,12.5))
p.title('BOSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "bossv5100_MPSF_MFF.png" ))
p.clf()


p.figure(1, (4.5, 4.5))
p.axes([0.18,0.18,0.8,0.73])
p.plot(n.log10(d['AGE'][ok]*1e9), n.log10(d['Kroupa_MILES_age_lightW'][ok]), 'k,'  , alpha=0.2, rasterized= True, label='all')
#p.plot(n.log10(d['AGE'][ok & ebv_agree]*1e9), n.log10(d['Kroupa_MILES_age_lightW'][ok & ebv_agree]), 'r,'  , alpha=0.2, rasterized= True, label=r'$\Delta (E(B-V))<0.02$')
p.plot(n.arange(6,10,0.1), n.arange(6,10,0.1), label='x=y', ls='dashed')
p.xlabel(r'$\log_{10}(Age/yr)$ (PSF DR12)')
p.ylabel(r'$\log_{10}(Age/yr)$ (FF DR14)')
p.xlim((6,10.5))
p.ylim((6,10.5))
p.title('BOSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "bossv5100_APSF_AFF.png" ))
p.clf()

#METALLICITY



from scipy.stats import norm
out_dir = os.path.join(os.environ['HOME'],'wwwDir', 'stuff')
#out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images/sky')

def get_selections_DR14(catalog, z_name, z_err_name, class_name, zwarning, zflg_val, prefix):
	catalog_zOk =(catalog[z_err_name] > 0.) & (catalog[z_name] > catalog[z_err_name])  & (catalog[class_name]=='GALAXY')  & (catalog[zwarning]==zflg_val) & (catalog[z_name] > z_min) & (catalog[z_name] < z_max) 
	converged = (catalog_zOk)&(catalog[prefix+'stellar_mass'] > 0 )
	converged2 = (catalog_zOk)&(catalog[prefix+'stellar_mass'] < 10**13. ) & (catalog[prefix+'stellar_mass'] > 10**4 )  & (catalog[prefix+'stellar_mass'] > catalog[prefix+'stellar_mass_low_1sig'] ) & (catalog[prefix+'stellar_mass'] < catalog[prefix+'stellar_mass_up_1sig'] ) 
	dex04 = (converged2) & (catalog[prefix+'stellar_mass'] < 10**14. ) & (catalog[prefix+'stellar_mass'] > 0 )  & (catalog[prefix+'stellar_mass'] > catalog[prefix+'stellar_mass_low_1sig'] ) & (catalog[prefix+'stellar_mass'] < catalog[prefix+'stellar_mass_up_1sig'] ) & ( - n.log10(catalog[prefix+'stellar_mass_low_1sig'])  + n.log10(catalog[prefix+'stellar_mass_up_1sig']) < 0.8 )
	dex02 = (dex04) & ( - n.log10(catalog[prefix+'stellar_mass_low_1sig'])  + n.log10(catalog[prefix+'stellar_mass_up_1sig']) < 0.4 )
	m_catalog = n.log10(catalog[prefix+'stellar_mass'])
	w_catalog =  n.ones_like(catalog[prefix+'stellar_mass'])
	print(ld(catalog_zOk))
	return catalog_zOk, dex04, dex02 

#for IMF in imfs :

IMF = imfs[1]

gal, dex04, dex02 = get_selections_DR14(boss, 'Z_NOQSO', 'Z_ERR_NOQSO', 'CLASS_NOQSO', 'ZWARNING_NOQSO', 0., IMF)

rand = n.random.random(len(boss['PLUG_RA']))

rd = (rand<0.75)

p.figure(0, (9, 4.5))
p.axes([0.12,0.18,0.8,0.73])
p.plot(boss['PLUG_RA'][rd], boss['PLUG_DEC'][rd], 'k,'                , alpha=0.2, rasterized= True, label='all')
p.xlabel('Right Ascension [J2000, degrees]')
p.ylabel('Declination [J2000, degrees]')
p.title('eBOSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "eboss_ra_dec_all_"+IMF+".png" ))
p.clf()

p.figure(0, (9, 4.5))
p.axes([0.12,0.18,0.8,0.73])
p.plot(boss['PLUG_RA'][gal & rd], boss['PLUG_DEC'][gal & rd], 'k,'    , alpha=0.2, rasterized= True, label='galaxies')
p.xlabel('Right Ascension [J2000, degrees]')
p.ylabel('Declination [J2000, degrees]')
p.title('eBOSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "eboss_ra_dec_gal_"+IMF+".png" ))
p.clf()

p.figure(0, (9, 4.5))
p.axes([0.12,0.18,0.8,0.73])
p.plot(boss['PLUG_RA'][dex02 & rd], boss['PLUG_DEC'][dex02 & rd], 'k,', alpha=0.2, rasterized= True, label='$\sigma_{\log_{10}M}<0.2$ dex')
p.xlabel('Right Ascension [J2000, degrees]')
p.ylabel('Declination [J2000, degrees]')
p.title('eBOSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "eboss_ra_dec_dex02_"+IMF+".png" ))
p.clf()


p.figure(0, (9, 4.5))
p.axes([0.12,0.18,0.8,0.73])
p.plot(boss['PLUG_RA'][dex04 & rd], boss['PLUG_DEC'][dex04 & rd], 'k,', alpha=0.2, rasterized= True, label='$\sigma_{\log_{10}M}<0.4$ dex')
p.xlabel('Right Ascension [J2000, degrees]')
p.ylabel('Declination [J2000, degrees]')
p.title('eBOSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "eboss_ra_dec_dex04_"+IMF+".png" ))
p.clf()



gal, dex04, dex02 = get_selections_DR14(sdss, 'Z', 'Z_ERR', 'CLASS', 'ZWARNING', 0., IMF)

rand = n.random.random(len(sdss['PLUG_RA']))

rd = (rand<0.5)

p.figure(0, (9, 4.5))
p.axes([0.12,0.18,0.8,0.73])
p.plot(sdss['PLUG_RA'][rd], sdss['PLUG_DEC'][rd], 'k,'                , alpha=0.2, rasterized= True, label='all')
p.xlabel('Right Ascension [J2000, degrees]')
p.ylabel('Declination [J2000, degrees]')
p.title('SDSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "sdss_ra_dec_all_"+IMF+".png" ))
p.clf()

p.figure(0, (9, 4.5))
p.axes([0.12,0.18,0.8,0.73])
p.plot(sdss['PLUG_RA'][gal & rd], sdss['PLUG_DEC'][gal & rd], 'k,'    , alpha=0.2, rasterized= True, label='galaxies')
p.xlabel('Right Ascension [J2000, degrees]')
p.ylabel('Declination [J2000, degrees]')
p.title('SDSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "sdss_ra_dec_gal_"+IMF+".png" ))
p.clf()

p.figure(0, (9, 4.5))
p.axes([0.12,0.18,0.8,0.73])
p.plot(sdss['PLUG_RA'][dex02 & rd], sdss['PLUG_DEC'][dex02 & rd], 'k,', alpha=0.2, rasterized= True, label='$\sigma_{\log_{10}M}<0.2$ dex')
p.xlabel('Right Ascension [J2000, degrees]')
p.ylabel('Declination [J2000, degrees]')
p.title('SDSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "sdss_ra_dec_dex02_"+IMF+".png" ))
p.clf()


p.figure(0, (9, 4.5))
p.axes([0.12,0.18,0.8,0.73])
p.plot(sdss['PLUG_RA'][dex04 & rd], sdss['PLUG_DEC'][dex04 & rd], 'k,', alpha=0.2, rasterized= True, label='$\sigma_{\log_{10}M}<0.4$ dex')
p.xlabel('Right Ascension [J2000, degrees]')
p.ylabel('Declination [J2000, degrees]')
p.title('SDSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "sdss_ra_dec_dex04_"+IMF+".png" ))
p.clf()


