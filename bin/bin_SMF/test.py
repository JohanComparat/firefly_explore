from lib_spm import *
#imfs = ["Chabrier_ELODIE_", "Chabrier_MILES_", "Chabrier_STELIB_", "Kroupa_ELODIE_", "Kroupa_MILES_", "Kroupa_STELIB_",  "Salpeter_ELODIE_", "Salpeter_MILES_", "Salpeter_STELIB_" ]

import astropy.cosmology as co
aa=co.Planck15
import astropy.io.fits as fits
import matplotlib.pyplot as p
import numpy as n
import os

import sys

# global cosmo quantities
z_min = float(sys.argv[1])
z_max = float(sys.argv[2])
#imf = 'kroupa'
#lO2_min = float(sys.argv[3]) # 'salpeter'

SNlimit = 5

smf_ilbert13 = lambda M, M_star, phi_1s, alpha_1s, phi_2s, alpha_2s : ( phi_1s * (M/M_star) ** alpha_1s + phi_2s * (M/M_star) ** alpha_2s ) * n.e ** (-M/M_star) * (M/ M_star)

#ff_dir = os.path.join(os.environ['OBS_REPO'], 'spm', 'firefly')
#ll_dir = os.path.join(os.environ['OBS_REPO'], 'spm', 'literature')
co_dir = os.path.join(os.environ['OBS_REPO'], 'COSMOS', 'catalogs', "photoz-2.0" )
#sdss_dir = os.path.join(os.environ['OBS_REPO'], 'SDSS')
#spiders_dir = os.path.join(os.environ['OBS_REPO'], 'spiders')

#out_dir = os.path.join(os.environ['OBS_REPO'], 'spm', 'results')
out_dir = os.path.join(os.environ['HOME'], 'software/linux/firefly_explore', 'data/images/SMF')

#path_2_sdss_cat = os.path.join( ff_dir, "FireflyGalaxySdssDR14.fits" )
#path_2_eboss_cat = os.path.join( ff_dir, "FireflyGalaxyEbossDR14.fits" )

#path_2_spall_sdss_dr12_cat = os.path.join( sdss_dir, "specObj-SDSS-dr12.fits" )
#path_2_spall_sdss_dr14_cat = os.path.join( sdss_dir, "specObj-SDSS-dr14.fits" )
#path_2_spall_boss_dr12_cat = os.path.join( sdss_dir, "specObj-BOSS-dr12.fits" )
#path_2_spall_boss_dr14_cat = os.path.join( sdss_dir, "specObj-BOSS-dr14.fits" )

#path_2_spall_spiders_dr14_cat = os.path.join( spiders_dir, "cluster_statistics_2016-11-08-DR14_spm.fits" )

#print "SDSS spAll DR14", len(fits.open(path_2_spall_sdss_dr14_cat)[1].data)
#print "BOSS spAll DR14",len(fits.open(path_2_spall_boss_dr14_cat)[1].data)
path_2_cosmos_cat = os.path.join( co_dir, "photoz_vers2.0_010312.fits")
#path_2_vvdsW_cat = os.path.join( ff_dir, "VVDS_WIDE_summary.v1.spm.fits" )
#path_2_vipers_cat = os.path.join( ff_dir, "VIPERS_W14_summary_v2.1.linesFitted.spm.fits" )
#path_2_vvdsD_cat = os.path.join( ff_dir, "VVDS_DEEP_summary.v1.spm.fits" )
#path_2_deep2_cat = os.path.join( ff_dir, "zcat.deep2.dr4.v4.LFcatalogTC.Planck15.spm.v2.fits" )

cosmos = fits.open(path_2_cosmos_cat)[1].data
#deep2   = fits.open(path_2_deep2_cat)[1].data
#vvdsD   = fits.open(path_2_vvdsD_cat)[1].data
#vvdsW   = fits.open(path_2_vvdsW_cat)[1].data
#vipers   = fits.open(path_2_vipers_cat)[1].data
#spiders   = fits.open(path_2_spall_spiders_dr14_cat)[1].data


