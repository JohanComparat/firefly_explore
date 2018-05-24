from lib_spm import *

#out_dir = os.path.join('/data42s/comparat/firefly/v1_1_0/figures', 'mass-redshift-presentation')
out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images', 'mass-redshift-presentation')

imf = imfs[0]
stellar_mass = imf+'stellar_mass'

redshift_reliable_boss =  (boss['CLASS_NOQSO'] == "GALAXY") & ( boss['Z_ERR_NOQSO'] > 0.0) & (boss['ZWARNING_NOQSO'] == 0) & (boss['Z_NOQSO']>0.001) & (boss['Z_NOQSO'] > boss['Z_ERR_NOQSO'] ) # (boss['SN_MEDIAN_ALL'] > 0.1 ) & 
redshift_reliable_sdss =  (sdss['CLASS'] == "GALAXY")       & ( sdss['Z_ERR'] > 0.0)       & (sdss['ZWARNING'] == 0)       & (sdss['Z'] > 0.001) & (sdss['Z'] > sdss['Z_ERR'] ) # (sdss['SN_MEDIAN_ALL'] > 0.1 ) &

error_reliable_boss = (boss[stellar_mass+'_up_1sig'] > boss[stellar_mass+'_low_1sig'] ) & (boss[stellar_mass+'_up_1sig'] > 0. ) & ( boss[stellar_mass+'_low_1sig'] > 0. ) & (boss[stellar_mass+'_up_1sig'] < 1e14 ) & ( boss[stellar_mass+'_low_1sig'] < 1e14 ) 
error_reliable_sdss = (sdss[stellar_mass+'_up_1sig'] > sdss[stellar_mass+'_low_1sig'] ) & (sdss[stellar_mass+'_up_1sig'] > 0. ) & ( sdss[stellar_mass+'_low_1sig'] > 0. ) & (sdss[stellar_mass+'_up_1sig'] < 1e14 ) & ( sdss[stellar_mass+'_low_1sig'] < 1e14 ) 

mass_reliable_boss_02 = (boss[stellar_mass] > 1e6 ) & ( boss[stellar_mass] < 1e14 ) & ((n.log10(boss[stellar_mass+'_up_1sig']) - n.log10(boss[stellar_mass+'_low_1sig']))/2. < 0.2 )
mass_reliable_sdss_02 = (sdss[stellar_mass] > 1e6 ) & ( sdss[stellar_mass] < 1e14 ) & ((n.log10(sdss[stellar_mass+'_up_1sig']) - n.log10(sdss[stellar_mass+'_low_1sig']))/2. < 0.2 )
mass_reliable_boss_04 = (boss[stellar_mass] > 1e6 ) & ( boss[stellar_mass] < 1e14 ) & ((n.log10(boss[stellar_mass+'_up_1sig']) - n.log10(boss[stellar_mass+'_low_1sig']))/2. < 0.4 )
mass_reliable_sdss_04 = (sdss[stellar_mass] > 1e6 ) & ( sdss[stellar_mass] < 1e14 ) & ((n.log10(sdss[stellar_mass+'_up_1sig']) - n.log10(sdss[stellar_mass+'_low_1sig']))/2. < 0.4 )

ok_boss_02 = (error_reliable_boss) & (mass_reliable_boss_02) & (redshift_reliable_boss)
ok_sdss_02 = (error_reliable_sdss) & (mass_reliable_sdss_02) & (redshift_reliable_sdss)
ok_boss_04 = (error_reliable_boss) & (mass_reliable_boss_04) & (redshift_reliable_boss)
ok_sdss_04 = (error_reliable_sdss) & (mass_reliable_sdss_04) & (redshift_reliable_sdss)
print( "boss 02",len(ok_boss_02.nonzero()[0]))
print( "sdss 02",len(ok_sdss_02.nonzero()[0]))
print( "boss 04",len(ok_boss_04.nonzero()[0]))
print( "sdss 04",len(ok_sdss_04.nonzero()[0]))

