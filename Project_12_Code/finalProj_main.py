# -*- coding: utf-8 -*-
################################################################
# #
# Seth Cram #
# ECE351-53 #
# Project 11 #
# Due: 4/26/2022 #
# Any other necessary information needed to navigate the file #
#  
#
################################################################

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from proj9_main import myfft, clean_myfft
import pandas as pd

#load input sig:
df = pd.read_csv('NoisySignal.csv')

t = df['0'].values
sensor_sig = df['1'].values

plt.figure(figsize = (10, 7))
plt.plot(t, sensor_sig)
plt.grid()
plt.title('Noisy Input Signal')
plt.xlabel('Time [s]')
plt.ylabel('Ampltiude [V]')
plt.show()

#our code starts here:
  
fs = 1e6

    
(sensor_mag, X_phi, freq) = clean_myfft(sensor_sig, fs)


#stem plotting funct:
def make_stem(ax, x, y, color = 'k', 
              style = 'solid', label = '', linewidths = 2.5, **kwargs):
    ax.axhline(x[0], x[-1], 0, color = 'r')
    ax.vlines(x, 0, y, color = color,
              linestyles = style, label = label, linewidths = linewidths)
    ax.set_ylim([1.05*y.min(), 1.05*y.max()])

 
#Overall plot:
#to use the funct as a single plot:
fig , ax = plt . subplots ( figsize =(10 , 7) )
plt.title('Magnitude plot of sensor_sig')
make_stem ( ax , freq , sensor_mag )
plt.ylabel('Magnitude (V)')
plt.xlabel('Freq (Hz)')
#can change to narrow in on different sections
plt.xlim(0, 120000) #bc care ab around 0, cant have neg freqs, and after 100,000
plt.show ()

#first req = attenuate desired freq less than -0.3dB
fig , ax = plt . subplots ( figsize =(10 , 7) )
plt.title('Magnitude plot of sensor_sig')
make_stem ( ax , freq , sensor_mag )
plt.ylabel('Magnitude (V)')
plt.xlabel('Freq (Hz)')
#can change to narrow in on different sections
plt.xlim(1800, 2000) 
plt.show ()

#second req = attenuate atleast -30dB around 0
fig , ax = plt . subplots ( figsize =(10 , 7) )
plt.title('Magnitude plot of sensor_sig')
make_stem ( ax , freq , sensor_mag )
plt.ylabel('Magnitude (V)')
plt.xlabel('Freq (Hz)')
#can change to narrow in on different sections
plt.xlim(0, 1000) 
plt.show ()

#third req = attenuate atleast -30dB around 0
fig , ax = plt . subplots ( figsize =(10 , 7) )
plt.title('Magnitude plot of sensor_sig')
make_stem ( ax , freq , sensor_mag )
plt.ylabel('Magnitude (V)')
plt.xlabel('Freq (Hz)')
#can change to narrow in on different sections
plt.xlim(2000, 100000) 
plt.show ()

#Fourth req = The switching amplifier noise must be attenuated by at least -21dB
fig , ax = plt . subplots ( figsize =(10 , 7) )
plt.title('Magnitude plot of sensor_sig')
make_stem ( ax , freq , sensor_mag )
plt.ylabel('Magnitude (V)')
plt.xlabel('Freq (Hz)')
#can change to narrow in on different sections
plt.xlim(100000, 150000) 
plt.show ()



"""#for mult subplots: (doesnt work)
fig, ( ax1, ax2 ) = plt.subplots (2 , 1 , figsize =(10 , 7) )
#plt.title('Magnitude plot of sensor_sig')
plt.subplot ( ax1 )
make_stem(ax1, freq, sensor_mag)
plt.subplot ( ax2 )
make_stem ( ax2 , freq , sensor_mag )
#plt.ylabel('Magnitude')
#plt.xlabel('Freq (Hz)')
#can change to narrow in on different sections
plt.xlim(1800, 2000)
plt.show()
"""

#bode plot

#default vals

#original:
#R = 1000
#L = 27e-3
#C = 100e-9

#works in rad/s:
#R = 7500
#L = 2700e-3
#C = 100e-9

#works in Hz:
R = 5
L = 1e-3 
C = 8e-6

num = [1/(R*C), 0]
denom = [1, 1/(R*C), 1/(L*C)]

syst = sig.lti(num,denom)

steps = 100 #decrease for better resolution
#in rad/s (DONT USE 1**3 AS ARG (fails))
w = np.arange(1, 1e6*2*np.pi+steps, steps)

(bodeW, bodeMag, bodePhase) = sig.bode(syst, w)

#doesn't work: bodeW = np.rad2deg(bodeW)

#conv rad/s to Hz:
bodeW = bodeW / (2*np.pi)

#PLOTS

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

#plot1:    