#path_2_sdss_cat = os.path.join( ff_dir, "FireflyGalaxySdss26.fits" )
#path_2_eboss_cat = os.path.join( ff_dir, "FireflyGalaxyEbossDR14.fits" )

#path_2_pS_salpeter_cat = os.path.join( ll_dir, "portsmouth_stellarmass_starforming_salp-26.fits.gz" )
#path_2_pB_salpeter_cat = os.path.join( ll_dir, "portsmouth_stellarmass_starforming_salp-DR12-boss.fits.gz" )

#path_2_pS_kroupa_cat = os.path.join( ll_dir, "portsmouth_stellarmass_starforming_krou-26.fits.gz" )
#path_2_pB_kroupa_cat = os.path.join( ll_dir, "portsmouth_stellarmass_starforming_krou-DR12-boss.fits.gz" )

#path_2_ppS_kroupa_cat = os.path.join( ll_dir, "portsmouth_stellarmass_passive_krou-26.fits")
#path_2_ppB_kroupa_cat = os.path.join( ll_dir, "portsmouth_stellarmass_passive_krou-DR12.fits")

#path_2_F16_cat = os.path.join( sdss_dir, "RA_DEC_z_w_fluxOII_Mstar_grcol_Mr_lumOII.dat" )

##RA, DEC, z, weigth, O2flux, M_star, gr_color, Mr_5logh, O2luminosity = n.loadtxt(path_2_F16_cat, unpack=True)

#cosmos = fits.open(path_2_cosmos_cat)[1].data
##sdss   = fits.open(path_2_sdss_cat)[1].data
##boss   = fits.open(path_2_eboss_cat)[1].data

#sdss_12_portSF_kr   = fits.open(path_2_pS_kroupa_cat)[1].data
#boss_12_portSF_kr   = fits.open(path_2_pB_kroupa_cat)[1].data

#sdss_12_portPA_kr   = fits.open(path_2_ppS_kroupa_cat)[1].data
#boss_12_portPA_kr   = fits.open(path_2_ppB_kroupa_cat)[1].data

#sdss_12_portSF_sa   = fits.open(path_2_pS_salpeter_cat)[1].data
#boss_12_portSF_sa   = fits.open(path_2_pB_salpeter_cat)[1].data


path_ilbert13_SMF = os.path.join(ll_dir, "ilbert_2013_mass_function_params.txt")
zmin, zmax, N, M_comp, M_star, phi_1s, alpha_1s, phi_2s, alpha_2s, log_rho_s = n.loadtxt(os.path.join( ll_dir, "ilbert_2013_mass_function_params.txt"), unpack=True)

#smfs_ilbert13 = n.array([lambda mass : smf_ilbert13( mass , 10**M_star[ii], phi_1s[ii]*10**(-3), alpha_1s[ii], phi_2s[ii]*10**(-3), alpha_2s[ii] ) for ii in range(len(M_star)) ])

smf0205 = lambda mass : smf_ilbert13( mass , 10**M_star[0], phi_1s[0]*10**(-3), alpha_1s[0], phi_2s[0]*10**(-3), alpha_2s[0] )
smf0508 = lambda mass : smf_ilbert13( mass , 10**M_star[1], phi_1s[1]*10**(-3), alpha_1s[1], phi_2s[1]*10**(-3), alpha_2s[1] )
smf0811 = lambda mass : smf_ilbert13( mass , 10**M_star[2], phi_1s[2]*10**(-3), alpha_1s[2], phi_2s[2]*10**(-3), alpha_2s[2] )

volume_per_deg2 = ( aa.comoving_volume(z_max) -  aa.comoving_volume(z_min) ) * n.pi / 129600.
volume_per_deg2_val = volume_per_deg2.value

