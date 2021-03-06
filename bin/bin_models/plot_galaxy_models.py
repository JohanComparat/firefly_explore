import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as p
import sys
import os
import numpy as n
import GalaxySpectrumFIREFLY as gs

##        Index band       blue continuum     red continuum Units name
#01    4142.125 4177.125  4080.125 4117.625  4244.125 4284.125 1  CN_1   
iii, b0, b1, bc0, bc1, rc0, rc1, unit, name = n.loadtxt('../../data/lick_indices/indices_table.txt', unpack=True, dtype='str')

li0 = b0.astype('float')
li1 = b1.astype('float')

dir_elodie = os.path.join( os.environ['STELLARPOPMODELS_DIR'], 'data', 'SSP_M11_ELODIE') 
dir_miles = os.path.join( os.environ['STELLARPOPMODELS_DIR'], 'data', 'SSP_M11_MILES') 
dir_stelib = os.path.join( os.environ['STELLARPOPMODELS_DIR'], 'data', 'SSP_M11_STELIB') 

IMF = {'cha': 'Ch', 'kr': 'Kr', 'ss': 'Sa'}

spec_sdss = gs.GalaxySpectrumFIREFLY( '/home/comparat/SDSS/26/spectra/0266/spec-0266-51602-0004.fits' )
spec_sdss.openObservedSDSSSpectrum('sdssMain')

spec_boss = gs.GalaxySpectrumFIREFLY( '/home/comparat/SDSS/v5_10_0/spectra/3586/spec-3586-55181-0024.fits' )
spec_boss.openObservedSDSSSpectrum('sdss4')

path_2_deep2 = '/home/comparat/data2/firefly/v1_1_0/DEEP2/spectra/2/deep2-2249-22052688.fits' 
spec_deep2 = gs.GalaxySpectrumFIREFLY( path_2_deep2 )
spec_deep2.openObservedDEEP2pectrum(path_2_deep2, survey='deep2_fits')

file_list_elodie = n.array([
# chabrier
#os.path.join(dir_elodie, 'ssp_M11_ELODIE.chaz001'),
os.path.join(dir_elodie, 'ssp_M11_ELODIE.chaz002'),
#os.path.join(dir_elodie, 'ssp_M11_ELODIE.chaz004'),
# kroupa
#os.path.join(dir_elodie, 'ssp_M11_ELODIE.krz001'),
os.path.join(dir_elodie, 'ssp_M11_ELODIE.krz002'),
#os.path.join(dir_elodie, 'ssp_M11_ELODIE.krz004'),
# salpeter
#os.path.join(dir_elodie, 'ssp_M11_ELODIE.ssz001'),
os.path.join(dir_elodie, 'ssp_M11_ELODIE.ssz002'),
#os.path.join(dir_elodie, 'ssp_M11_ELODIE.ssz004')
])

file_list_miles = n.array([
# chabrier
#os.path.join(dir_miles, 'ssp_M11_MILES.chaz001'),
os.path.join(dir_miles, 'ssp_M11_MILES.chaz002'),
#os.path.join(dir_miles, 'ssp_M11_MILES.chaz004'),
# kroupa
#os.path.join(dir_miles, 'ssp_M11_MILES.krz001'),
os.path.join(dir_miles, 'ssp_M11_MILES.krz002'),
#os.path.join(dir_miles, 'ssp_M11_MILES.krz004'),
# salpeter
#os.path.join(dir_miles, 'ssp_M11_MILES.ssz001'),
os.path.join(dir_miles, 'ssp_M11_MILES.ssz002'),
#os.path.join(dir_miles, 'ssp_M11_MILES.ssz004')
])

file_list_stelib = n.array([
# chabrier
#os.path.join(dir_stelib, 'ssp_M11_STELIB.chaz001'),
os.path.join(dir_stelib, 'ssp_M11_STELIB.chaz002'),
#os.path.join(dir_stelib, 'ssp_M11_STELIB.chaz004'),
# kroupa
#os.path.join(dir_stelib, 'ssp_M11_STELIB.krz001'),
os.path.join(dir_stelib, 'ssp_M11_STELIB.krz002'),
#os.path.join(dir_stelib, 'ssp_M11_STELIB.krz004'),
# salpeter
#os.path.join(dir_stelib, 'ssp_M11_STELIB.ssz001'),
os.path.join(dir_stelib, 'ssp_M11_STELIB.ssz002'),
#os.path.join(dir_stelib, 'ssp_M11_STELIB.ssz004')
])


