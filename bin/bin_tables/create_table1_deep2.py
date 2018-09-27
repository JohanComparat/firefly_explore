from lib_spm import *

imfs = ["Chabrier_ELODIE_", "Chabrier_MILES_", "Chabrier_STELIB_", "Kroupa_ELODIE_", "Kroupa_MILES_", "Kroupa_STELIB_",  "Salpeter_ELODIE_", "Salpeter_MILES_", "Salpeter_STELIB_" ]

out_file = os.path.join('../../data/tables/', "table_deep2_r.tex")
f=open(out_file, 'w')

for IMF in imfs :
	prf = IMF.split('_')[0]+' & '+IMF.split('_')[1]
	l2w = get_basic_stat_deep2(deep2, 'ZBEST', 'ZQUALITY', prf, 2., IMF, o2=True)
	f.write(l2w + " \n")

f.close()


out_file = os.path.join('../../data/tables/', "table_deep2.tex")
f=open(out_file, 'w')

for IMF in imfs :
	prf = IMF.split('_')[0]+' & '+IMF.split('_')[1]
	l2w = get_basic_stat_deep2(deep2, 'ZBEST', 'ZQUALITY', prf, 2., IMF, o2=False)
	f.write(l2w + " \n")

f.close()