# global spm quantities

# stat functions
ld = lambda selection : len(selection.nonzero()[0])

area_sdss = 7900.    
area_boss = 10000.
area_cosmos = 1.52

# stats about DEEP2 run
area1=0.60
area2=0.62
area3=0.90
area4=0.66
if z_min>=0.7:
    area_deep2 = area1+area2+area3+area4
else :
    area_deep2 = 0.6


def get_basic_stat_anyCat(catalog_name, z_name, z_err_name, name, zflg_val):
    catalog = fits.open(catalog_name)[1].data
    catalog_zOk =(catalog[z_err_name] > 0.) & (catalog[z_name] > catalog[z_err_name]) 
    catalog_stat = (catalog_zOk) #& (catalog[z_name] > z_min) & (catalog[z_name] < z_max) 
    catalog_sel = (catalog_stat) & (catalog['LOGMASS'] < 14. ) & (catalog['LOGMASS'] > 0 ) & (catalog['MAXLOGMASS'] - catalog['MINLOGMASS'] <0.4) & (catalog['LOGMASS'] < catalog['MAXLOGMASS'] ) & (catalog['LOGMASS'] > catalog['MINLOGMASS'] )
    m_catalog = catalog['LOGMASS']
    w_catalog =  n.ones_like(catalog['LOGMASS'])
    print catalog_name, "& - & $", ld(catalog_zOk),"$ & $", ld(catalog_sel),"$ \\\\"
    #return catalog_sel, m_catalog, w_catalog

def get_basic_stat_DR12(catalog, z_name, z_err_name, name, zflg_val):
    catalog_zOk =(catalog[z_err_name] > 0.) & (catalog[z_name] > catalog[z_err_name]) 
    catalog_stat = (catalog_zOk) & (catalog[z_name] > z_min) & (catalog[z_name] < z_max) 
    catalog_sel = (catalog_stat) & (catalog['LOGMASS'] < 14. ) & (catalog['LOGMASS'] > 0 ) & (catalog['MAXLOGMASS'] - catalog['MINLOGMASS'] <0.4) & (catalog['LOGMASS'] < catalog['MAXLOGMASS'] ) & (catalog['LOGMASS'] > catalog['MINLOGMASS'] )
    m_catalog = catalog['LOGMASS']
    w_catalog =  n.ones_like(catalog['LOGMASS'])
    print name, "& - & $", ld(catalog_zOk),"$ & $", ld(catalog_sel),"$ \\\\"
    return catalog_sel, m_catalog, w_catalog

def get_basic_stat_DR14(catalog, z_name, z_err_name, class_name, zwarning, name, zflg_val, prefix):
    catalog_zOk =(catalog[z_err_name] > 0.) & (catalog[z_name] > catalog[z_err_name])  & (catalog[class_name]=='GALAXY')  & (catalog[zwarning]==zflg_val)
    catalog_stat = (catalog_zOk) & (catalog[z_name] > z_min) & (catalog[z_name] < z_max) 
    catalog_sel = (catalog_stat) & (catalog[prefix+'stellar_mass'] < 10**14. ) & (catalog[prefix+'stellar_mass'] > 0 )  & (catalog[prefix+'stellar_mass'] > catalog[prefix+'stellar_mass_low_1sig'] ) & (catalog[prefix+'stellar_mass'] < catalog[prefix+'stellar_mass_up_1sig'] ) & ( - n.log10(catalog[prefix+'stellar_mass_low_1sig'])  + n.log10(catalog[prefix+'stellar_mass_up_1sig']) < 0.4 )
    m_catalog = n.log10(catalog[prefix+'stellar_mass'])
    w_catalog =  n.ones_like(catalog[prefix+'stellar_mass'])
    print name, '& $',len(catalog), "$ & $", ld(catalog_zOk),"$ & $", ld(catalog_sel),"$ \\\\"
    return catalog_sel, m_catalog, w_catalog
    
