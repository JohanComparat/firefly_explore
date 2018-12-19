from lib_spm import *
p.rc('lines', linewidth=1.5)

from scipy.stats import norm

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

#out_dir = os.path.join(os.environ['HOME'],'wwwDir', 'stuff')
out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images/sky')

gal, dex04, dex02 = get_selections_DR14(boss, 'Z_NOQSO', 'Z_ERR_NOQSO', 'CLASS_NOQSO', 'ZWARNING_NOQSO', 0., IMF)

ok = (boss['modelMag_r']>0)&(boss['modelMag_r']<40)
 
p.figure(1, (4.5, 4.5))
p.axes([0.18,0.18,0.8,0.73])
nn_1, bb, pp=p.hist(boss['modelMag_r'][ok]        , bins=100, lw=2, histtype='step', label='all')
nn_2, bb, pp=p.hist(boss['modelMag_r'][gal & ok]  , bins=bb, lw=2, histtype='step', label='galaxies')
nn_3, bb, pp=p.hist(boss['modelMag_r'][dex04 & ok], bins=bb, lw=2, histtype='step', label='$\sigma_{\log_{10}M}<0.4$ dex')
nn_4, bb, pp=p.hist(boss['modelMag_r'][dex02 & ok], bins=bb, lw=2, histtype='step', label='$\sigma_{\log_{10}M}<0.2$ dex')
p.xlim((16,23))
p.ylim((1e2,3e5))
p.yscale('log')
p.xlabel('r magnitude')
p.ylabel('Normed distribution')
p.title('eBOSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "eboss_rmag_hist_"+IMF+".png" ))
p.clf()

x_b = (bb[1:]+bb[:-1])*0.5

p.figure(1, (4.5, 4.5))
p.axes([0.18,0.18,0.8,0.73])
#p.plot(x_b, nn_2/nn_1, lw=2, label='all')
p.plot(x_b, nn_3/nn_2, lw=2, label='$\sigma_{\log_{10}M}<0.4$ dex')
p.plot(x_b, nn_4/nn_2, lw=2, label='$\sigma_{\log_{10}M}<0.2$ dex')
p.xlim((16,23))
p.ylim((0.0,1))
#p.yscale('log')
p.xlabel('r magnitude')
p.ylabel('N / N galaxies')
p.title('eBOSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "eboss_rmag_ratio_"+IMF+".png" ))
p.clf()

gal, dex04, dex02 = get_selections_DR14(sdss, 'Z', 'Z_ERR', 'CLASS', 'ZWARNING', 0., IMF)

ok = (sdss['modelMag_r']>0)&(sdss['modelMag_r']<40)
 
p.figure(1, (4.5, 4.5))
p.axes([0.18,0.18,0.8,0.73])
nn_1, bb, pp=p.hist(sdss['modelMag_r'][ok]        , bins=100, lw=2, histtype='step', label='all')
nn_2, bb, pp=p.hist(sdss['modelMag_r'][gal & ok]  , bins=bb, lw=2, histtype='step', label='galaxies')
nn_3, bb, pp=p.hist(sdss['modelMag_r'][dex04 & ok], bins=bb, lw=2, histtype='step', label='$\sigma_{\log_{10}M}<0.4$ dex')
nn_4, bb, pp=p.hist(sdss['modelMag_r'][dex02 & ok], bins=bb, lw=2, histtype='step', label='$\sigma_{\log_{10}M}<0.2$ dex')
p.xlim((16,23))
p.ylim((1e2,3e5))
p.yscale('log')
p.xlabel('r magnitude')
p.ylabel('Normed distribution')
p.title('SDSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "sdss_rmag_hist_"+IMF+".png" ))
p.clf()

x_b = (bb[1:]+bb[:-1])*0.5

p.figure(1, (4.5, 4.5))
p.axes([0.18,0.18,0.8,0.73])
#p.plot(x_b, nn_2/nn_1, lw=2, label='all')
p.plot(x_b, nn_3/nn_2, lw=2, label='$\sigma_{\log_{10}M}<0.4$ dex')
p.plot(x_b, nn_4/nn_2, lw=2, label='$\sigma_{\log_{10}M}<0.2$ dex')
p.xlim((16,23))
p.ylim((0.0,1))
#p.yscale('log')
p.xlabel('r magnitude')
p.ylabel('N / N galaxies')
p.title('SDSS')
p.legend(loc=0)
p.grid()
p.savefig(os.path.join(out_dir, "sdss_rmag_ratio_"+IMF+".png" ))
p.clf()

