from lib_spm import *

#out_dir = os.path.join('/data42s/comparat/firefly/v1_1_0/figures', 'mass-redshift-presentation')
#out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images')
out_dir = os.path.join(os.environ['HOME'], 'wwwDir', 'stuff')

imf1 = imfs[0]
imf2 = imfs[1]

imf = imf1

metal = imf+'metallicity_massW'
age = imf+'age_massW'
ebv = imf+'spm_EBV'
stellar_mass = imf+'stellar_mass'

A_ref = n.log10(boss[age])

redshift_reliable_boss =  (boss['CLASS_NOQSO'] == "GALAXY") & ( boss['Z_ERR_NOQSO'] > 0.0) & (boss['ZWARNING_NOQSO'] == 0) & (boss['Z_NOQSO']>0.001) & (boss['Z_NOQSO'] > boss['Z_ERR_NOQSO'] ) # (boss['SN_MEDIAN_ALL'] > 0.1 ) & 

error_reliable_boss = (boss[stellar_mass+'_up_1sig'] > boss[stellar_mass+'_low_1sig'] ) & (boss[stellar_mass+'_up_1sig'] > 0. ) & ( boss[stellar_mass+'_low_1sig'] > 0. ) & (boss[stellar_mass+'_up_1sig'] < 1e14 ) & ( boss[stellar_mass+'_low_1sig'] < 1e14 ) 
mass_reliable_boss_04 = (boss[stellar_mass] > 1e6 ) & ( boss[stellar_mass] < 1e14 ) & ((n.log10(boss[stellar_mass+'_up_1sig']) - n.log10(boss[stellar_mass+'_low_1sig']))/2. < 0.4 )


ok_boss_04 = (error_reliable_boss) & (mass_reliable_boss_04) & (redshift_reliable_boss) & (A_ref>9.8)&(A_ref<10.2)&(n.log10(boss[metal])<-1)

Z_1 = n.log10(boss[metal][ok_boss_04])
EBV_1 = boss[ebv][ok_boss_04]

imf = imf2
metal = imf+'metallicity_massW'
ebv = imf+'spm_EBV'
Z_2 = n.log10(boss[metal][ok_boss_04])
EBV_2 = boss[ebv][ok_boss_04]


p.figure(0, (5.5, 4.5))
p.axes([0.2,0.2,0.7,0.7])
p.plot(abs(Z_2-Z_1), abs(EBV_2-EBV_1), 'k,', alpha=0.2)
#p.xlim((-2.2,0.5))
#p.ylim((7.3,10.5))
p.ylabel(r'$|\Delta E(B-V)|$')
p.xlabel(r'$|\Delta \log_{10}(Z/Z_\odot)|$')
#p.colorbar(shrink=0.7, label=r'$\log_{10}(N \times w_M)$')
#p.legend(loc=0, frameon = False)
p.grid()
p.title('M11-MILES - M11-ELODIE')
#p.text(-2.1, 7.5,'eBOSS '+imf.split('_')[1]+' '+str(ii) )
p.tight_layout()
p.savefig(os.path.join(out_dir, "metallicity_EBV_eboss_04.png" ))
p.clf()
#