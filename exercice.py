# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 18:59:33 2018

@author: vittorio
"""

import numpy as np
import matplotlib.pyplot as plt

x,y=np.loadtxt('data.txt',delimiter=None, unpack=True, skiprows=1)
plt.plot(x,y)
plt.xlabel('time')
plt.ylabel('counts/s')
plt.show()

