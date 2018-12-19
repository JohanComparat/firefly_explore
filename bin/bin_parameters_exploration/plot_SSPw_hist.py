from lib_spm import *

#out_dir = os.path.join('/data42s/comparat/firefly/v1_1_0/figures', 'mass-redshift-presentation')
out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images/sspW')
#out_dir = os.path.join(os.environ['HOME'],'wwwDir', 'stuff')

s_bins = 10**n.arange(-4, 0.1, 0.05)
m_bins = 10**n.arange(6.5, 12.5, 0.25)

for imf in imfs:
	print('deep2')
	p.figure(1, (4.5, 4.5))
	p.axes([0.12,0.18,0.8,0.73])
	for ii in range(3):
		stellar_mass = imf+'stellar_mass'
		ssp = imf+'weightMass_ssp_'+str(ii)
		ssp_mass = imf+'stellar_mass_ssp_'+str(ii)
		z_flg = 'ZQUALITY'
		z_name = 'ZBEST'
		deep2_zOk = (deep2[z_name] > 0.6) & (deep2[z_flg]>=2.) & (deep2[z_name] < 1.2) & (deep2['SSR']>0) & (deep2['TSR']>0) & (deep2['SSR']<=1.0001) & (deep2['TSR']<=1.0001)
		ok_deep2_04 = (deep2_zOk) & (deep2[stellar_mass] < 10**14. ) & (deep2[stellar_mass] > 0. )  & (deep2[stellar_mass] >= deep2[stellar_mass+'_low_1sig'] ) & (deep2[stellar_mass] <= deep2[stellar_mass+'_up_1sig'] ) & ( - n.log10(deep2[stellar_mass+'_low_1sig'])  + n.log10(deep2[stellar_mass+'_up_1sig']) < 0.4 )
		ok_deep2_04 = (deep2_zOk) & (deep2[stellar_mass] < 10**14. ) & (deep2[stellar_mass] > 0. )  & (deep2[stellar_mass] >= deep2[stellar_mass+'_low_1sig'] ) & (deep2[stellar_mass] <= deep2[stellar_mass+'_up_1sig'] ) & ( - n.log10(deep2[stellar_mass+'_low_1sig'])  + n.log10(deep2[stellar_mass+'_up_1sig']) < 0.8 )
		ssps = deep2[ssp][ok_deep2_04]*deep2[ssp_mass][ok_deep2_04]
		if len(ssps[ssps>=0.0001])>0:
			p.hist(ssps, bins = m_bins, histtype='step', label=str(ii+1) )# , cumulative=True, normed=True )
	p.ylabel('counts')
	p.xlabel(r'SSP stellar mass $M_\odot$')
	p.yscale('log')
	p.xscale('log')
	p.title('DEEP2')
	p.legend(loc=0, frameon = False)
	#p.xlim((1e-4,1))
	p.grid()
	p.savefig(os.path.join(out_dir, imf+"ssp_stellar_mass_distribution_deep2.png" ))
	p.clf()
	
	p.figure(1, (4.5, 4.5))
	p.axes([0.12,0.18,0.8,0.73])
	for ii in range(3):
		stellar_mass = imf+'stellar_mass'
		ssp = imf+'weightMass_ssp_'+str(ii)
		ssp_mass = imf+'stellar_mass_ssp_'+str(ii)
		z_flg = 'ZQUALITY'
		z_name = 'ZBEST'
		deep2_zOk = (deep2[z_name] > 0.6) & (deep2[z_flg]>=2.) & (deep2[z_name] < 1.2) & (deep2['SSR']>0) & (deep2['TSR']>0) & (deep2['SSR']<=1.0001) & (deep2['TSR']<=1.0001)
		ok_deep2_04 = (deep2_zOk) & (deep2[stellar_mass] < 10**14. ) & (deep2[stellar_mass] > 0. )  & (deep2[stellar_mass] >= deep2[stellar_mass+'_low_1sig'] ) & (deep2[stellar_mass] <= deep2[stellar_mass+'_up_1sig'] ) & ( - n.log10(deep2[stellar_mass+'_low_1sig'])  + n.log10(deep2[stellar_mass+'_up_1sig']) < 0.4 )
		ok_deep2_04 = (deep2_zOk) & (deep2[stellar_mass] < 10**14. ) & (deep2[stellar_mass] > 0. )  & (deep2[stellar_mass] >= deep2[stellar_mass+'_low_1sig'] ) & (deep2[stellar_mass] <= deep2[stellar_mass+'_up_1sig'] ) & ( - n.log10(deep2[stellar_mass+'_low_1sig'])  + n.log10(deep2[stellar_mass+'_up_1sig']) < 0.8 )
		ssps = deep2[ssp][ok_deep2_04]
		if len(ssps[ssps>=0.0001])>0:
			p.hist(ssps, bins = s_bins, histtype='step', label=str(ii+1) )# , cumulative=True, normed=True )
	p.ylabel('counts')
	p.xlabel(r'SSP stellar mass $M_\odot$')
	p.yscale('log')
	p.xscale('log')
	p.title('DEEP2')
	p.legend(loc=0, frameon = False)
	#p.xlim((1e-4,1))
	p.grid()
	p.savefig(os.path.join(out_dir, imf+"ssp_massW_distribution_deep2.png" ))
	p.clf()
	
	p.figure(1, (4.5, 4.5))
	p.axes([0.18,0.18,0.75,0.75])
	print('sdss SMF', imf)
	for ii in range(7):
		stellar_mass = imf+'stellar_mass'
		ssp = imf+'weightMass_ssp_'+str(ii)
		ssp_mass = imf+'stellar_mass_ssp_'+str(ii)
		redshift_reliable_sdss =  (sdss['CLASS'] == "GALAXY")       & ( sdss['Z_ERR'] > 0.0)       & (sdss['ZWARNING'] == 0)       & (sdss['Z'] > 0.001) & (sdss['Z'] > sdss['Z_ERR'] ) # (sdss['SN_MEDIAN_ALL'] > 0.1 ) &
		error_reliable_sdss = (sdss[stellar_mass+'_up_1sig'] > sdss[stellar_mass+'_low_1sig'] ) & (sdss[stellar_mass+'_up_1sig'] > 0. ) & ( sdss[stellar_mass+'_low_1sig'] > 0. ) & (sdss[stellar_mass+'_up_1sig'] < 1e14 ) & ( sdss[stellar_mass+'_low_1sig'] < 1e14 ) 
		mass_reliable_sdss_02 = (sdss[stellar_mass] > 1e6 ) & ( sdss[stellar_mass] < 1e14 ) & ((n.log10(sdss[stellar_mass+'_up_1sig']) - n.log10(sdss[stellar_mass+'_low_1sig']))/2. < 0.2 )
		mass_reliable_sdss_04 = (sdss[stellar_mass] > 1e6 ) & ( sdss[stellar_mass] < 1e14 ) & ((n.log10(sdss[stellar_mass+'_up_1sig']) - n.log10(sdss[stellar_mass+'_low_1sig']))/2. < 0.4 )
		ok_sdss_02 = (error_reliable_sdss) & (mass_reliable_sdss_02) & (redshift_reliable_sdss)
		ok_sdss_04 = (error_reliable_sdss) & (mass_reliable_sdss_04) & (redshift_reliable_sdss)
		ssps = sdss[ssp][ok_sdss_04]*sdss[ssp_mass][ok_sdss_04]
		if len(ssps[ssps>0])>0:
			p.hist(ssps, bins = m_bins, histtype='step', label=str(ii+1) )# , cumulative=True, normed=True )
	#p.ylabel('normed cumulative distribution')
	p.ylabel('counts')
	p.xlabel(r'SSP stellar mass $M_\odot$')
	p.yscale('log')
	p.xscale('log')
	p.title('SDSS')
	p.legend(loc=0, frameon = False)
	#p.xlim((1e-4,1))
	p.grid()
	p.savefig(os.path.join(out_dir, imf+"ssp_stellar_mass_distribution_sdss.png" ))
	p.clf()
	
	p.figure(1, (4.5, 4.5))
	p.axes([0.18,0.18,0.75,0.75])
	print('sdss ssp', imf)
	for ii in range(7):
		stellar_mass = imf+'stellar_mass'
		ssp = imf+'weightMass_ssp_'+str(ii)
		redshift_reliable_sdss =  (sdss['CLASS'] == "GALAXY")       & ( sdss['Z_ERR'] > 0.0)       & (sdss['ZWARNING'] == 0)       & (sdss['Z'] > 0.001) & (sdss['Z'] > sdss['Z_ERR'] ) # (sdss['SN_MEDIAN_ALL'] > 0.1 ) &
		error_reliable_sdss = (sdss[stellar_mass+'_up_1sig'] > sdss[stellar_mass+'_low_1sig'] ) & (sdss[stellar_mass+'_up_1sig'] > 0. ) & ( sdss[stellar_mass+'_low_1sig'] > 0. ) & (sdss[stellar_mass+'_up_1sig'] < 1e14 ) & ( sdss[stellar_mass+'_low_1sig'] < 1e14 ) 
		mass_reliable_sdss_02 = (sdss[stellar_mass] > 1e6 ) & ( sdss[stellar_mass] < 1e14 ) & ((n.log10(sdss[stellar_mass+'_up_1sig']) - n.log10(sdss[stellar_mass+'_low_1sig']))/2. < 0.2 )
		mass_reliable_sdss_04 = (sdss[stellar_mass] > 1e6 ) & ( sdss[stellar_mass] < 1e14 ) & ((n.log10(sdss[stellar_mass+'_up_1sig']) - n.log10(sdss[stellar_mass+'_low_1sig']))/2. < 0.4 )
		ok_sdss_02 = (error_reliable_sdss) & (mass_reliable_sdss_02) & (redshift_reliable_sdss)
		ok_sdss_04 = (error_reliable_sdss) & (mass_reliable_sdss_04) & (redshift_reliable_sdss)
		ssps = sdss[ssp][ok_sdss_04]
		if len(ssps[ssps>0])>0:
			p.hist(ssps, bins = s_bins, histtype='step', label=str(ii+1) )# , cumulative=True, normed=True )
	#p.ylabel('normed cumulative distribution')
	p.ylabel('counts')
	p.xlabel('SSP mass weight')
	p.yscale('log')
	p.xscale('log')
	p.title('SDSS')
	p.legend(loc=2, frameon = False, fontsize=11)
	p.xlim((1e-4,1))
	p.grid()
	p.savefig(os.path.join(out_dir, imf+"ssp_massW_distribution_sdss.png" ))
	p.clf()
	
	p.figure(1, (4.5, 4.5))
	p.axes([0.18,0.18,0.75,0.75])
	print('eboss SMF', imf)
	for ii in range(7):
		stellar_mass = imf+'stellar_mass'
		ssp = imf+'weightMass_ssp_'+str(ii)
		ssp_mass = imf+'stellar_mass_ssp_'+str(ii)
		redshift_reliable_boss =  (boss['CLASS_NOQSO'] == "GALAXY") & ( boss['Z_ERR_NOQSO'] > 0.0) & (boss['ZWARNING_NOQSO'] == 0) & (boss['Z_NOQSO']>0.001) & (boss['Z_NOQSO'] > boss['Z_ERR_NOQSO'] ) # (boss['SN_MEDIAN_ALL'] > 0.1 ) & 
		error_reliable_boss = (boss[stellar_mass+'_up_1sig'] > boss[stellar_mass+'_low_1sig'] ) & (boss[stellar_mass+'_up_1sig'] > 0. ) & ( boss[stellar_mass+'_low_1sig'] > 0. ) & (boss[stellar_mass+'_up_1sig'] < 1e14 ) & ( boss[stellar_mass+'_low_1sig'] < 1e14 ) 
		mass_reliable_boss_02 = (boss[stellar_mass] > 1e6 ) & ( boss[stellar_mass] < 1e14 ) & ((n.log10(boss[stellar_mass+'_up_1sig']) - n.log10(boss[stellar_mass+'_low_1sig']))/2. < 0.2 )
		mass_reliable_boss_04 = (boss[stellar_mass] > 1e6 ) & ( boss[stellar_mass] < 1e14 ) & ((n.log10(boss[stellar_mass+'_up_1sig']) - n.log10(boss[stellar_mass+'_low_1sig']))/2. < 0.4)
		ok_boss_02 = (error_reliable_boss) & (mass_reliable_boss_02) & (redshift_reliable_boss)
		ok_boss_04 = (error_reliable_boss) & (mass_reliable_boss_04) & (redshift_reliable_boss)
		#Ms_02_boss = n.log10(boss[stellar_mass][ok_boss_02])
		ssps = boss[ssp][ok_boss_04]*boss[ssp_mass][ok_boss_04]
		if len(ssps[ssps>0])>0:
			p.hist(ssps, bins = m_bins, histtype='step', label=str(ii+1) )# , cumulative=True, normed=True )
	#p.ylabel('normed cumulative distribution')
	p.ylabel('counts')
	p.xlabel(r'SSP stellar mass $M_\odot$')
	p.yscale('log')
	p.xscale('log')
	p.title('eBOSS')
	p.legend(loc=2, frameon = False, fontsize=11)
	#p.xlim((1e-4,1))
	p.grid()
	p.savefig(os.path.join(out_dir, imf+"ssp_stellar_mass_distribution_eboss.png" ))
	p.clf()
	
	p.figure(1, (4.5, 4.5))
	p.axes([0.18,0.18,0.75,0.75])
	print('eboss ssp', imf)
	for ii in range(7):
		stellar_mass = imf+'stellar_mass'
		ssp = imf+'weightMass_ssp_'+str(ii)
		redshift_reliable_boss =  (boss['CLASS_NOQSO'] == "GALAXY") & ( boss['Z_ERR_NOQSO'] > 0.0) & (boss['ZWARNING_NOQSO'] == 0) & (boss['Z_NOQSO']>0.001) & (boss['Z_NOQSO'] > boss['Z_ERR_NOQSO'] ) # (boss['SN_MEDIAN_ALL'] > 0.1 ) & 
		error_reliable_boss = (boss[stellar_mass+'_up_1sig'] > boss[stellar_mass+'_low_1sig'] ) & (boss[stellar_mass+'_up_1sig'] > 0. ) & ( boss[stellar_mass+'_low_1sig'] > 0. ) & (boss[stellar_mass+'_up_1sig'] < 1e14 ) & ( boss[stellar_mass+'_low_1sig'] < 1e14 ) 
		mass_reliable_boss_02 = (boss[stellar_mass] > 1e6 ) & ( boss[stellar_mass] < 1e14 ) & ((n.log10(boss[stellar_mass+'_up_1sig']) - n.log10(boss[stellar_mass+'_low_1sig']))/2. < 0.2 )
		mass_reliable_boss_04 = (boss[stellar_mass] > 1e6 ) & ( boss[stellar_mass] < 1e14 ) & ((n.log10(boss[stellar_mass+'_up_1sig']) - n.log10(boss[stellar_mass+'_low_1sig']))/2. < 0.4)
		ok_boss_02 = (error_reliable_boss) & (mass_reliable_boss_02) & (redshift_reliable_boss)
		ok_boss_04 = (error_reliable_boss) & (mass_reliable_boss_04) & (redshift_reliable_boss)
		#Ms_02_boss = n.log10(boss[stellar_mass][ok_boss_02])
		ssps = boss[ssp][ok_boss_04]
		if len(ssps[ssps>0])>0:
			p.hist(ssps, bins = s_bins, histtype='step', label=str(ii+1) )# , cumulative=True, normed=True )
	#p.ylabel('normed cumulative distribution')
	p.ylabel('counts')
	p.xlabel('SSP mass weight')
	p.yscale('log')
	p.xscale('log')
	p.title('eBOSS')
	p.legend(loc=2, frameon = False, fontsize=11)
	p.xlim((1e-4,1))
	p.grid()
	p.savefig(os.path.join(out_dir, imf+"ssp_massW_distribution_eboss.png" ))
	p.clf()







