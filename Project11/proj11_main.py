# -*- coding: utf-8 -*-
################################################################
# #
# Seth Cram #
# ECE351-53 #
# Project 11 #
# Due: 4/12/2022 #
# Any other necessary information needed to navigate the file #
#  
#
################################################################

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from zplane import zplane

#TASK 1
H_zNum = [2, -40, 0]
H_zDenom = [1, -10, 16]

#TASK 2
#h_k = 4

#TASK 3
(res, poles, k) = sig.residuez(H_zNum, H_zDenom)
print("residue: ", res)
print("poles: ", poles)
print("k: ", k)

#emptry space
print()

#TASK 4 (pole zero plots) (auto plotted)
(z, p, k2) = zplane(H_zNum, H_zDenom)
print("z: ", z)
print("p: ", p)
print("k: ", k2)

#TASK 5 (h = complex number)
(w, h) = sig.freqz( H_zNum, H_zDenom, whole = True)

#find magnitude in dB and phase in degs:
mag = 20*np.log10( np.abs(h) )
phase = np.angle(h, deg = True)

#PLOTS

font = {'weight' : 'bold',
        'size'   : 22}

#plot1:    

plt.rc('font', **font)    
plt.figure(figsize = (30,30))
plt.subplot(2, 1, 1)
#plt.semilogx(w, mag)
plt.plot(w, mag)
plt.grid() #add a grid to graph
plt.title('Response of H(z)')
plt.ylabel('|H(z)| (dB)')

#plot2:    
    
plt.subplot(2, 1, 2)
#plt.semilogx(w, phase)
plt.plot(w, phase)
plt.grid() #add a grid to graph
plt.ylabel('angle of H(z) (degs)')
plt.xlabel('w (rads/sample)')  

plt.show() #display figure