def get_hist(masses, weights, mbins):
    NN = n.histogram(masses, mbins)[0]
    NW = n.histogram(masses, mbins, weights = weights)[0]
    xx = (mbins[1:] + mbins[:-1])/2.
    return xx, NW, NN**(-0.5)*NW


dlog10m = 0.25
mbins = n.arange(8,12.5,dlog10m)

def plot_smf_b(IMF="Chabrier_ELODIE_"):
	boss_sel, boss_m, boss_w = get_basic_stat_DR14(boss, 'Z_NOQSO', 'Z_ERR_NOQSO', 'CLASS_NOQSO', 'ZWARNING_NOQSO', IMF+' & BOSS & 14 ', 0., IMF)
	x, y, ye = get_hist(boss_m[boss_sel], weights = boss_w[boss_sel]/(dlog10m*n.log(10)*area_boss*volume_per_deg2_val), mbins = mbins)
	p.errorbar(x, y, yerr = ye)#, label=IMF+'BOSS', lw=1)
	return x,y,ye

def plot_smf_s(IMF="Chabrier_ELODIE_"):
	boss_sel, boss_m, boss_w = get_basic_stat_DR14(sdss, 'Z', 'Z_ERR', 'CLASS', 'ZWARNING', IMF+' & BOSS & 14 ', 0., IMF)
	x, y, ye = get_hist(boss_m[boss_sel], weights = boss_w[boss_sel]/(dlog10m*n.log(10)*area_boss*volume_per_deg2_val), mbins = mbins)
	p.errorbar(x, y, yerr = ye)#, label=IMF+'SDSS', lw=1)
	return x,y,ye

#def plot_smf_spiders(IMF="Chabrier_ELODIE_"):
	#boss_sel, boss_m, boss_w = get_basic_stat_DR14(spiders, 'Z', 'Z_ERR', 'CLASS', 'ZWARNING', IMF+' & BOSS & 14 ', 0., IMF)
	#x, y, ye = get_hist(boss_m[boss_sel], weights = boss_w[boss_sel]/(dlog10m*n.log(10)*area_boss*volume_per_deg2_val), mbins = mbins)
	#p.errorbar(x, y, yerr = ye, label=IMF+'SPIDERS', lw=1)


def get_basic_stat(catalog, z_name, z_flg, name, zflg_min, prefix):
    catalog_zOk = (catalog[z_name] > z_min) & (catalog[z_flg]>=zflg_min) 
    catalog_stat = (catalog_zOk) & (catalog[z_name] > z_min) & (catalog[z_name] < z_max) & (catalog['SSR']>0) & (catalog['TSR']>0) & (catalog['SSR']<=1.0001) & (catalog['TSR']<=1.0001)
    catalog_sel = (catalog_stat) & (catalog[prefix+'stellar_mass'] < 10**14. ) & (catalog[prefix+'stellar_mass'] >= 10**5. )  & (catalog[prefix+'stellar_mass'] <= catalog[prefix+'stellar_mass_up_1sig'] ) & (catalog[prefix+'stellar_mass'] >= catalog[prefix+'stellar_mass_low_1sig'] ) & (-n.log10(catalog[prefix+'stellar_mass_low_1sig'])  + n.log10(catalog[prefix+'stellar_mass_up_1sig']) < 0.6 	)
    l_o2 = lineSelection(catalog, "O2_3728") & catalog_stat
    l_o3 = lineSelection(catalog, "O3_5007") & catalog_stat
    l_hb = lineSelection(catalog, "H1_4862") & catalog_stat
    m_catalog = n.log10(catalog[prefix+'stellar_mass'])
    w_catalog = 1. / (catalog['TSR'] * catalog['SSR'])
    #print name, '& $',len(catalog), "$ & $", ld(catalog_zOk),"$ & $", ld(catalog_stat), "\\;(", ld(catalog_sel),")$ & $", ld(l_o2), "\\;(", ld(catalog_sel & l_o2),")$ & $", ld(l_o3), "\\;(", ld(catalog_sel & l_o3),")$ & $", ld(l_hb), "\\;(", ld(catalog_sel & l_hb),")$ \\\\"
    return catalog_sel, m_catalog, w_catalog, l_o2, l_o3, l_hb
    

