from lib_spm import *

#out_dir = os.path.join('/data42s/comparat/firefly/v1_1_0/figures', 'mass-redshift-presentation')
out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images', 'dust-mass')

def plot_dm_boss(imf_ref):
	stellar_mass = imf_ref+'stellar_mass'
	age = imf_ref+'age_massW'
	metal = imf_ref+'metallicity_massW'
	ebv = imf_ref+'spm_EBV'
	redshift_reliable_boss =  (boss['CLASS_NOQSO'] == "GALAXY") & ( boss['Z_ERR_NOQSO'] > 0.0) & (boss['ZWARNING_NOQSO'] == 0) & (boss['Z_NOQSO']>0.001) & (boss['Z_NOQSO'] > boss['Z_ERR_NOQSO'] ) # (boss['SN_MEDIAN_ALL'] > 0.1 ) & 
	#redshift_reliable_sdss =  (sdss['CLASS'] == "GALAXY")       & ( sdss['Z_ERR'] > 0.0)       & (sdss['ZWARNING'] == 0)       & (sdss['Z'] > 0.001) & (sdss['Z'] > sdss['Z_ERR'] ) # (sdss['SN_MEDIAN_ALL'] > 0.1 ) &
	error_reliable_boss = (boss[stellar_mass+'_up_1sig'] > boss[stellar_mass+'_low_1sig'] ) & (boss[stellar_mass+'_up_1sig'] > 0. ) & ( boss[stellar_mass+'_low_1sig'] > 0. ) & (boss[stellar_mass+'_up_1sig'] < 1e14 ) & ( boss[stellar_mass+'_low_1sig'] < 1e14 ) 
	#error_reliable_sdss = (sdss[stellar_mass+'_up_1sig'] > sdss[stellar_mass+'_low_1sig'] ) & (sdss[stellar_mass+'_up_1sig'] > 0. ) & ( sdss[stellar_mass+'_low_1sig'] > 0. ) & (sdss[stellar_mass+'_up_1sig'] < 1e14 ) & ( sdss[stellar_mass+'_low_1sig'] < 1e14 ) 
	mass_reliable_boss_04 = (boss[stellar_mass] > 1e6 ) & ( boss[stellar_mass] < 1e14 ) & ((n.log10(boss[stellar_mass+'_up_1sig']) - n.log10(boss[stellar_mass+'_low_1sig']))/2. < 0.4 )
	#mass_reliable_sdss_04 = (sdss[stellar_mass] > 1e6 ) & ( sdss[stellar_mass] < 1e14 ) & ((n.log10(sdss[stellar_mass+'_up_1sig']) - n.log10(sdss[stellar_mass+'_low_1sig']))/2. < 0.4 )
	ok_boss_04 = (error_reliable_boss) & (mass_reliable_boss_04) & (redshift_reliable_boss)
	#ok_sdss_04 = (error_reliable_sdss) & (mass_reliable_sdss_04) & (redshift_reliable_sdss)
	M_04_ref = n.log10(boss[stellar_mass][ok_boss_04]           )
	E_04_ref = boss[ebv][ok_boss_04]         
	m_bins = n.arange(6.5, 12.6, 0.25)
	e_bins = n.arange(0,0.71,0.05)
	XX, YY = n.meshgrid((e_bins[1:]+e_bins[:-1])/2., 0.5*(m_bins[1:]+m_bins[:-1]))

	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(E_04_ref, M_04_ref, bins=[e_bins, m_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s', vmin=1, vmax=4 )
	p.ylabel(r'$\log_{10}(M/M_\odot)$')
	p.xlabel(r'$E(B-V)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	#p.legend(loc=0, frameon = False)
	p.xlim((-0.01,0.71))
	p.ylim((5.5,12.5))
	p.text(0.01, 6.,'eBOSS '+imf_ref.split('_')[1] )
	p.tight_layout()
	p.grid()
	p.savefig(os.path.join(out_dir, "dust_mass_"+imf_ref+"eboss_04.png" ))
	p.clf()
	
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(E_04_ref, M_04_ref, bins=[e_bins, m_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s', vmin=1, vmax=4 )
	#p.ylabel(r'$\log_{10}(M/M_\odot)$')
	p.xlabel(r'$E(B-V)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	#p.legend(loc=0, frameon = False)
	p.xlim((-0.01,0.71))
	p.ylim((5.5,12.5))
	p.text(0.01, 6.,'eBOSS '+imf_ref.split('_')[1] )
	p.tight_layout()
	p.grid()
	p.savefig(os.path.join(out_dir, "no_Y_dust_mass_"+imf_ref+"eboss_04.png" ))
	p.clf()
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(E_04_ref, M_04_ref, bins=[e_bins, m_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s', vmin=1, vmax=4 )
	p.ylabel(r'$\log_{10}(M/M_\odot)$')
	#p.xlabel(r'$E(B-V)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	#p.legend(loc=0, frameon = False)
	p.xlim((-0.01,0.71))
	p.ylim((5.5,12.5))
	p.text(0.01, 6.,'eBOSS '+imf_ref.split('_')[1] )
	p.tight_layout()
	p.grid()
	p.savefig(os.path.join(out_dir, "no_X_dust_mass_"+imf_ref+"eboss_04.png" ))
	p.clf()
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(E_04_ref, M_04_ref, bins=[e_bins, m_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s', vmin=1, vmax=4 )
	#p.ylabel(r'$\log_{10}(M/M_\odot)$')
	#p.xlabel(r'$E(B-V)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	#p.legend(loc=0, frameon = False)
	p.xlim((-0.01,0.71))
	p.ylim((5.5,12.5))
	p.text(0.01, 6.,'eBOSS '+imf_ref.split('_')[1] )
	p.tight_layout()
	p.grid()
	p.savefig(os.path.join(out_dir, "no_XY_dust_mass_"+imf_ref+"eboss_04.png" ))
	p.clf()
	
def plot_dm_sdss(imf_ref):
	stellar_mass = imf_ref+'stellar_mass'
	age = imf_ref+'age_massW'
	metal = imf_ref+'metallicity_massW'
	ebv = imf_ref+'spm_EBV'
	redshift_reliable_sdss =  (sdss['CLASS'] == "GALAXY")       & ( sdss['Z_ERR'] > 0.0)       & (sdss['ZWARNING'] == 0)       & (sdss['Z'] > 0.001) & (sdss['Z'] > sdss['Z_ERR'] ) 
	error_reliable_sdss = (sdss[stellar_mass+'_up_1sig'] > sdss[stellar_mass+'_low_1sig'] ) & (sdss[stellar_mass+'_up_1sig'] > 0. ) & ( sdss[stellar_mass+'_low_1sig'] > 0. ) & (sdss[stellar_mass+'_up_1sig'] < 1e14 ) & ( sdss[stellar_mass+'_low_1sig'] < 1e14 ) 
	mass_reliable_sdss_04 = (sdss[stellar_mass] > 1e6 ) & ( sdss[stellar_mass] < 1e14 ) & ((n.log10(sdss[stellar_mass+'_up_1sig']) - n.log10(sdss[stellar_mass+'_low_1sig']))/2. < 0.4 )
	ok_sdss_04 = (error_reliable_sdss) & (mass_reliable_sdss_04) & (redshift_reliable_sdss)
	M_04_ref = n.log10(sdss[stellar_mass][ok_sdss_04]           )
	E_04_ref = sdss[ebv][ok_sdss_04]         
	m_bins = n.arange(6.5, 12.6, 0.25)
	e_bins = n.arange(0,0.71,0.05)
	XX, YY = n.meshgrid((e_bins[1:]+e_bins[:-1])/2., 0.5*(m_bins[1:]+m_bins[:-1]))
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(E_04_ref, M_04_ref, bins=[e_bins, m_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' , vmin=1, vmax=4)
	p.ylabel(r'$\log_{10}(M/M_\odot)$')
	p.xlabel(r'$E(B-V)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	#p.legend(loc=0, frameon = False)
	p.xlim((-0.01,0.71))
	p.ylim((5.5,12.5))
	p.text(0.01, 6.,'SDSS '+imf_ref.split('_')[1] )
	p.grid()
	p.savefig(os.path.join(out_dir, "dust_mass_"+imf_ref+"sdss_04.png" ))
	p.clf()
	
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(E_04_ref, M_04_ref, bins=[e_bins, m_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' , vmin=1, vmax=4)
	p.ylabel(r'$\log_{10}(M/M_\odot)$')
	#p.xlabel(r'$E(B-V)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	#p.legend(loc=0, frameon = False)
	p.xlim((-0.01,0.71))
	p.ylim((5.5,12.5))
	p.text(0.01, 6.,'SDSS '+imf_ref.split('_')[1] )
	p.grid()
	p.savefig(os.path.join(out_dir, "no_X_dust_mass_"+imf_ref+"sdss_04.png" ))
	p.clf()
	
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(E_04_ref, M_04_ref, bins=[e_bins, m_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' , vmin=1, vmax=4)
	#p.ylabel(r'$\log_{10}(M/M_\odot)$')
	p.xlabel(r'$E(B-V)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	#p.legend(loc=0, frameon = False)
	p.xlim((-0.01,0.71))
	p.ylim((5.5,12.5))
	p.text(0.01, 6.,'SDSS '+imf_ref.split('_')[1] )
	p.grid()
	p.savefig(os.path.join(out_dir, "no_Y_dust_mass_"+imf_ref+"sdss_04.png" ))
	p.clf()
	
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(E_04_ref, M_04_ref, bins=[e_bins, m_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' , vmin=1, vmax=4)
	#p.ylabel(r'$\log_{10}(M/M_\odot)$')
	#p.xlabel(r'$E(B-V)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	#p.legend(loc=0, frameon = False)
	p.xlim((-0.01,0.71))
	p.ylim((5.5,12.5))
	p.text(0.01, 6.,'SDSS '+imf_ref.split('_')[1] )
	p.grid()
	p.savefig(os.path.join(out_dir, "no_XY_dust_mass_"+imf_ref+"sdss_04.png" ))
	p.clf()


def plot_dm_deep2(imf_ref):
	stellar_mass = imf_ref+'stellar_mass'
	age = imf_ref+'age_massW'
	metal = imf_ref+'metallicity_massW'
	ebv = imf_ref+'spm_EBV'
	z_flg = 'ZQUALITY'
	z_name = 'ZBEST'
	deep2_zOk = (deep2[z_name] > 0.6) & (deep2[z_flg]>=2.) & (deep2[z_name] < 1.2) & (deep2['SSR']>0) & (deep2['TSR']>0) & (deep2['SSR']<=1.0001) & (deep2['TSR']<=1.0001)
	ok_deep2_04 = (deep2_zOk) & (deep2[stellar_mass] < 10**14. ) & (deep2[stellar_mass] > 0. )  & (deep2[stellar_mass] >= deep2[stellar_mass+'_low_1sig'] ) & (deep2[stellar_mass] <= deep2[stellar_mass+'_up_1sig'] ) & ( - n.log10(deep2[stellar_mass+'_low_1sig'])  + n.log10(deep2[stellar_mass+'_up_1sig']) < 0.8 )
	M_04_ref = n.log10(deep2[stellar_mass][ok_deep2_04]           )
	E_04_ref = deep2[ebv][ok_deep2_04]         
	m_bins = n.arange(6.5, 12.6, 0.25)
	e_bins = n.arange(0,0.71,0.05)
	XX, YY = n.meshgrid((e_bins[1:]+e_bins[:-1])/2., 0.5*(m_bins[1:]+m_bins[:-1]))
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(E_04_ref, M_04_ref, bins=[e_bins, m_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' , vmin=1, vmax=2.5)
	p.ylabel(r'$\log_{10}(M/M_\odot)$')
	p.xlabel(r'$E(B-V)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	p.xlim((-0.01,0.71))
	p.ylim((5.5,12.5))
	p.text(0.01, 6.,'DEEP2 '+imf_ref.split('_')[1] )
	#p.legend(loc=0, frameon = False)
	p.grid()
	p.savefig(os.path.join(out_dir, "dust_mass_"+imf_ref+"deep2_04.png" ))
	p.clf()

	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(E_04_ref, M_04_ref, bins=[e_bins, m_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' , vmin=1, vmax=2.5)
	p.ylabel(r'$\log_{10}(M/M_\odot)$')
	#p.xlabel(r'$E(B-V)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	p.xlim((-0.01,0.71))
	p.ylim((5.5,12.5))
	p.text(0.01, 6.,'DEEP2 '+imf_ref.split('_')[1] )
	#p.legend(loc=0, frameon = False)
	p.grid()
	p.savefig(os.path.join(out_dir, "no_X_dust_mass_"+imf_ref+"deep2_04.png" ))
	p.clf()
	
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(E_04_ref, M_04_ref, bins=[e_bins, m_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' , vmin=1, vmax=2.5)
	#p.ylabel(r'$\log_{10}(M/M_\odot)$')
	p.xlabel(r'$E(B-V)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	p.xlim((-0.01,0.71))
	p.ylim((5.5,12.5))
	p.text(0.01, 6.,'DEEP2 '+imf_ref.split('_')[1] )
	#p.legend(loc=0, frameon = False)
	p.grid()
	p.savefig(os.path.join(out_dir, "no_Y_dust_mass_"+imf_ref+"deep2_04.png" ))
	p.clf()
	
	p.figure(0, (5.5, 4.5))
	p.axes([0.2,0.2,0.7,0.7])
	HH = n.histogram2d(E_04_ref, M_04_ref, bins=[e_bins, m_bins])[0].T
	p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' , vmin=1, vmax=2.5)
	#p.ylabel(r'$\log_{10}(M/M_\odot)$')
	#p.xlabel(r'$E(B-V)$')
	p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
	p.xlim((-0.01,0.71))
	p.ylim((5.5,12.5))
	p.text(0.01, 6.,'DEEP2 '+imf_ref.split('_')[1] )
	#p.legend(loc=0, frameon = False)
	p.grid()
	p.savefig(os.path.join(out_dir, "no_XY_dust_mass_"+imf_ref+"deep2_04.png" ))
	p.clf()

plot_dm_deep2(imf_ref = imfs[0])
plot_dm_deep2(imf_ref = imfs[1])
plot_dm_deep2(imf_ref = imfs[2])
plot_dm_deep2(imf_ref = imfs[3])
plot_dm_deep2(imf_ref = imfs[4])
plot_dm_deep2(imf_ref = imfs[5])
plot_dm_deep2(imf_ref = imfs[6])
plot_dm_deep2(imf_ref = imfs[7])
plot_dm_deep2(imf_ref = imfs[8])


plot_dm_sdss(imf_ref = imfs[0])
plot_dm_sdss(imf_ref = imfs[1])
plot_dm_sdss(imf_ref = imfs[2])
plot_dm_sdss(imf_ref = imfs[3])
plot_dm_sdss(imf_ref = imfs[4])
plot_dm_sdss(imf_ref = imfs[5])
plot_dm_sdss(imf_ref = imfs[6])
plot_dm_sdss(imf_ref = imfs[7])
plot_dm_sdss(imf_ref = imfs[8])


plot_dm_boss(imf_ref = imfs[0])
plot_dm_boss(imf_ref = imfs[1])
plot_dm_boss(imf_ref = imfs[2])
plot_dm_boss(imf_ref = imfs[3])
plot_dm_boss(imf_ref = imfs[4])
plot_dm_boss(imf_ref = imfs[5])
plot_dm_boss(imf_ref = imfs[6])
plot_dm_boss(imf_ref = imfs[7])
plot_dm_boss(imf_ref = imfs[8])
