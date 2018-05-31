from lib_spm import *
from scipy.stats import norm
#out_dir = os.path.join('/data42s/comparat/firefly/v1_1_0/figures', 'mass-redshift-presentation')
out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images/ebv')

m_bins = n.arange(-1., 1., 0.01)


def plotDIFF_fixed_imf_deep2(imf_ref, imf_1, imf_2):
	print('deep2')
	stellar_mass = imf_ref+'stellar_mass'
	ebv = imf_ref+'spm_EBV'
	z_flg = 'ZQUALITY'
	z_name = 'ZBEST'
	deep2_zOk = (deep2[z_name] > 0.6) & (deep2[z_flg]>=2.) & (deep2[z_name] < 1.2) & (deep2['SSR']>0) & (deep2['TSR']>0) & (deep2['SSR']<=1.0001) & (deep2['TSR']<=1.0001)
	deep2_sel_02 = (deep2_zOk) & (deep2[stellar_mass] < 10**14. ) & (deep2[stellar_mass] > 0. )  & (deep2[stellar_mass] >= deep2[stellar_mass+'_low_1sig'] ) & (deep2[stellar_mass] <= deep2[stellar_mass+'_up_1sig'] ) & ( - n.log10(deep2[stellar_mass+'_low_1sig'])  + n.log10(deep2[stellar_mass+'_up_1sig']) < 0.4 )
	deep2_sel_04 = (deep2_zOk) & (deep2[stellar_mass] < 10**14. ) & (deep2[stellar_mass] > 0. )  & (deep2[stellar_mass] >= deep2[stellar_mass+'_low_1sig'] ) & (deep2[stellar_mass] <= deep2[stellar_mass+'_up_1sig'] ) & ( - n.log10(deep2[stellar_mass+'_low_1sig'])  + n.log10(deep2[stellar_mass+'_up_1sig']) < 0.8 )&(deep2[ebv]>0)
	# defines ref quantity
	ebv_04_ref = deep2[ebv][deep2_sel_04]
	# quantity to compare to
	ebv_1 = imf_1+'spm_EBV'
	ebv_04_1 = deep2[ebv_1][deep2_sel_04]
	# quantity to compare to
	ebv_2 = imf_2+'spm_EBV'
	ebv_04_2 = deep2[ebv_2][deep2_sel_04]
	# normalized comparison ratio
	delta_m1 = (ebv_04_1-ebv_04_ref)
	delta_m2 = (ebv_04_2-ebv_04_ref)
	# figure
	p.figure(2, (4.5, 4.5))
	p.axes([0.12,0.18,0.8,0.73])
	p.hist(delta_m1, bins=m_bins, histtype='step', label=imf_1.split('_')[1]+"-"+imf_ref.split('_')[1] , normed=True, lw=2 )
	p.hist(delta_m2, bins=m_bins, histtype='step', label=imf_2.split('_')[1]+"-"+imf_ref.split('_')[1] , normed=True, lw=2 )
	#p.plot(m_bins, norm.pdf(m_bins, loc=0, scale=1), label='N(0,1)', ls='dashed')
	p.ylabel('normed distribution')
	p.xlabel(r'$E(B-V)-E(B-V)_{ref}$')
	p.title('DEEP2 '+imf_ref.split('_')[0])
	p.legend(loc=2, frameon = False, fontsize=11)
	p.xlim((-0.7, 0.7))
	p.grid()
	p.savefig(os.path.join(out_dir, "delta_EBV_distribution_deep2"+imf_ref.split('_')[0]+".png" ))
	p.clf()



plotDIFF_fixed_imf_deep2(	imf_ref = imfs[0], 	imf_1   = imfs[1], 	imf_2   = imfs[2])
plotDIFF_fixed_imf_deep2(	imf_ref = imfs[3], 	imf_1   = imfs[4], 	imf_2   = imfs[5])
plotDIFF_fixed_imf_deep2(	imf_ref = imfs[6], 	imf_1   = imfs[7], 	imf_2   = imfs[8])

