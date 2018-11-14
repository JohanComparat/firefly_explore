from lib_spm import *

#out_dir = os.path.join('/data42s/comparat/firefly/v1_1_0/figures', 'mass-redshift-presentation')
out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images', 'az')

def plot_az_boss(imf_ref):
	stellar_mass = imf_ref+'stellar_mass'
	age = imf_ref+'age_massW'
	metal = imf_ref+'metallicity_massW'
	redshift_reliable_boss =  (boss['CLASS_NOQSO'] == "GALAXY") & ( boss['Z_ERR_NOQSO'] > 0.0) & (boss['ZWARNING_NOQSO'] == 0) & (boss['Z_NOQSO']>0.001) & (boss['Z_NOQSO'] > boss['Z_ERR_NOQSO'] ) # (boss['SN_MEDIAN_ALL'] > 0.1 ) & 
	#redshift_reliable_sdss =  (sdss['CLASS'] == "GALAXY")       & ( sdss['Z_ERR'] > 0.0)       & (sdss['ZWARNING'] == 0)       & (sdss['Z'] > 0.001) & (sdss['Z'] > sdss['Z_ERR'] ) # (sdss['SN_MEDIAN_ALL'] > 0.1 ) &
	error_reliable_boss = (boss[stellar_mass+'_up_1sig'] > boss[stellar_mass+'_low_1sig'] ) & (boss[stellar_mass+'_up_1sig'] > 0. ) & ( boss[stellar_mass+'_low_1sig'] > 0. ) & (boss[stellar_mass+'_up_1sig'] < 1e14 ) & ( boss[stellar_mass+'_low_1sig'] < 1e14 ) 
	#error_reliable_sdss = (sdss[stellar_mass+'_up_1sig'] > sdss[stellar_mass+'_low_1sig'] ) & (sdss[stellar_mass+'_up_1sig'] > 0. ) & ( sdss[stellar_mass+'_low_1sig'] > 0. ) & (sdss[stellar_mass+'_up_1sig'] < 1e14 ) & ( sdss[stellar_mass+'_low_1sig'] < 1e14 ) 
	mass_reliable_boss_04 = (boss[stellar_mass] > 1e6 ) & ( boss[stellar_mass] < 1e14 ) & ((n.log10(boss[stellar_mass+'_up_1sig']) - n.log10(boss[stellar_mass+'_low_1sig']))/2. < 0.4 )
	#mass_reliable_sdss_04 = (sdss[stellar_mass] > 1e6 ) & ( sdss[stellar_mass] < 1e14 ) & ((n.log10(sdss[stellar_mass+'_up_1sig']) - n.log10(sdss[stellar_mass+'_low_1sig']))/2. < 0.4 )
	ok_boss_04 = (error_reliable_boss) & (mass_reliable_boss_04) & (redshift_reliable_boss)
	#ok_sdss_04 = (error_reliable_sdss) & (mass_reliable_sdss_04) & (redshift_reliable_sdss)
	A_04_ref = n.log10(boss[age][ok_boss_04]           )
	Z_04_ref = n.log10(boss[metal][ok_boss_04]         )
	a_bins = n.arange(6.5, 10.5, 0.1)
	z_bins = n.arange(-3,3,0.1)
	XX, YY = n.meshgrid((z_bins[1:]+z_bins[:-1])/2., 0.5*(a_bins[1:]+a_bins[:-1]))
	
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(Z_04_ref, A_04_ref, bins=[z_bins, a_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s', vmin=1, vmax=4 )
	p.xlim((-2.2,0.5))
	p.ylim((7.3,10.5))
	p.ylabel(r'$\log_{10}(Age/yr)$')
	p.xlabel(r'$\log_{10}(Z/Z_\odot)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	p.legend(loc=0, frameon = False)
	p.grid()
	p.text(-2.2,7.3,'eBOSS '+imf_ref)
	p.tight_layout()
	p.savefig(os.path.join(out_dir, "age_metallicity_"+imf_ref+"eboss_04.png" ))
	p.clf()
	
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(Z_04_ref, A_04_ref, bins=[z_bins, a_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s', vmin=1, vmax=4 )
	p.xlim((-2.2,0.5))
	p.ylim((7.3,10.5))
	p.ylabel(r'$\log_{10}(Age/yr)$')
	p.xlabel(r'$\log_{10}(Z/Z_\odot)$')
	#p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	p.legend(loc=0, frameon = False)
	p.text(-2.2,7.3,'eBOSS '+imf_ref)
	p.grid()
	p.tight_layout()
	p.savefig(os.path.join(out_dir, "no_CB_age_metallicity_"+imf_ref+"eboss_04.png" ))
	p.clf()
	
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(Z_04_ref, A_04_ref, bins=[z_bins, a_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s', vmin=1, vmax=4 )
	p.xlim((-2.2,0.5))
	p.ylim((7.3,10.5))
	p.ylabel(r'$\log_{10}(Age/yr)$')
	#p.xlabel(r'$\log_{10}(Z/Z_\odot)$')
	#p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	p.legend(loc=0, frameon = False)
	p.text(-2.2,7.3,'eBOSS '+imf_ref)
	p.grid()
	p.tight_layout()
	p.savefig(os.path.join(out_dir, "no_CBX_age_metallicity_"+imf_ref+"eboss_04.png" ))
	p.clf()
	
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(Z_04_ref, A_04_ref, bins=[z_bins, a_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s', vmin=1, vmax=4 )
	p.xlim((-2.2,0.5))
	p.ylim((7.3,10.5))
	#p.ylabel(r'$\log_{10}(Age/yr)$')
	#p.xlabel(r'$\log_{10}(Z/Z_\odot)$')
	#p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	p.legend(loc=0, frameon = False)
	p.grid()
	p.text(-2.2,7.3,'eBOSS '+imf_ref)
	p.tight_layout()
	p.savefig(os.path.join(out_dir, "no_CBXY_age_metallicity_"+imf_ref+"eboss_04.png" ))
	p.clf()
	
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(Z_04_ref, A_04_ref, bins=[z_bins, a_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s', vmin=1, vmax=4 )
	p.xlim((-2.2,0.5))
	p.ylim((7.3,10.5))
	#p.ylabel(r'$\log_{10}(Age/yr)$')
	p.xlabel(r'$\log_{10}(Z/Z_\odot)$')
	#p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	p.legend(loc=0, frameon = False)
	p.grid()
	p.text(-2.2,7.3,'eBOSS '+imf_ref)
	p.tight_layout()
	p.savefig(os.path.join(out_dir, "no_CBY_age_metallicity_"+imf_ref+"eboss_04.png" ))
	p.clf()
	

def plot_az_sdss(imf_ref):
	stellar_mass = imf_ref+'stellar_mass'
	age = imf_ref+'age_massW'
	metal = imf_ref+'metallicity_massW'
	redshift_reliable_sdss =  (sdss['CLASS'] == "GALAXY")       & ( sdss['Z_ERR'] > 0.0)       & (sdss['ZWARNING'] == 0)       & (sdss['Z'] > 0.001) & (sdss['Z'] > sdss['Z_ERR'] ) 
	error_reliable_sdss = (sdss[stellar_mass+'_up_1sig'] > sdss[stellar_mass+'_low_1sig'] ) & (sdss[stellar_mass+'_up_1sig'] > 0. ) & ( sdss[stellar_mass+'_low_1sig'] > 0. ) & (sdss[stellar_mass+'_up_1sig'] < 1e14 ) & ( sdss[stellar_mass+'_low_1sig'] < 1e14 ) 
	mass_reliable_sdss_04 = (sdss[stellar_mass] > 1e6 ) & ( sdss[stellar_mass] < 1e14 ) & ((n.log10(sdss[stellar_mass+'_up_1sig']) - n.log10(sdss[stellar_mass+'_low_1sig']))/2. < 0.4 )
	ok_sdss_04 = (error_reliable_sdss) & (mass_reliable_sdss_04) & (redshift_reliable_sdss)
	A_04_ref = n.log10(sdss[age][ok_sdss_04]           )
	Z_04_ref = n.log10(sdss[metal][ok_sdss_04]         )
	a_bins = n.arange(6.5, 10.5, 0.1)
	z_bins = n.arange(-3,3,0.1)
	XX, YY = n.meshgrid((z_bins[1:]+z_bins[:-1])/2., 0.5*(a_bins[1:]+a_bins[:-1]))
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(Z_04_ref, A_04_ref, bins=[z_bins, a_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' , vmin=1, vmax=4)
	p.xlim((-2.2,0.5))
	p.ylim((7.3,10.5))
	p.ylabel(r'$\log_{10}(Age/yr)$')
	p.xlabel(r'$\log_{10}(Z/Z_\odot)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	p.legend(loc=0, frameon = False)
	p.grid()
	p.tight_layout()
	p.savefig(os.path.join(out_dir, "age_metallicity_"+imf_ref+"sdss_04.png" ))
	p.clf()


def plot_az_deep2(imf_ref):
	stellar_mass = imf_ref+'stellar_mass'
	age = imf_ref+'age_massW'
	metal = imf_ref+'metallicity_massW'
	z_flg = 'ZQUALITY'
	z_name = 'ZBEST'
	deep2_zOk = (deep2[z_name] > 0.6) & (deep2[z_flg]>=2.) & (deep2[z_name] < 1.2) & (deep2['SSR']>0) & (deep2['TSR']>0) & (deep2['SSR']<=1.0001) & (deep2['TSR']<=1.0001)
	deep2_sel_04 = (deep2_zOk) & (deep2[stellar_mass] < 10**14. ) & (deep2[stellar_mass] > 0. )  & (deep2[stellar_mass] >= deep2[stellar_mass+'_low_1sig'] ) & (deep2[stellar_mass] <= deep2[stellar_mass+'_up_1sig'] ) & ( - n.log10(deep2[stellar_mass+'_low_1sig'])  + n.log10(deep2[stellar_mass+'_up_1sig']) < 0.8 )
	A_04_ref = n.log10(deep2[age][deep2_sel_04]           )
	Z_04_ref = n.log10(deep2[metal][deep2_sel_04]         )
	a_bins = n.arange(6.5, 10.5, 0.1)
	z_bins = n.arange(-3,3,0.1)
	XX, YY = n.meshgrid((z_bins[1:]+z_bins[:-1])/2., 0.5*(a_bins[1:]+a_bins[:-1]))
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(Z_04_ref, A_04_ref, bins=[z_bins, a_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' , vmin=1, vmax=2.5)
	p.xlim((-2.2,0.5))
	p.ylim((7.3,10.5))
	p.ylabel(r'$\log_{10}(Age/yr)$')
	p.xlabel(r'$\log_{10}(Z/Z_\odot)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	p.legend(loc=0, frameon = False)
	p.grid()
	p.tight_layout()
	p.savefig(os.path.join(out_dir, "age_metallicity_"+imf_ref+"deep2_04.png" ))
	p.clf()


plot_az_deep2(imf_ref = imfs[0])
plot_az_deep2(imf_ref = imfs[1])
plot_az_deep2(imf_ref = imfs[2])
plot_az_deep2(imf_ref = imfs[3])
plot_az_deep2(imf_ref = imfs[4])
plot_az_deep2(imf_ref = imfs[5])
plot_az_deep2(imf_ref = imfs[6])
plot_az_deep2(imf_ref = imfs[7])
plot_az_deep2(imf_ref = imfs[8])


plot_az_sdss(imf_ref = imfs[0])
plot_az_sdss(imf_ref = imfs[1])
plot_az_sdss(imf_ref = imfs[2])
plot_az_sdss(imf_ref = imfs[3])
plot_az_sdss(imf_ref = imfs[4])
plot_az_sdss(imf_ref = imfs[5])
plot_az_sdss(imf_ref = imfs[6])
plot_az_sdss(imf_ref = imfs[7])
plot_az_sdss(imf_ref = imfs[8])


plot_az_boss(imf_ref = imfs[0])
plot_az_boss(imf_ref = imfs[1])
plot_az_boss(imf_ref = imfs[2])
plot_az_boss(imf_ref = imfs[3])
plot_az_boss(imf_ref = imfs[4])
plot_az_boss(imf_ref = imfs[5])
plot_az_boss(imf_ref = imfs[6])
plot_az_boss(imf_ref = imfs[7])
plot_az_boss(imf_ref = imfs[8])
