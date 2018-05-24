import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as p
import sys
import os
import numpy as n

dir_elodie = os.path.join( os.environ['STELLARPOPMODELS_DIR'], 'data', 'SSP_M11_ELODIE') 
dir_miles = os.path.join( os.environ['STELLARPOPMODELS_DIR'], 'data', 'SSP_M11_MILES') 
dir_stelib = os.path.join( os.environ['STELLARPOPMODELS_DIR'], 'data', 'SSP_M11_STELIB') 

IMF = {'cha': 'Ch', 'kr': 'Kr', 'ss': 'Sa'}

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

p.axvline(3934, ls='dashed', label='Ca H')
p.axvline(3969, ls='dashed', label='Ca K')
p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
#p.xscale('log')
p.yscale('log')
p.ylim((6e27,1e29))
p.xlim((3800,4500))
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


p.axvline(3934, ls='dashed', label='Ca H')
p.axvline(3969, ls='dashed', label='Ca K')
p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
#p.xscale('log')
p.yscale('log')
p.ylim((6e27,1e29))
p.xlim((3800,4500))
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

p.axvline(3934, ls='dashed', label='Ca H')
p.axvline(3969, ls='dashed', label='Ca K')
p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
#p.xscale('log')
p.yscale('log')
p.ylim((6e27,1e29))
p.xlim((3800,4500))
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