def plotDIFF_fixed_imf_sdss(imf_ref, imf_1, imf_2):
	print('sdss')
	stellar_mass = imf_ref+'stellar_mass'
	ebv = imf_ref+'spm_EBV'
	# selections boo
	redshift_reliable_sdss =  (sdss['CLASS'] == "GALAXY")       & ( sdss['Z_ERR'] > 0.0)       & (sdss['ZWARNING'] == 0)       & (sdss['Z'] > 0.001) & (sdss['Z'] > sdss['Z_ERR'] ) # (sdss['SN_MEDIAN_ALL'] > 0.1 ) &
	error_reliable_sdss = (sdss[stellar_mass+'_up_1sig'] > sdss[stellar_mass+'_low_1sig'] ) & (sdss[stellar_mass+'_up_1sig'] > 0. ) & ( sdss[stellar_mass+'_low_1sig'] > 0. ) & (sdss[stellar_mass+'_up_1sig'] < 1e14 ) & ( sdss[stellar_mass+'_low_1sig'] < 1e14 ) 
	mass_reliable_sdss_02 = (sdss[stellar_mass] > 1e6 ) & ( sdss[stellar_mass] < 1e14 ) & ((n.log10(sdss[stellar_mass+'_up_1sig']) - n.log10(sdss[stellar_mass+'_low_1sig']))/2. < 0.2 )
	mass_reliable_sdss_04 = (sdss[stellar_mass] > 1e6 ) & ( sdss[stellar_mass] < 1e14 ) & ((n.log10(sdss[stellar_mass+'_up_1sig']) - n.log10(sdss[stellar_mass+'_low_1sig']))/2. < 0.4 )
	ok_sdss_04 = (error_reliable_sdss) & (mass_reliable_sdss_04) & (redshift_reliable_sdss)&(sdss[ebv]>0)
	# defines ref quantity
	ebv_04_ref = sdss[ebv][ok_sdss_04]
	# quantity to compare to
	ebv_1 = imf_1+'spm_EBV'
	ebv_04_1 = sdss[ebv_1][ok_sdss_04]
	# quantity to compare to
	ebv_2 = imf_2+'spm_EBV'
	ebv_04_2 = sdss[ebv_2][ok_sdss_04]
	# normalized comparison ratio
	delta_m1 = (ebv_04_1-ebv_04_ref)
	delta_m2 = (ebv_04_2-ebv_04_ref)
	# figure
	p.figure(2, (4.5, 4.5))
	p.axes([0.12,0.18,0.8,0.73])
	p.hist(delta_m1, bins=m_bins, histtype='step', label=imf_1.split('_')[1]+"-"+imf_ref.split('_')[1] , normed=True, lw=2 )
	p.hist(delta_m2, bins=m_bins, histtype='step', label=imf_2.split('_')[1]+"-"+imf_ref.split('_')[1] , normed=True, lw=2 )
	#p.plot(m_bins, norm.pdf(m_bins, loc=0, scale=1), label='N(0,1)', ls='dashed')
	p.ylabel('normed distribution')
	p.xlabel(r'$E(B-V)-E(B-V)_{ref}$')
	p.title('SDSS '+imf_ref.split('_')[0])
	p.legend(loc=2, frameon = False, fontsize=11)
	p.xlim((-0.7, 0.7))
	p.grid()
	p.savefig(os.path.join(out_dir, "delta_EBV_distribution_sdss"+imf_ref.split('_')[0]+".png" ))
	p.clf()



plotDIFF_fixed_imf_sdss(	imf_ref = imfs[0], 	imf_1   = imfs[1], 	imf_2   = imfs[2])
plotDIFF_fixed_imf_sdss(	imf_ref = imfs[3], 	imf_1   = imfs[4], 	imf_2   = imfs[5])
plotDIFF_fixed_imf_sdss(	imf_ref = imfs[6], 	imf_1   = imfs[7], 	imf_2   = imfs[8])

def plotDIFF_fixed_imf(imf_ref, imf_1, imf_2):
	print('eboss')
	stellar_mass = imf_ref+'stellar_mass'
	ebv = imf_ref+'spm_EBV'
	# selections boo
	redshift_reliable_boss =  (boss['CLASS_NOQSO'] == "GALAXY") & ( boss['Z_ERR_NOQSO'] > 0.0) & (boss['ZWARNING_NOQSO'] == 0) & (boss['Z_NOQSO']>0.001) & (boss['Z_NOQSO'] > boss['Z_ERR_NOQSO'] ) # (boss['SN_MEDIAN_ALL'] > 0.1 ) & 
	error_reliable_boss = (boss[stellar_mass+'_up_1sig'] > boss[stellar_mass+'_low_1sig'] ) & (boss[stellar_mass+'_up_1sig'] > 0. ) & ( boss[stellar_mass+'_low_1sig'] > 0. ) & (boss[stellar_mass+'_up_1sig'] < 1e14 ) & ( boss[stellar_mass+'_low_1sig'] < 1e14 ) 
	mass_reliable_boss_04 = (boss[stellar_mass] > 1e6 ) & ( boss[stellar_mass] < 1e14 ) & ((n.log10(boss[stellar_mass+'_up_1sig']) - n.log10(boss[stellar_mass+'_low_1sig']))/2. < 0.4)
	ok_boss_04 = (error_reliable_boss) & (mass_reliable_boss_04) & (redshift_reliable_boss)&(boss[ebv]>0)
	# defines ref quantity
	ebv_04_ref = boss[ebv][ok_boss_04]
	# quantity to compare to
	ebv_1 = imf_1+'spm_EBV'
	ebv_04_1 = boss[ebv_1][ok_boss_04]
	# quantity to compare to
	ebv_2 = imf_2+'spm_EBV'
	ebv_04_2 = boss[ebv_2][ok_boss_04]
	# normalized comparison ratio
	delta_m1 = (ebv_04_1-ebv_04_ref)
	delta_m2 = (ebv_04_2-ebv_04_ref)
	# figure
	p.figure(2, (4.5, 4.5))
	p.axes([0.12,0.18,0.8,0.73])
	p.hist(delta_m1, bins=m_bins, histtype='step', label=imf_1.split('_')[1]+"-"+imf_ref.split('_')[1] , normed=True, lw=2 )
	p.hist(delta_m2, bins=m_bins, histtype='step', label=imf_2.split('_')[1]+"-"+imf_ref.split('_')[1] , normed=True, lw=2 )
	#p.plot(m_bins, norm.pdf(m_bins, loc=0, scale=1), label='N(0,1)', ls='dashed')
	p.ylabel('normed distribution')
	p.xlabel(r'$E(B-V)-E(B-V)_{ref}$')
	p.title('eBOSS '+imf_ref.split('_')[0])
	p.legend(loc=2, frameon = False, fontsize=11)
	p.xlim((-0.7, 0.7))
	p.grid()
	p.savefig(os.path.join(out_dir, "delta_EBV_distribution_eboss"+imf_ref.split('_')[0]+".png" ))
	p.clf()