aaa = 10


p.figure(0, (12,5))
p.axes([0.1,0.15,0.85,0.8])

#for a0, a1, na in zip(li0, li1, name):
	#if a1<4200 and a1>3900:
		#p.plot([a0,a1],[1e29,1e29])
		#p.text(a0, 1.3e29, na)

for file_name in file_list_miles:
	ids = os.path.basename(file_name).split('.')[-1]
	imf = ids[:-4]
	zzz = ids[-3:]
	DATA = n.loadtxt(file_name, unpack=True)
	ages = n.array(list(set(DATA[0])))
	ages.sort()
	for age in ages[(ages==aaa)]:
		sel = (DATA[0]==age)
		p.plot(DATA[2][sel], DATA[3][sel],label="MILES, "+IMF[imf],rasterized=True, lw=0.7)

#p.plot(spec_sdss.restframe_wavelength,  3e28*spec_sdss.flux, label='sdss')
p.plot(spec_boss.restframe_wavelength,  3e28*spec_boss.flux, label='rescaled boss spectrum z='+str(n.round(spec_boss.redshift,2)), lw=0.7)
#p.plot(spec_deep2.restframe_wavelength, 3e28*spec_deep2.flux, label='deep2')
p.axvline(3934, ls='dashed', label='Ca H')
p.axvline(3969, ls='dashed', label='Ca K', c='m')
p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
#p.xscale('log')
p.yscale('log')
p.ylim((6e27,2e29))
p.xlim((3900,4200))
p.grid()
p.title(str(aaa)+' Gyr old, Solar metallicity')
p.legend(frameon=False, loc=0)
p.savefig('/home/comparat/software/linux/firefly_explore/data/images/models/Zsun_'+str(aaa)+'Gyr_MILES_models_38_45.png')
p.clf()

p.figure(0, (12,5))
p.axes([0.1,0.15,0.85,0.8])

for file_name in file_list_stelib:
	ids = os.path.basename(file_name).split('.')[-1]
	imf = ids[:-4]
	zzz = ids[-3:]
	DATA = n.loadtxt(file_name, unpack=True)
	ages = n.array(list(set(DATA[0])))
	ages.sort()
	for age in ages[(ages==aaa)]:
		sel = (DATA[0]==age)
		p.plot(DATA[2][sel], DATA[3][sel],label="STELIB "+IMF[imf],rasterized=True, lw=0.7)


#p.plot(spec_sdss.restframe_wavelength,  1e30*spec_sdss.flux, label='sdss')
p.plot(spec_boss.restframe_wavelength,  3e28*spec_boss.flux, label='rescaled boss spectrum z='+str(n.round(spec_boss.redshift,2)), lw=0.7)
#p.plot(spec_deep2.restframe_wavelength, 1e30*spec_deep2.flux, label='deep2')
p.axvline(3934, ls='dashed', label='Ca H')
p.axvline(3969, ls='dashed', label='Ca K', c='m')
p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
#p.xscale('log')
p.yscale('log')
p.ylim((6e27,2e29))
p.xlim((3900,4200))
p.grid()
p.title(str(aaa)+' Gyr old, Solar metallicity')
p.legend(frameon=False, loc=0)
p.savefig('/home/comparat/software/linux/firefly_explore/data/images/models/Zsun_'+str(aaa)+'Gyr_STELIB_models_38_45.png')
p.clf()


p.figure(0, (12,5))
p.axes([0.1,0.15,0.85,0.8])

for file_name in file_list_elodie:
	ids = os.path.basename(file_name).split('.')[-1]
	imf = ids[:-4]
	zzz = ids[-3:]
	DATA = n.loadtxt(file_name, unpack=True)
	ages = n.array(list(set(DATA[0])))
	ages.sort()
	for age in ages[(ages==aaa)]:
		sel = (DATA[0]==age)
		p.plot(DATA[2][sel], DATA[3][sel],label="ELODIE, "+IMF[imf],rasterized=True, lw=0.7)