zz_02 = n.hstack(( boss['Z_NOQSO'][ok_boss_02], sdss['Z'][ok_sdss_02]))
Ms_02 = n.hstack(( n.log10(boss[stellar_mass][ok_boss_02]), n.log10(sdss[stellar_mass][ok_sdss_02]) ))
zz_02_boss = boss['Z_NOQSO'][ok_boss_02]
zz_02_sdss = sdss['Z'][ok_sdss_02]

zz_04 = n.hstack(( boss['Z_NOQSO'][ok_boss_04], sdss['Z'][ok_sdss_04]))
Ms_04 = n.hstack(( n.log10(boss[stellar_mass][ok_boss_04]), n.log10(sdss[stellar_mass][ok_sdss_04]) ))
zz_04_boss = boss['Z_NOQSO'][ok_boss_04]
zz_04_sdss = sdss['Z'][ok_sdss_04]

z_bins = n.arange(0,1.5,0.05)
m_bins = n.arange(6.5, 13, 0.2)
XX, YY = n.meshgrid(z_bins[:-1]+0.05/2., m_bins[:-1]+0.2/2.)

p.figure(0, (5.5, 4.5))
p.axes([0.2,0.2,0.7,0.7])
HH = n.histogram2d(zz_02, Ms_02, bins=[z_bins, m_bins])[0].T
p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' )
p.ylabel(r"$\log_{10}$ (stellar mass / $M_\odot$ )")
#p.axvline(n.log10(3.), ls='dashed', label='z=0.1, 0.5, 1, 2')
#p.axvline(n.log10(2.), ls='dashed')#, label='z=1')
#p.axvline(n.log10(1.1),ls='dashed')#, label='z=0.1')
#p.axvline(n.log10(1.5),ls='dashed')#, label='z=0.5')
p.xlabel('redshift')
#p.xlabel(r'$\log_{10}(1+z)$')
#p.xscale('log')
p.colorbar(shrink=0.7, label=r'$\log_{10}(N)$')
p.legend(loc=0, frameon = False)
p.xlim((-0.05, 1.4))
p.ylim((6.5, 12.5))
p.grid()
p.title('SDSS and eBOSS '+r'$\sigma_M < 0.2$')
p.savefig(os.path.join(out_dir, "mass_redshift_mass_"+imf+"sdss_boss_02.png" ))
p.clf()

#p.figure(1, (4.5, 4.5))
#p.axes([0.2,0.2,0.7,0.7])
##p.plot(zz_04, Ms_04, 'r,', rasterized=True, alpha=0.5, label=r' $\sigma_M < 0.4$')
#p.plot(zz_02, Ms_02, 'k,', rasterized=True, alpha=0.5, label=r' $\sigma_M < 0.2$')
#p.ylabel(r"$\log_{10}$ (stellar mass / $M_\odot$ )")
##p.axvline(n.log10(3.), ls='dashed', label='z=0.1, 0.5, 1, 2')
##p.axvline(n.log10(2.), ls='dashed')#, label='z=1')
##p.axvline(n.log10(1.1),ls='dashed')#, label='z=0.1')
##p.axvline(n.log10(1.5),ls='dashed')#, label='z=0.5')
#p.xlabel('redshift')
##p.xlabel(r'$\log_{10}(1+z)$')
##p.xscale('log')
#p.legend(loc=0, frameon = False)
#p.xlim((0.0, 1.4))
#p.ylim((6.5, 12.5))
#p.grid()
#p.title('SDSS and eBOSS')
#p.savefig(os.path.join(out_dir, "mass_redshift_mass_"+imf+"sdss_boss_02.png" ))
#p.clf()


