# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 21:54:37 2022

@author: amijo
"""

import numpy as np
import matplotlib.pyplot as plt
f = 20
t = np.linspace(-10,10,100)
bh = np.zeros(len(t))
for n in range (1,1001,2):
      bh = bh + (4/(n*np.pi))*np.sin(2*np.pi*f*n*t);
      print(n)
plt.plot(t, bh);
plt.show();
