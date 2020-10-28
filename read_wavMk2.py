#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:04:38 2020

@author: nikkoangelo
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as s

from scipy.io.wavfile import read

filename = 'L5_499kOhm_40s.wav'
wave = read(filename)[1]
fs = read(filename)[0]


Time = np.linspace(0, len(wave) / fs, num=len(wave))

plt.title(filename + ' time trace')
plt.xlabel('time[s]')
plt.ylabel('Amplitude[V]')

plt.plot(Time,wave)
