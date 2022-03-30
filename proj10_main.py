# -*- coding: utf-8 -*-
################################################################
# #
# Seth Cram #
# ECE351-53 #
# Project 9 #
# Due: 3/29/2022 #
# Any other necessary information needed to navigate the file #
#  
#
################################################################

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import control as con

#default vals
R = 1000
L = 27e-3
C = 100e-9

steps = 1000
#in rad/s (DONT USE 1**3 AS ARG (fails))
w = np.arange(1e3, 1e6+steps, steps) 

#TASK 1.1

#prelab eqts
mag = (w/(R*C)) / np.sqrt(w**4 + ((1/(R*C))**2 - 2/(L*C))*(w**2) + (1/(L*C))**2)
phase = np.pi/2 - np.arctan((w/(R*C)) / (-1*(w**2)+(1/(L*C))))

#conv to db and degs
dbMag = 20*np.log10(mag)
degPhase = np.rad2deg(phase)

#need to shift by 180 degs later half to make look better
i=0 
while(i < len(w)):
    if(degPhase[i] > 90):
        degPhase[i] -= 180
    i += 1

#TASK 1.2

num = [1/(R*C), 0]
denom = [1, 1/(R*C), 1/(L*C)]

syst = sig.lti(num,denom)

(bodeW, bodeMag, bodePhase) = sig.bode(syst, w)

#PLOTS

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

#plot1:    

plt.rc('font', **font)    
plt.figure(figsize = (30,30))
plt.subplot(2, 1, 1)
plt.semilogx(w, dbMag)
plt.grid() #add a grid to graph
plt.title('Bode plot for Task 1.1')
plt.ylabel('|H(jw)| (dB)')

#plot2:    
    
plt.subplot(2, 1, 2)
plt.semilogx(w, degPhase)
plt.grid() #add a grid to graph
plt.ylabel('angle of H(jw) (degs)')
plt.xlabel('w (rads/s)')  

plt.show() #display figure

#plot1:    

plt.rc('font', **font)    
plt.figure(figsize = (30,30))
plt.subplot(2, 1, 1)
plt.semilogx(bodeW, bodeMag)
plt.grid() #add a grid to graph
plt.title('Bode plot for Task 1.2')
plt.ylabel('|H(jw)| (dB)')

#plot2:    
    
plt.subplot(2, 1, 2)
plt.semilogx(bodeW, bodePhase)
plt.grid() #add a grid to graph
plt.ylabel('angle of H(jw) (degs)')
plt.xlabel('w (rads/s)')  

plt.show() #display figure

#TASK 1.3

sys3 = con.TransferFunction(num, denom)

plt.figure(figsize = (15,15))
#used _ = .... to suppress the output (function auto-plots)
_ = con.bode(sys3, w, dB = True, Hz = True, deg = True, plot = True)
plt.title('Bode plot for Task 1.3')


"""#(conMag, conPhase, conW) = con.bode(sys3, w, dB = True, Hz = True, deg = True, plot = True)
#plot1:    

plt.rc('font', **font)    
plt.figure(figsize = (30,30))
plt.subplot(2, 1, 1)
plt.semilogx(conW, conMag)
plt.grid() #add a grid to graph
plt.title('Bode plot for Task 1.3')
plt.ylabel('|H(jw)| (dB)')

#plot2:    
    
plt.subplot(2, 1, 2)
plt.semilogx(conW, conPhase)
plt.grid() #add a grid to graph
plt.ylabel('angle of H(jw) (degs)')
plt.xlabel('w (Hz)')  

plt.show() #display figure
"""

#TASK 2.1

#chosen as x(t)'s max w_0
fs = 2*np.pi*50000

steps = 1/fs
t = np.arange(0, 1e-2 + steps , steps)

x = np.cos(2*np.pi*100*t) + np.cos(2*np.pi*3024*t) + np.sin(2*np.pi*50000*t)

#plot:
plt.figure(figsize = (15,15))
plt.plot(t, x)
plt.grid() #add a grid to graph
plt.title('x(t) vs t')
plt.ylabel('x(t)')
plt.xlabel('t (s)')

plt.show() #display figure

#TASK 2.2: conv H(s) to z-dom
(zNum, zDenom) = sig.bilinear(num, denom, 500000)

#TASK 2.3: pass x(t) thru z-dom filter
y = sig.lfilter(zNum, zDenom, x)

#plot:
plt.figure(figsize = (15,15))
plt.plot(t, y)
plt.grid() #add a grid to graph
plt.title('y(t) vs t')
plt.ylabel('y(t)')
plt.xlabel('t (s)')

plt.show() #display figure
