from lib_spm import *

imfs = ["Chabrier_ELODIE_", "Chabrier_MILES_", "Chabrier_STELIB_", "Kroupa_ELODIE_", "Kroupa_MILES_", "Kroupa_STELIB_",  "Salpeter_ELODIE_", "Salpeter_MILES_", "Salpeter_STELIB_" ]

out_file = os.path.join('../../data/tables/', "table1_eboss.tex")
f=open(out_file, 'w')

for IMF in imfs :
	prf = IMF.split('_')[0]+' & '+IMF.split('_')[1]
	l2w = get_basic_stat_firefly_DR14(boss, 'Z_NOQSO', 'Z_ERR_NOQSO', 'CLASS_NOQSO', 'ZWARNING_NOQSO', prf, 0., IMF)
	f.write(l2w + " \n")
	
f.write('\\hline \n')

f.close()


out_file = os.path.join('../../data/tables/', "table1_sdss.tex")
f=open(out_file, 'w')

for IMF in imfs :
	prf = IMF.split('_')[0]+' & '+IMF.split('_')[1]
	l2w = get_basic_stat_firefly_DR14(sdss, 'Z', 'Z_ERR', 'CLASS', 'ZWARNING', prf, 0., IMF)
	f.write(l2w + " \n")

f.write('\\hline \n')
f.close()

