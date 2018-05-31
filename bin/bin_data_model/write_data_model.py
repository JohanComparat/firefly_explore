from lib_spm import *

#boss
#sdss
#deep2

f=open('../../data/data_model/sdss.tex', 'w')
for el in sdss.columns :
	f.write(r"\_".join(el.name.split('_'))+":  \\newline \n")

f.close()

f=open('../../data/data_model/deep2.tex', 'w')
for el in deep2.columns :
	f.write(r"\_".join(el.name.split('_'))+":  \\newline \n")

f.close()

f=open('../../data/data_model/eboss.tex', 'w')
for el in boss.columns :
	f.write(r"\_".join(el.name.split('_'))+":  \\newline \n")

f.close()