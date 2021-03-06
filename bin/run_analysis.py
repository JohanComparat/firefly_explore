#!/bin/bash

# on ds52, 

# first create tables 
# to be executed only once 

cd /home/comparat/software/linux/firefly_explore/bin/bin_deep2
python measure_SNMEDIAN_DEEP2.py

cd /home/comparat/software/linux/firefly_explore/bin/bin_tables

python make_fly_plate_list.py v5_10_0
python summary_table_concatenate_spFlyAll.py v5_10_0
python summary_table_merge_specObjAll_SNRall.py v5_10_0
python summary_table_merge_firefly_MAG.py v5_10_0

python make_fly_plate_list.py 26
python summary_table_concatenate_spFlyAll.py 26
python summary_table_merge_specObjAll_SNRall.py 26
python summary_table_merge_firefly_MAG.py 26

#CATALOG are written here 
#/data37s/SDSS/26/catalogs
#/data37s/SDSS/v5_10_0/catalogs

python create_table1.py
python create_table_completeness.py sdss
python create_table_completeness.py boss
python create_table_snr.py sdss
python create_table_snr.py boss
python create_table_delta_mag.py sdss
python create_table_delta_mag.py boss
#python create_table_completeness.py deep2

# writes here os.environ['OBS_REPO'], 'spm', 'results', "table_1.tex" and "table_2.tex" and *.tex for the appendix tables.

# copy the tables to the public site
cp /data36s/comparat/spm/results/*.tex /data42s/comparat/firefly/v1_1_0/tables/
cd /data42s/comparat/firefly/v1_1_0/tables/
chmod o+r * 


# plots the spectra showed in the paper
cd /home/comparat/software/linux/firefly_explore/bin/bin_spectra

# Figures 1,2,3
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/v5_10_0/stellarpop/3586/spFly-3586-55181-0003.fits
python3.6 plot_result_file.py /data42s/comparat/firefly/v1_1_0/26/stellarpop/0266/spFly-0266-51602-0004.fits 
python3.6 plot_result_file_deep2.py /data42s/comparat/firefly/v1_1_0/DEEP2/stellarpop/1/spFly-deep2-1103-11013914.fits

cp /data42s/comparat/firefly/v1_1_0/v5_10_0/stellarpop/3586/spFly-3586-55181-0003.png ../../data/spec_plot/
cp /data42s/comparat/firefly/v1_1_0/26/stellarpop/0266/spFly-0266-51602-0004.png  ../../data/spec_plot/
cp /data42s/comparat/firefly/v1_1_0/DEEP2/stellarpop/1/spFly-deep2-1103-11013914.png ../../data/spec_plot/

# explore the parameter space 
cd /home/comparat/software/linux/firefly_explore/bin/bin_parameters_exploration

# Figure 4
python3.4 plot_age_metal_plane.py
python3.4 plot_age_metal_plane_per_SSP.py

# Figure 5, 6, 8, 9, 10
python3.4 plot_differences_age_sdss.py
python3.4 plot_differences_age_eboss.py
python3.4 plot_differences_age_deep2.py

# Figure 7
python3.4 plot_dust_mass_plane.py

# Figure 11, NZ

# Figure 14 
python3.4 plot_SNMED_uncertainty.py


# figures 18,19
python3.4 plot_distribution_metals.py
python3.4 plot_distribution_ages.py


# Figure 1 
# first row
python3.4 object_types_mass.py
# second row
python3.4 object_types_SNMEDIANALL.py
# Creates figure 3 about sigma_m and SNR per pixel
python pdf_SM_error.py


# Figures comparing all the parameters

# previous figures
python3.4 plot_distribution_masses.py
python3.4 plot_distribution_ebv.py
python3.4 plot_distribution_ages.py
python3.4 plot_distribution_masses_imf_diff.py
python3.4 plot_age_metal_plane.py
python3.4 plot_distribution_metals.py
python3.4 plot_differences_age.py


python3.4 plot_distribution_ebv.py
python3.4 plot_differences_ebv.py




# copy figures to the public repo

#rm /home/comparat/wwwDir/firefly_data/dr14/v1_1_0/plots/*.png
#cp /data36s/comparat/spm/results/mass-redshift-presentation/*.png /home/comparat/wwwDir/firefly_data/dr14/v1_1_0/plots/
#cp /data36s/comparat/spm/results/mass-snr/*.png /home/comparat/wwwDir/firefly_data/dr14/v1_1_0/plots/

# Stellar maa functions
cd /home/comparat/software/linux/firefly_explore/bin/bin_SMF

# Figure 4, stellar mass functions probed by SDSS and BOSS and DEEP2 in different redshift bins
python2 smf_sdss_eboss.py 0.2 0.5
python2 smf_sdss_eboss.py 0.5 0.8
python2 smf_sdss_eboss.py 0.8 1.1

# Figure 5 stellar mass functions probed by [OII] emitters in DEEP2.
python smf_plot.py 0.78 0.83 41.8
python smf_plot.py 0.83 1.03 41.8

#chmod o+r /data42s/comparat/firefly/v1_1_0/figures/*

