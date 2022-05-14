# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:52:48 2022

@author: codmusic
"""

import pyxdf
import matplotlib.pyplot as plt
import numpy as np

#data, header = pyxdf.load_xdf('C:\\Users\\codmusic\\Documents\\CurrentStudy\\sub-P001\\ses-S001\\eeg\\sub-P001_ses-S001_task-Default_run-001_eeg_old2.xdf')
data, header = pyxdf.load_xdf(r'C:\Users\codmusic\Documents\CurrentStudy\sub-P003\ses-S001\eeg\sub-P003_ses-S001_task-Default_run-001_eeg.xdf')
print(f'data specs{type(data)}')
print(f'data len{len(data)}')
print(data[0])
print("------------------------------------------------------------------")
print(data[1])
print("------------------------------------------------------------------")
print(data[2])
print(type(data[0]))
print(f'len dat0{len(data[0])}')
print(f'len dat0{len(data[1])}')
print(f'0 dict{data[0].keys()}')

for stream in data:
    y = stream['time_series']
    print(y.shape)
    i=0
    for z in y.T:
        print(f'Channel no.:{i}')
        print(f'channel valies{z[:20]}')
        i=i+1
    #print(f'y_dtype{y.dtype}')
    #print(f'y shape{y.shape}')
    #print(f'y type{type(y)}')
    #print (type(stream))
    #print (len(stream))
    # print (stream[:5])

    if isinstance(y, list):
        # list of strings, draw one vertical line for each marker
        for timestamp, marker in zip(stream['time_stamps'], y):
            plt.axvline(x=timestamp)
            print(f'Marker "{marker[0]}" @ {timestamp:.2f}s')
    elif isinstance(y, np.ndarray):
        # numeric data, draw as lines
        plt.plot(stream['time_stamps'], y)
    else:
        raise RuntimeError('Unknown stream format')

plt.show()