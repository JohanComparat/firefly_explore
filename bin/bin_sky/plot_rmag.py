from lib_spm import *
p.rc('lines', linewidth=1.5)

from scipy.stats import norm
out_dir = os.path.join(os.environ['HOME'],'wwwDir', 'stuff')
out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images/sky')

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