p.figure(1, (4.5, 4.5))
p.axes([0.2,0.2,0.7,0.7])
HH = n.histogram2d(zz_04, Ms_04, bins=[z_bins, m_bins])[0].T
p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' )
#p.plot(zz_04, Ms_04, 'k,', rasterized=True, alpha=0.5, label=r' $\sigma_M < 0.4$')
#p.plot(zz_02, Ms_02, 'k,', rasterized=True, alpha=0.5, label=r' $\sigma_M < 0.2$')
p.ylabel(r"$\log_{10}$ (stellar mass / $M_\odot$ )")
#p.axvline(n.log10(3.), ls='dashed', label='z=0.1, 0.5, 1, 2')
#p.axvline(n.log10(2.), ls='dashed')#, label='z=1')
#p.axvline(n.log10(1.1),ls='dashed')#, label='z=0.1')
#p.axvline(n.log10(1.5),ls='dashed')#, label='z=0.5')
p.xlabel('redshift')
#p.xlabel(r'$\log_{10}(1+z)$')
#p.xscale('log')
p.legend(loc=0, frameon = False)
p.xlim((0.0, 1.4))
p.ylim((6.5, 12.5))
p.grid()
p.title('SDSS and eBOSS '+r'$\sigma_M < 0.4$')
p.savefig(os.path.join(out_dir, "mass_redshift_mass_"+imf+"sdss_boss_04.png" ))
p.clf()

z_flg = 'ZQUALITY'
z_name = 'ZBEST'
deep2_zOk = (deep2[z_name] > 0.001) & (deep2[z_flg]>=2.) & (deep2[z_name] < 1.7) & (deep2['SSR']>0) & (deep2['TSR']>0) & (deep2['SSR']<=1.0001) & (deep2['TSR']<=1.0001)
deep2_sel_02 = (deep2_zOk) & (deep2[stellar_mass] < 10**14. ) & (deep2[stellar_mass] > 0. )  & (deep2[stellar_mass] >= deep2[stellar_mass+'_low_1sig'] ) & (deep2[stellar_mass] <= deep2[stellar_mass+'_up_1sig'] ) & ( - n.log10(deep2[stellar_mass+'_low_1sig'])  + n.log10(deep2[stellar_mass+'_up_1sig']) < 0.4 )
deep2_sel_04 = (deep2_zOk) & (deep2[stellar_mass] < 10**14. ) & (deep2[stellar_mass] > 0. )  & (deep2[stellar_mass] >= deep2[stellar_mass+'_low_1sig'] ) & (deep2[stellar_mass] <= deep2[stellar_mass+'_up_1sig'] ) & ( - n.log10(deep2[stellar_mass+'_low_1sig'])  + n.log10(deep2[stellar_mass+'_up_1sig']) < 0.8 )

Ms_02 = n.log10(deep2[stellar_mass][deep2_sel_02])
zz_02 = deep2[z_name][deep2_sel_02]
Ms_04 = n.log10(deep2[stellar_mass][deep2_sel_04])
zz_04 = deep2[z_name][deep2_sel_04]

w_deep2 = 1. / (deep2['TSR'] * deep2['SSR'])

print( "deep2 02",len(deep2_sel_02.nonzero()[0]))
print( "deep2 04",len(deep2_sel_04.nonzero()[0]))

p.figure(1, (4.5, 4.5))
p.axes([0.2,0.2,0.7,0.7])

HH = n.histogram2d(zz_02, Ms_02, bins=[z_bins, m_bins])[0].T
p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' )
#p.plot(zz_04, Ms_04, 'r+', rasterized=True, label=r' $\sigma_M < 0.4$', alpha=0.5)
#p.plot(zz_02, Ms_02, 'k+', rasterized=True, label=r' $\sigma_M < 0.2$', alpha=0.5)
p.ylabel(r"$\log_{10}$ (stellar mass / $M_\odot$ )")
#p.axvline(n.log10(3.), ls='dashed', label='z=0.1, 0.5, 1, 2')
#p.axvline(n.log10(2.), ls='dashed')#, label='z=1')
#p.axvline(n.log10(1.1),ls='dashed')#, label='z=0.1')
#p.axvline(n.log10(1.5),ls='dashed')#, label='z=0.5')
p.xlabel('redshift')
#p.xlabel(r'$\log_{10}(1+z)$')
#p.xscale('log')
p.legend(loc=0, frameon = False)
p.xlim((0.0, 1.4))
p.ylim((6.5, 12.5))
p.grid()
p.title('DEEP2 '+r'$\sigma_M < 0.2$')
p.savefig(os.path.join(out_dir, "mass_redshift_mass_"+imf+"deep2_02.png" ))
p.clf()