x_M13, yM13 = n.loadtxt( os.path.join(os.environ['HOME'],'/software/linux/firefly_explore/data/literature/Maraston_13_05_06.txt' ), unpack=True) 

p.figure(1, (8,8))
if z_min==0.2:
	p.plot(mbins, smf0205(10**mbins), label='Il 13, 0.2<z<0.5', ls='dashed', lw=3)
if z_min==0.5:
	p.plot(mbins, smf0508(10**mbins), label='Il 13, 0.5<z<0.8', ls='dashed', lw=3)
if z_min==0.8:
	p.plot(mbins, smf0811(10**mbins), label='Il 13, 0.8<z<1.1', ls='dashed', lw=3)

p.plot(x_M13, yM13, label='Ma 13, 0.5<z<0.6', ls='dashed', lw=3)

# DEEP2 lines
xs,ys,yes = [],[],[]
for prefix in imfs :
	deep2_sel, deep2_m, deep2_w, deep2_o2, deep2_o3, deep2_hb = get_basic_stat(deep2, 'ZBEST', 'ZQUALITY', 'DEEP2', 2., prefix)
	x, y, ye = get_hist(deep2_m[deep2_sel], weights = deep2_w[deep2_sel]/(dlog10m*n.log(10)*area_deep2*volume_per_deg2_val), mbins = mbins)
	p.errorbar(x, y, yerr = ye)
	xs.append(x)
	ys.append(y)
	yes.append(ye)

xs  = n.array(xs )
ys  = n.array(ys )
yes = n.array(yes)

y_up  = ys+yes
y_low = ys-yes

ok = (n.min(y_low, axis=0) < n.max(y_up, axis=0))
p.fill_between(xs[0][ok], y1=n.min(y_low, axis=0)[ok], y2=n.max(y_up, axis=0)[ok], color='g', alpha=0.3, label='DEEP2')

# BOSS eBOSS lines
xs,ys,yes = [],[],[]
for prefix in imfs :
	x, y, ye = plot_smf_b(prefix)
	xs.append(x)
	ys.append(y)
	yes.append(ye)

xs  = n.array(xs )
ys  = n.array(ys )
yes = n.array(yes)

y_up  = ys+yes
y_low = ys-yes

p.fill_between(xs[0], y1=n.min(y_low, axis=0), y2=n.max(y_up, axis=0), color='r', alpha=0.3, label='eBOSS')

# SDSS 

xs,ys,yes = [],[],[]
for prefix in imfs :
	x, y, ye = plot_smf_s(prefix)
	xs.append(x)
	ys.append(y)
	yes.append(ye)

xs  = n.array(xs )
ys  = n.array(ys )
yes = n.array(yes)

y_up  = ys+yes
y_low = ys-yes

p.fill_between(xs[0], y1=n.min(y_low, axis=0), y2=n.max(y_up, axis=0), color='b', alpha=0.3, label='SDSS')


p.title(str(z_min)+'<z<'+str(z_max))
p.xlabel(r"$\log_{10}$ (M / $M_\odot$ )")
p.ylabel(r'$\Phi(M)$ [Mpc$^{-3}$ dex$^{-1}$]')
p.yscale('log')
p.legend(loc=0, frameon = False)
p.ylim((1e-8, 1e-2))
p.xlim((9.5, 12.5))
p.grid()
p.savefig(os.path.join(out_dir, "firefly_SMFs_BOSS_"+str(z_min)+'_z_'+str(z_max)+".png" ))
p.clf()