#p.plot(spec_sdss.restframe_wavelength,  1e30*spec_sdss.flux, label='sdss')
p.plot(spec_boss.restframe_wavelength,  3e28*spec_boss.flux, label='rescaled boss spectrum z='+str(n.round(spec_boss.redshift,2)), lw=0.7)
#p.plot(spec_deep2.restframe_wavelength, 1e30*spec_deep2.flux, label='deep2')
p.axvline(3934, ls='dashed', label='Ca H')
p.axvline(3969, ls='dashed', label='Ca K', c='m')
p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
#p.xscale('log')
p.yscale('log')
p.ylim((6e27,2e29))
p.xlim((3900,4200))
p.grid()
p.title(str(aaa)+' Gyr old, Solar metallicity')
p.legend(frameon=False, loc=0)
p.savefig('/home/comparat/software/linux/firefly_explore/data/images/models/Zsun_'+str(aaa)+'Gyr_ELODIE_models_38_45.png')
p.clf()


sys.exit()

# 10 Gyr model, solar metallicity
aaa = 10


p.figure(0, (12,5))
p.axes([0.1,0.15,0.85,0.8])

for file_name in file_list_miles:
	ids = os.path.basename(file_name).split('.')[-1]
	imf = ids[:-4]
	zzz = ids[-3:]
	DATA = n.loadtxt(file_name, unpack=True)
	ages = n.array(list(set(DATA[0])))
	ages.sort()
	for age in ages[(ages==aaa)]:
		sel = (DATA[0]==age)
		p.plot(DATA[2][sel], DATA[3][sel],label="MILES, "+IMF[imf],rasterized=True, lw=0.5)

p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
#p.xscale('log')
p.yscale('log')
p.ylim((1e28,2e29))
#p.xlim((3000,9700))
p.grid()
p.title(str(aaa)+' Gyr old, Solar metallicity')
p.legend(frameon=False, loc=0)
p.savefig('/home/comparat/software/linux/firefly_explore/data/images/models/Zsun_'+str(aaa)+'Gyr_MILES_models.png')
p.clf()


p.figure(0, (12,5))
p.axes([0.1,0.15,0.85,0.8])

for file_name in file_list_stelib:
	ids = os.path.basename(file_name).split('.')[-1]
	imf = ids[:-4]
	zzz = ids[-3:]
	DATA = n.loadtxt(file_name, unpack=True)
	ages = n.array(list(set(DATA[0])))
	ages.sort()
	for age in ages[(ages==aaa)]:
		sel = (DATA[0]==age)
		p.plot(DATA[2][sel], DATA[3][sel],label="STELIB "+IMF[imf],rasterized=True, lw=0.5)


p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
#p.xscale('log')
p.yscale('log')
p.ylim((1e28,2e29))
#p.xlim((3000,9700))
p.grid()
p.title(str(aaa)+' Gyr old, Solar metallicity')
p.legend(frameon=False, loc=0)
p.savefig('/home/comparat/software/linux/firefly_explore/data/images/models/Zsun_'+str(aaa)+'Gyr_STELIB_models.png')
p.clf()


p.figure(0, (12,5))
p.axes([0.1,0.15,0.85,0.8])

for file_name in file_list_elodie:
	ids = os.path.basename(file_name).split('.')[-1]
	imf = ids[:-4]
	zzz = ids[-3:]
	DATA = n.loadtxt(file_name, unpack=True)
	ages = n.array(list(set(DATA[0])))
	ages.sort()
	for age in ages[(ages==aaa)]:
		sel = (DATA[0]==age)
		p.plot(DATA[2][sel], DATA[3][sel],label="ELODIE, "+IMF[imf],rasterized=True, lw=0.5)


p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
#p.xscale('log')
p.yscale('log')
p.ylim((1e28,2e29))
#p.xlim((3000,9700))
p.grid()
p.title(str(aaa)+' Gyr old, Solar metallicity')
p.legend(frameon=False, loc=0)
p.savefig('/home/comparat/software/linux/firefly_explore/data/images/models/Zsun_'+str(aaa)+'Gyr_ELODIE_models.png')
p.clf()