p.figure(1, (4.5, 4.5))
p.axes([0.2,0.2,0.7,0.7])
HH = n.histogram2d(zz_04, Ms_04, bins=[z_bins, m_bins])[0].T
p.scatter(XX[HH>10], YY[HH>10], c=n.log10(HH[HH>10]), s=40, edgecolors='none', marker='s' )
#p.plot(zz_04, Ms_04, 'k+', rasterized=True, label=r' $\sigma_M < 0.4$', alpha=0.5)
#p.plot(zz_02, Ms_02, 'kx', rasterized=True, label=r' $\sigma_M < 0.2$', alpha=0.5)
p.ylabel(r"$\log_{10}$ (stellar mass / $M_\odot$ )")
#p.axvline(n.log10(3.), ls='dashed', label='z=0.1, 0.5, 1, 2')
#p.axvline(n.log10(2.), ls='dashed')#, label='z=1')
#p.axvline(n.log10(1.1),ls='dashed')#, label='z=0.1')
#p.axvline(n.log10(1.5),ls='dashed')#, label='z=0.5')
p.xlabel('redshift')
#p.xlabel(r'$\log_{10}(1+z)$')
#p.xscale('log')
p.legend(loc=0, frameon = False)
p.xlim((0.0, 1.4))
p.ylim((6.5, 12.5))
p.grid()
p.title('DEEP2 '+r'$\sigma_M < 0.4$')
p.savefig(os.path.join(out_dir, "mass_redshift_mass_"+imf+"deep2_04.png" ))
p.clf()

z_bins = n.arange(0.,1.4,0.05)
p.figure(2, (6.5, 3.5))
p.axes([0.12,0.18,0.8,0.73])
p.hist(zz_02_boss, bins = z_bins, histtype='step', label=r'eBOSS', ls='solid', color='r')
p.hist(zz_04_boss, bins = z_bins, histtype='step', ls='dashed', color='r')
p.hist(zz_02_sdss, bins = z_bins, histtype='step', label='SDSS', ls='solid', color='k')
p.hist(zz_04_sdss, bins = z_bins, histtype='step', ls='dashed', color='k')
p.hist(zz_02     , bins = z_bins, histtype='step', label='DEEP2', ls='solid', color='b')
p.hist(zz_04     , bins = z_bins, histtype='step', ls='dashed', color='b')
p.ylabel(r"N(dz=0.05)")
p.xlabel('redshift')
p.yscale('log')
p.legend(loc=0, frameon = False)
p.xlim((0.0, 1.4))
#p.ylim((1, 12.5))
p.grid()
p.savefig(os.path.join(out_dir, "redshift_distribution.png" ))
p.clf()




















sys.exit()

out_dir = os.path.join(os.environ['OBS_REPO'], 'spm', 'results', 'mass-redshift-presentation', 'per-PROGRAMNAME')

