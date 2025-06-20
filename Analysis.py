import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt
from FreeTrace.module.data_load import read_csv, read_multiple_csv

trajectory_data = read_csv(file='/home/adrien/RESULT-crop/RESULT/crop_inside_250509_U2OS-53BP1Halo_50nM_cell21_10ms_irra40mins007_traces.csv')
#trajectory_data = read_multiple_csv('outputs')
trajectory_data["z"] = 0.0
trajectory_data

import seaborn as sns
import matplotlib.pyplot as plt
from FreeTrace.module.preprocessing import simple_preprocessing

"""
Option settings for data analysis.
"""
PIXELMICRONS = 0.16
FRAMERATE = 0.01
CUTOFF = 3  # miminum length of trajectory to conisder for the analysis.
number_of_bins = 50
figure_resolution_in_dpi = 200
figure_font_size = 20


"""
preprocessing generates 4 data.
@params: data folder path, pixel microns, frame rate, cutoff
@output: Analysis_data1(pd.DataFrame), Analysis_data2(pd.DataFrame), MSD(pd.DataFrame), TAMSD(pd.DataFrame)

Simple_preprocessing includes below steps.
1. exclude the trajectory where length is shorter than CUTOFF
2. convert from pixel unit to micrometer unit with PIXELMICRONS and FRAMERATE
3. generate 4 DataFrames.
"""
analysis_data1, analysis_data2, analysis_data3, msd, tamsd = simple_preprocessing(data=trajectory_data,
                                                                                  pixelmicrons=PIXELMICRONS,
                                                                                  framerate=FRAMERATE,
                                                                                  cutoff=CUTOFF)

print(f'\nanalysis_data1:\n', analysis_data1)
print(f'\nanalysis_data2:\n', analysis_data2)
print(f'\nanalysis_data3:\n', analysis_data3)
print(f'\nMSD:\n', msd)
print(f'\nEnsemble-averaged TAMSD:\n', tamsd)