plt.rc('font', **font)    
plt.figure(figsize = (30,30))
plt.subplot(2, 1, 1)
plt.semilogx(bodeW, bodeMag)
plt.grid(True, which='both', ls='-')
# plt.grid() #add a grid to graph
plt.title('Bode plot for H(s)')
plt.ylabel('|H(jw)| (dB)')

#plot2:    
    
plt.subplot(2, 1, 2)
plt.semilogx(bodeW, bodePhase)
plt.grid() #add a grid to graph
plt.ylabel('angle of H(jw) (degs)')
plt.xlabel('w (Hz)')  

plt.show() #display figure

#first req = attenuate desired freqa less than -0.3dB
plt.rc('font', **font)    
plt.figure(figsize = (30,30))
plt.semilogx(bodeW, bodeMag)
plt.grid() #add a grid to graph
plt.title('Bode plot for H(s) (positional measurement)')
plt.xlim(0, 1800)
plt.ylabel('|H(jw)| (dB)')
plt.xlabel('w (Hz)')  

#second req = attenuate desired freqa less than -0.3dB
plt.rc('font', **font)    
plt.figure(figsize = (30,30))
plt.semilogx(bodeW, bodeMag)
plt.grid() #add a grid to graph
plt.title('Bode plot for H(s) (positional measurement)')
plt.xlim(1800, 2000)
plt.ylim(-1, 0)
plt.ylabel('|H(jw)| (dB)')
plt.xlabel('w (Hz)')  

#third req = attenuate atleast -30dB around 0
plt.rc('font', **font)    
plt.figure(figsize = (30,30))
plt.plot(bodeW, bodeMag)
plt.grid() #add a grid to graph
plt.title('Bode plot for H(s) (switching amplifier noise)')
plt.xlim(2000, 100000)
plt.ylabel('|H(jw)| (dB)')
plt.xlabel('w (Hz)')  

#fourth req = attenuate a ton by 100kHz
plt.rc('font', **font)    
plt.figure(figsize = (30,30))
plt.semilogx(bodeW, bodeMag)
plt.grid() #add a grid to graph
plt.title('Bode plot for H(s) (frequencies greater than 100kHz)')
plt.xlim(100000, 150000)
plt.ylabel('|H(jw)| (dB)')
plt.xlabel('w (Hz)')  


#fs = 500000

#conv H(s) to z-dom
(zNum, zDenom) = sig.bilinear(num, denom, fs) #last arg was 500000

# pass sensor_sig thru z-dom filter
y = sig.lfilter(zNum, zDenom, sensor_sig)

(Y_mag, Y_phi, freq) = clean_myfft(y, fs)

#plot:
plt.figure(figsize = (15,15))
plt.plot(t, y)
plt.grid() #add a grid to graph
plt.title('filtered Y_sig vs t')
plt.ylabel('y(t)')
plt.xlabel('t (s)')

plt.show() #display figure

#Overall plot:
#to use the funct as a single plot:
fig , ax = plt . subplots ( figsize =(10 , 7) )
plt.title('Magnitude plot of sensor_sig')
make_stem ( ax , freq , Y_mag )
plt.ylabel('Magnitude (V)')
plt.xlabel('Freq (Hz)')
#can change to narrow in on different sections
plt.xlim(0, 120000) #bc care ab around 0, cant have neg freqs, and after 100,000
plt.show ()

#first req = attenuate desired freq less than -0.3dB
fig , ax = plt . subplots ( figsize =(10 , 7) )
plt.title('Magnitude plot of Y_sig')
make_stem ( ax , freq , Y_mag )
plt.ylabel('Magnitude (V)')
plt.xlabel('Freq (Hz)')
#can change to narrow in on different sections
plt.xlim(1800, 2000) 
plt.show ()

#second req = attenuate atleast -30dB around 0
fig , ax = plt . subplots ( figsize =(10 , 7) )
plt.title('Magnitude plot of Y_sig')
make_stem ( ax , freq , Y_mag )
plt.ylabel('Magnitude (V)')
plt.xlabel('Freq (Hz)')
#can change to narrow in on different sections
plt.xlim(0, 1000) 
plt.show ()

#third req = attenuate atleast -30dB around 0
fig , ax = plt . subplots ( figsize =(10 , 7) )
plt.title('Magnitude plot of Y_sig')
make_stem ( ax , freq , Y_mag )
plt.ylabel('Magnitude (V)')
plt.xlabel('Freq (Hz)')
#can change to narrow in on different sections
plt.xlim(2000, 100000) 
plt.show ()

#Fourth req = The switching amplifier noise must be attenuated by at least -21dB
fig , ax = plt . subplots ( figsize =(10 , 7) )
plt.title('Magnitude plot of Y_sig')
make_stem ( ax , freq , Y_mag )
plt.ylabel('Magnitude (V)')
plt.xlabel('Freq (Hz)')
#can change to narrow in on different sections
plt.xlim(100000, 150000) 
plt.ylim(0, 0.2)
plt.show ()

