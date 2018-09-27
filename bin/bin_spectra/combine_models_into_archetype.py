import numpy as np
import astropy.io.fits as pyfits
import astropy.units as u
import os,sys
import matplotlib.pyplot as plt

#>>>>>> STELIB: 3.4AA sampling at 5500AA, covers 3200-9300AA
#>>>>>> MILES: 2.5AA sampling at 5500AA, covers 3500-7430AA
#>>>>>> ELODIE: 0.5AA sampling at 5500AA, covers 3900-6800AA

path_2_file = "/home/comparat/data2/firefly/v1_1_0/v5_10_0/stellarpop/7612/spFly-7612-56972-0896.fits"
specLiteFile = "/home/comparat/SDSS/v5_10_0/spectra/7612/spec-7612-56972-0896.fits"

path_2_out = "/home/comparat/spFlyModel-7612-56972-0896.fits"

hdulist = pyfits.open(specLiteFile)
wavelength = 10**hdulist[1].data['loglam']
flux = hdulist[1].data['flux']
error = hdulist[1].data['ivar']**(-0.5)
bad_flags = np.ones(len(wavelength))
redshift = hdulist[2].data['Z_NOQSO'][0] 
restframe_wavelength = wavelength / (1.0+redshift)
N_angstrom_masked = 20.
bad_data = np.isnan(flux) | np.isinf(flux) | (flux <= 0.0) | np.isnan(error) | np.isinf(error)

keep_lines = ((restframe_wavelength > 3728 - N_angstrom_masked) & (restframe_wavelength < 3728 + N_angstrom_masked)) | ((restframe_wavelength > 5007 - N_angstrom_masked) & (restframe_wavelength < 5007 + N_angstrom_masked)) | ((restframe_wavelength > 4861 - N_angstrom_masked) & (restframe_wavelength < 4861 + N_angstrom_masked)) | ((restframe_wavelength > 6564 - N_angstrom_masked) & (restframe_wavelength < 6564 + N_angstrom_masked)) 
wl_s = ( ( wavelength>9300 ) | (keep_lines) ) & (bad_data==False)


line_mask = lambda wwl :   ((wwl > 3728 - N_angstrom_masked) & (wwl < 3728 + N_angstrom_masked)) | ((wwl > 5007 - N_angstrom_masked) & (wwl < 5007 + N_angstrom_masked)) | ((wwl > 4861 - N_angstrom_masked) & (wwl < 4861 + N_angstrom_masked)) | ((wwl > 6564 - N_angstrom_masked) & (wwl < 6564 + N_angstrom_masked)) 

ff=pyfits.open(path_2_file)

ff4_s = (ff[4].data['wavelength'] > 3900) & (ff[4].data['wavelength'] < 6800) &(line_mask(ff[4].data['wavelength'])==False)

ff1_s = (( (ff[1].data['wavelength'] > 3500) & (ff[1].data['wavelength'] < 3930) )|( (ff[1].data['wavelength'] > 6800) & (ff[1].data['wavelength'] < 7430) )     ) &(line_mask(ff[1].data['wavelength'])==False)

ff7_s = (((ff[7].data['wavelength'] > 3200) & (ff[7].data['wavelength'] < 3500)) | ((ff[7].data['wavelength'] > 7430) & (ff[7].data['wavelength'] < 9300))      )&(line_mask(ff[7].data['wavelength'])==False)


x=np.hstack((
ff[4].data['wavelength'][ff4_s],
ff[1].data['wavelength'][ff1_s],
ff[7].data['wavelength'][ff7_s],
wavelength[wl_s]
))

y=np.hstack((
ff[4].data['firefly_model'][ff4_s],
ff[1].data['firefly_model'][ff1_s],
ff[7].data['firefly_model'][ff7_s],
flux[wl_s]
))

ids = np.argsort(x)

wl = x[ids]
fl = y[ids]

waveCol = pyfits.Column(name="wavelength",format="D", unit="Angstrom", array= wl)
dataCol = pyfits.Column(name="model",format="D", unit="1e-17erg/s/cm2/Angstrom", array = fl)
cols = pyfits.ColDefs([ waveCol, dataCol ])
tbhdu = pyfits.BinTableHDU.from_columns(cols)

tbhdu.header['EBV']    = 0.6

prihdr = pyfits.Header()
prihdr['author'] = 'JC'
prihdr['file'] = os.path.basename(path_2_out)

prihdu = pyfits.PrimaryHDU(header=prihdr)
thdulist = pyfits.HDUList([prihdu, tbhdu])

if os.path.isfile(path_2_out ):
  os.remove(path_2_out )
thdulist.writeto(path_2_out )


plt.figure(0, (10,4))

plt.plot(wl,fl,label='stitched model', lw=0.8)

plt.plot(ff[4].data['wavelength'][ff4_s], ff[4].data['firefly_model'][ff4_s],ls='None',marker=',', label='ELODIE')
plt.plot(ff[1].data['wavelength'][ff1_s], ff[1].data['firefly_model'][ff1_s],ls='None',marker=',', label='MILES')
plt.plot(ff[7].data['wavelength'][ff7_s], ff[7].data['firefly_model'][ff7_s],ls='None',marker=',', label='STELIB')
plt.plot(wavelength[wl_s]               , flux[wl_s]                        ,ls='None',marker=',', label='DATA')
plt.axvline(3200, ls='dashed',lw=0.8,label='3,200A')
plt.axvline(10350,ls='dashed',lw=0.8, label='10,350A')
plt.grid()
plt.legend()
plt.ylabel('flux erg/cm2/s/A')
plt.xlabel('wavelength')
plt.savefig(path_2_out[:-4]+"png")
plt.clf()