def plotDIFF_fixed_lib(imf_ref, imf_1, imf_2):
	print('eboss')
	stellar_mass = imf_ref+'stellar_mass'
	ebv = imf_ref+'spm_EBV'
	# selections boo
	redshift_reliable_boss =  (boss['CLASS_NOQSO'] == "GALAXY") & ( boss['Z_ERR_NOQSO'] > 0.0) & (boss['ZWARNING_NOQSO'] == 0) & (boss['Z_NOQSO']>0.001) & (boss['Z_NOQSO'] > boss['Z_ERR_NOQSO'] ) # (boss['SN_MEDIAN_ALL'] > 0.1 ) & 
	error_reliable_boss = (boss[stellar_mass+'_up_1sig'] > boss[stellar_mass+'_low_1sig'] ) & (boss[stellar_mass+'_up_1sig'] > 0. ) & ( boss[stellar_mass+'_low_1sig'] > 0. ) & (boss[stellar_mass+'_up_1sig'] < 1e14 ) & ( boss[stellar_mass+'_low_1sig'] < 1e14 ) 	
	mass_reliable_boss_04 = (boss[stellar_mass] > 1e6 ) & ( boss[stellar_mass] < 1e14 ) & ((n.log10(boss[stellar_mass+'_up_1sig']) - n.log10(boss[stellar_mass+'_low_1sig']))/2. < 0.4)
	ok_boss_04 = (error_reliable_boss) & (mass_reliable_boss_04) & (redshift_reliable_boss)&(boss[ebv]>0)
	# defines ref quantity
	ebv_04_ref = boss[ebv][ok_boss_04]
	# quantity to compare to
	ebv_1 = imf_1+'spm_EBV'
	ebv_04_1 = boss[ebv_1][ok_boss_04]
	# quantity to compare to
	ebv_2 = imf_2+'spm_EBV'
	ebv_04_2 = boss[ebv_2][ok_boss_04]
	# normalized comparison ratio
	delta_m1 = (ebv_04_1-ebv_04_ref)
	delta_m2 = (ebv_04_2-ebv_04_ref)
	# figure
	p.figure(2, (4.5, 4.5))
	p.axes([0.12,0.18,0.8,0.73])
	p.hist(delta_m1, bins=m_bins, histtype='step', label=imf_1.split('_')[0]+"-"+imf_ref.split('_')[0] , normed=True, lw=2 )
	p.hist(delta_m2, bins=m_bins, histtype='step', label=imf_2.split('_')[0]+"-"+imf_ref.split('_')[0] , normed=True, lw=2 )
	#p.plot(m_bins, norm.pdf(m_bins, loc=0, scale=1), label='N(0,1)', ls='dashed')
	p.ylabel('normed distribution')
	p.xlabel(r'$E(B-V)-E(B-V)_{ref}$')
	p.title('eBOSS '+imf_ref.split('_')[1])
	p.legend(loc=2, frameon = False, fontsize=11)
	p.xlim((-0.7, 0.7))
	p.grid()
	p.savefig(os.path.join(out_dir, "delta_EBV_distribution_eboss"+imf_ref.split('_')[1]+".png" ))
	p.clf()


plotDIFF_fixed_imf(	imf_ref = imfs[0], 	imf_1   = imfs[1], 	imf_2   = imfs[2])
plotDIFF_fixed_imf(	imf_ref = imfs[3], 	imf_1   = imfs[4], 	imf_2   = imfs[5])
plotDIFF_fixed_imf(	imf_ref = imfs[6], 	imf_1   = imfs[7], 	imf_2   = imfs[8])

plotDIFF_fixed_lib(	imf_ref = imfs[0], 	imf_1   = imfs[3], 	imf_2   = imfs[6])
plotDIFF_fixed_lib(	imf_ref = imfs[1], 	imf_1   = imfs[4], 	imf_2   = imfs[7])
plotDIFF_fixed_lib(	imf_ref = imfs[2], 	imf_1   = imfs[5], 	imf_2   = imfs[8])