sys.exit()



p.figure(0, (12,5))
p.axes([0.1,0.15,0.85,0.8])

for file_name in file_list_miles:
	ids = os.path.basename(file_name).split('.')[-1]
	imf = ids[:-4]
	zzz = ids[-3:]
	DATA = n.loadtxt(file_name, unpack=True)
	ages = n.array(list(set(DATA[0])))
	ages.sort()
	for age in ages[(ages==aaa)]:
		sel = (DATA[0]==age)
		p.plot(DATA[2][sel], DATA[3][sel],label="MILES, "+IMF[imf],rasterized=True, lw=0.5)

for file_name in file_list_stelib:
	ids = os.path.basename(file_name).split('.')[-1]
	imf = ids[:-4]
	zzz = ids[-3:]
	DATA = n.loadtxt(file_name, unpack=True)
	ages = n.array(list(set(DATA[0])))
	ages.sort()
	for age in ages[(ages==aaa)]:
		sel = (DATA[0]==age)
		p.plot(DATA[2][sel], DATA[3][sel],label="STELIB "+IMF[imf],rasterized=True, lw=0.5)


for file_name in file_list_elodie:
	ids = os.path.basename(file_name).split('.')[-1]
	imf = ids[:-4]
	zzz = ids[-3:]
	DATA = n.loadtxt(file_name, unpack=True)
	ages = n.array(list(set(DATA[0])))
	ages.sort()
	for age in ages[(ages==aaa)]:
		sel = (DATA[0]==age)
		p.plot(DATA[2][sel], DATA[3][sel],label="ELODIE, "+IMF[imf],rasterized=True, lw=0.5)


p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
#p.xscale('log')
p.yscale('log')
p.ylim((1e28,2e29))
#p.xlim((3000,9700))
p.grid()
p.title(str(aaa)+' Gyr old, Solar metallicity')
p.legend(frameon=False, loc=0)
p.savefig('/home/comparat/software/linux/firefly_explore/data/images/models/Zsun_'+str(aaa)+'Gyr_all_models.png')
p.clf()

p.figure(0, (12,5))
p.axes([0.1,0.15,0.85,0.8])

for file_name in file_list_elodie:
	ids = os.path.basename(file_name).split('.')[-1]
	imf = ids[:-4]
	zzz = ids[-3:]
	DATA = n.loadtxt(file_name, unpack=True)
	ages = n.array(list(set(DATA[0])))
	ages.sort()
	for age in ages[::15]:
		sel = (DATA[0]==age)
		p.plot(DATA[2][sel], DATA[3][sel],label="age="+str(n.round(age,3))+" Gyr, imf="+imf,rasterized=True, lw=0.5)

p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
#p.xscale('log')
p.yscale('log')
p.ylim((1e28,1e33))
#p.xlim((3000,9700))
p.grid()
p.title('ELODIE, Solar metallicity')
p.legend(frameon=False, loc=0)
p.savefig('/home/comparat/software/linux/firefly_explore/data/images/models/elodie_galaxy_models.png')
p.clf()



p.figure(0, (12,5))
p.axes([0.1,0.15,0.85,0.8])

for file_name in file_list_stelib:
	ids = os.path.basename(file_name).split('.')[-1]
	imf = ids[:-4]
	zzz = ids[-3:]
	DATA = n.loadtxt(file_name, unpack=True)
	ages = n.array(list(set(DATA[0])))
	ages.sort()
	for age in ages[::15]:
		sel = (DATA[0]==age)
		p.plot(DATA[2][sel], DATA[3][sel],label="age="+str(n.round(age,3))+" Gyr, imf="+imf,rasterized=True, lw=0.5)

p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
#p.xscale('log')
p.yscale('log')
p.ylim((1e28,1e33))
#p.xlim((3000,9700))
p.grid()
p.title('STELIB, Solar metallicity')
p.legend(frameon=False, loc=0)
p.savefig('/home/comparat/software/linux/firefly_explore/data/images/models/stelib_galaxy_models.png')
p.clf()