def plot_all_prognames(hdu , imf, prefix, out_dir , redshift_reliable, merr=0.2 ) :
	stellar_mass = imf+'_stellar_mass'
	#mass_reliable = (hdu[stellar_mass] > 0 ) & ( hdu[stellar_mass] < 1e13. ) & ( abs(hdu[stellar_mass + '_up_1sig'] - hdu[stellar_mass]) < 0.4 ) & ( abs(hdu[stellar_mass + '_low_1sig'] - hdu[stellar_mass]) < 0.4 )
	mass_reliable = (hdu[stellar_mass] > 1e6 ) & ( hdu[stellar_mass] < 1e14 ) & ((n.log10(hdu[stellar_mass+'_up_1sig']) - n.log10(hdu[stellar_mass+'_low_1sig']))/2. < merr )
	#good_plates = (hdu['PLATEQUALITY']=='good') &(hdu['TARGETTYPE']=='science')
	all_names = set(hdu['PROGRAMNAME'])
	all_names_arr = n.array(list(all_names))
	for ii in range(len(all_names_arr)):
		selection = (mass_reliable) & (redshift_reliable) & (hdu['PROGRAMNAME']==all_names_arr[ii])
		N_occ = len(selection.nonzero()[0])
		print( all_names_arr[ii], N_occ)
		if N_occ>1:
			p.figure(1, (4.5, 4.5))
			p.axes([0.2,0.2,0.7,0.7])
			p.plot(n.log10(1.+hdu['Z'][selection]), n.log10(hdu[stellar_mass][selection]), 'k+', rasterized=True, alpha=0.5) #, label=all_names_arr[ii]
			p.ylabel(r'$\log_{10}$ (stellar mass '+imf+r" / $M_\odot$ )")
			p.axvline(n.log10(3.), ls='dashed', label='z=0.1, 0.5, 1, 2')
			p.axvline(n.log10(2.), ls='dashed')#, label='z=1')
			p.axvline(n.log10(1.1),ls='dashed')#, label='z=0.1')
			p.axvline(n.log10(1.5),ls='dashed')#, label='z=0.5')
			p.xlabel(r'$\log_{10}(1+z)$')
			#p.xscale('log')
			p.legend(loc=0, frameon = False)
			p.xlim((0.0, 0.7))
			p.ylim((6.5, 12.5))
			p.grid()
			p.title('N='+str(N_occ))
			p.savefig(os.path.join(out_dir, prefix+"_"+all_names_arr[ii]+"_redshift_mass_"+imf+".png" ))
			p.clf()
			p.figure(2, (4.5, 4.5))
			p.axes([0.2,0.2,0.7,0.7])
			#p.subplot(111, projection="mollweide")
			#p.plot((hdu['PLUG_RA'][selection]-180.)*n.pi/180., hdu['PLUG_DEC'][selection]*n.pi/180., 'k+', rasterized=True) # , label=all_names_arr[ii]
			p.plot(hdu['PLUG_RA'][selection], hdu['PLUG_DEC'][selection], 'k+', rasterized=True) # , label=all_names_arr[ii]
			p.title(all_names_arr[ii])#+', Ngal='+str(N_occ))
			p.xlim((0.0, 360.))
			p.ylim((-20., 85.))
			p.xlabel(r'ra [deg]')
			p.ylabel(r'dec [deg]')
			#p.legend(loc=0, frameon = False)
			p.grid()
			p.savefig(os.path.join(out_dir, prefix+"_"+all_names_arr[ii]+"_ra_dec_"+imf+".png" ))
			p.clf()


print('-----------------------------------------')
prefix = 'BOSS'
print(prefix)
hdus = boss
redshift_reliable = (boss['SNR_ALL'] > 0.1 ) & (boss['CLASS_NOQSO'] == "GALAXY") & (boss['Z'] >= 0) & ( boss['Z_ERR_NOQSO'] >= 0) & (boss['ZWARNING_NOQSO'] == 0) & (boss['Z_NOQSO'] > boss['Z_ERR_NOQSO'] )
plot_all_prognames(hdu=hdus, imf=imf[:-1], prefix=prefix, out_dir = out_dir, redshift_reliable=redshift_reliable, merr=0.4 )
"""
imf = 'Salpeter'
plot_all_prognames(hdus=hdus, imf=imf, prefix=prefix,  redshift_reliable=redshift_reliable )

imf = 'Kroupa'
plot_all_prognames(hdus=hdus, imf=imf, prefix=prefix, redshift_reliable=redshift_reliable )
"""
print('-----------------------------------------')
prefix = 'SDSS'
print(prefix)
hdus = sdss
redshift_reliable = (sdss['SNR_ALL'] > 0.1 ) & (sdss['CLASS'] == "GALAXY") & (sdss['Z'] >= 0) & ( sdss['Z_ERR'] >= 0) & (sdss['ZWARNING'] == 0) & (sdss['Z'] > sdss['Z_ERR'] )
plot_all_prognames(hdu=hdus, imf=imf[:-1], prefix=prefix, out_dir = out_dir, redshift_reliable=redshift_reliable, merr=0.4 )
"""
imf = 'Salpeter'
plot_all_prognames(hdus=hdus, imf=imf, prefix=prefix, redshift_reliable=redshift_reliable )

imf = 'Kroupa'
plot_all_prognames(hdus=hdus, imf=imf, prefix=prefix, redshift_reliable=redshift_reliable )
"""



