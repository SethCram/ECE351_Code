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
from scipy.fftpack import fft, fftshift

#Fast Fourier Transform: (x = signal, fs = sampling frequency of input signal)
def myfft(x, fs):
    N = len( x ) # find the length of the signal
    X_fft = fft ( x ) # perform the fast Fourier transform (fft)
    X_fft_shifted = fftshift ( X_fft ) # shift zero frequency components
        # to the center of the spectrum
    freq = np . arange ( - N /2 , N /2) * fs / N # compute the frequencies for the output
        # signal , (fs is the sampling frequency and
        # needs to be defined previously in your code)
    X_mag = np .abs( X_fft_shifted ) / N # compute the magnitudes of the signal
    X_phi = np . angle ( X_fft_shifted ) # compute the phases of the signal
    
    return (X_mag, X_phi, freq)

def clean_myfft(x, fs):
    N = len( x ) # find the length of the signal
    X_fft = fft ( x ) # perform the fast Fourier transform (fft)
    X_fft_shifted = fftshift ( X_fft ) # shift zero frequency components
        # to the center of the spectrum
    freq = np . arange ( - N /2 , N /2) * fs / N # compute the frequencies for the output
        # signal , (fs is the sampling frequency and
        # needs to be defined previously in your code)
    X_mag = np .abs( X_fft_shifted ) / N # compute the magnitudes of the signal
    X_phi = np . angle ( X_fft_shifted ) # compute the phases of the signal
    
    i = 0
    
    #added to make phase plots readable:
    while( i < len(X_mag)): # walk thru X_mag arr
        if( X_mag[i] < 1e-10 ): # if magnitude super small
            X_phi[i] = 0 # zero out its phase
        i += 1
    
    return (X_mag, X_phi, freq)
"""
fs = 1000

steps = 1/fs
t = np.arange(0, 2, steps)

x = np.cos(2*np.pi*t) #w_0 != fs
(X_mag, X_phi, freq) = myfft(x, fs)

x1 = 5*np.sin(2*np.pi*t)
(X1_mag, X1_phi, freq1) = myfft(x1, fs)

x2 = 2*np.cos((2*np.pi*2*t)-2) + np.sin((2*np.pi*6*t)+3)**2
(X2_mag, X2_phi, freq2) = myfft(x2, fs)

#PLOTS 

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

#plot1:    

plt.rc('font', **font)
plt.figure(figsize = (30,30))
plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.grid() #add a grid to graph
plt.title('cos(2πt)')
plt.ylabel('x(t)')
plt.xlabel("time (s)")    

plt.subplot(3, 2, 3)
plt.stem ( freq , X_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.title('Magnitude plot of cos(2πt)')
plt.ylabel('Magnitude')

plt.subplot(3, 2, 4)
plt.stem ( freq , X_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Magnitude plot of cos(2πt)')

plt.subplot(3, 2, 5)
plt.stem ( freq , X_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
plt.title('Phase plot of cos(2πt)')
plt.ylabel('Phase')
plt.xlabel("frequency (Hz)")

plt.subplot(3, 2, 6)
plt.stem ( freq , X_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Phase plot of cos(2πt)')
plt.xlabel("frequency (Hz)")

plt.show() #display figure

#plot2:

plt.figure(figsize = (30,30))
plt.subplot(3, 1, 1)
plt.plot(t, x1)
plt.grid() #add a grid to graph
plt.title('5sin(2πt)')
plt.ylabel('x(t)')
plt.xlabel("time (s)")

plt.subplot(3, 2, 3)
plt.stem ( freq1 , X1_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.title('Magnitude plot of 5sin(2πt)')
plt.ylabel('Magnitude')

plt.subplot(3, 2, 4)
plt.stem ( freq1 , X1_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Magnitude plot of 5sin(2πt)')

plt.subplot(3, 2, 5)
plt.stem ( freq1 , X1_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
#plt.xlim(-20, 20)
plt.title('Phase plot of 5sin(2πt)')
plt.ylabel('Phase')
plt.xlabel("frequency (Hz)")

plt.subplot(3, 2, 6)
plt.stem ( freq1 , X1_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Phase plot of 5sin(2πt)')
plt.xlabel("frequency (Hz)")

plt.show() #display figure

#plot3:
    
plt.figure(figsize = (30,30))
plt.subplot(3, 1, 1)
plt.plot(t, x2)
plt.grid() #add a grid to graph
plt.title('2cos((2π · 2t) − 2) + sin2((2π · 6t) + 3)^2')
plt.ylabel('x(t)')
plt.xlabel("time (s)")

plt.subplot(3, 2, 3)
plt.stem ( freq2 , X2_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.title('Magnitude plot of 2cos((2π · 2t) − 2) + sin2((2π · 6t) + 3)^2')
plt.ylabel('Magnitude')

plt.subplot(3, 2, 4)
plt.stem ( freq2 , X2_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Magnitude plot of 2cos((2π · 2t) − 2) + sin2((2π · 6t) + 3)^2')

plt.subplot(3, 2, 5)
plt.stem ( freq2 , X2_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
plt.title('Phase plot of 2cos((2π · 2t) − 2) + sin2((2π · 6t) + 3)')
plt.ylabel('Phase')
plt.xlabel("frequency (Hz)")

plt.subplot(3, 2, 6)
plt.stem ( freq2 , X2_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Phase plot of 2cos((2π · 2t) − 2) + sin2((2π · 6t) + 3)')
plt.ylabel('Phase')
plt.xlabel("frequency (Hz)")

plt.show() #display figure


(X_mag, X_phi, freq) = clean_myfft(x, fs)


(X1_mag, X1_phi, freq1) = clean_myfft(x1, fs)


(X2_mag, X2_phi, freq2) = clean_myfft(x2, fs)

#PLOTS 

#plot1:

plt.figure(figsize = (30,30))
plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.grid() #add a grid to graph
plt.title('Clean cos(2πt)')
plt.ylabel('x(t)')
plt.xlabel("time (s)")    

plt.subplot(3, 2, 3)
plt.stem ( freq , X_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.title('Magnitude plot of cos(2πt)')
plt.ylabel('Magnitude')

plt.subplot(3, 2, 4)
plt.stem ( freq , X_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Magnitude plot of cos(2πt)')

plt.subplot(3, 2, 5)
plt.stem ( freq , X_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
plt.title('Phase plot of cos(2πt)')
plt.ylabel('Phase')
plt.xlabel("frequency (Hz)")

plt.subplot(3, 2, 6)
plt.stem ( freq , X_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Phase plot of cos(2πt)')
plt.xlabel("frequency (Hz)")

plt.show() #display figure

#plot2:

plt.figure(figsize = (30,30))
plt.subplot(3, 1, 1)
plt.plot(t, x1)
plt.grid() #add a grid to graph
plt.title('Clean 5sin(2πt)')
plt.ylabel('x(t)')
plt.xlabel("time (s)")

plt.subplot(3, 2, 3)
plt.stem ( freq1 , X1_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.title('Magnitude plot of 5sin(2πt)')
plt.ylabel('Magnitude')

plt.subplot(3, 2, 4)
plt.stem ( freq1 , X1_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Magnitude plot of 5sin(2πt)')

plt.subplot(3, 2, 5)
plt.stem ( freq1 , X1_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
#plt.xlim(-20, 20)
plt.title('Phase plot of 5sin(2πt)')
plt.ylabel('Phase')
plt.xlabel("frequency (Hz)")

plt.subplot(3, 2, 6)
plt.stem ( freq1 , X1_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Phase plot of 5sin(2πt)')
plt.xlabel("frequency (Hz)")

plt.show() #display figure

#plot3:
    
plt.figure(figsize = (30,30))
plt.subplot(3, 1, 1)
plt.plot(t, x2)
plt.grid() #add a grid to graph
plt.title('Clean 2cos((2π · 2t) − 2) + sin2((2π · 6t) + 3)^2')
plt.ylabel('x(t)')
plt.xlabel("time (s)")

plt.subplot(3, 2, 3)
plt.stem ( freq2 , X2_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.title('Magnitude plot of 2cos((2π · 2t) − 2) + sin2((2π · 6t) + 3)^2')
plt.ylabel('Magnitude')

plt.subplot(3, 2, 4)
plt.stem ( freq2 , X2_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Magnitude plot of 2cos((2π · 2t) − 2) + sin2((2π · 6t) + 3)^2')

plt.subplot(3, 2, 5)
plt.stem ( freq2 , X2_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
plt.title('Phase plot of 2cos((2π · 2t) − 2) + sin2((2π · 6t) + 3)^2')
plt.ylabel('Phase')
plt.xlabel("frequency (Hz)")

plt.subplot(3, 2, 6)
plt.stem ( freq2 , X2_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Phase plot of 2cos((2π · 2t) − 2) + sin2((2π · 6t) + 3)^2')
plt.ylabel('Phase')
plt.xlabel("frequency (Hz)")

plt.show() #display figure

#pass in time arr, period, and number of iterations: (square wave approx)
def x(t, T, N):
    #vars needed for loops:
    k = 1
    w_0 = 2 * np.pi / T
    
    #alloc enough space for x arr:
    x = np.zeros( t.shape)

    #sum for each time:
    while ( k <= N):
        x += 2/(k*np.pi)*(1-np.cos(k*np.pi))*np.sin(k*w_0*t)
        k = k + 1
        
    return x


t = np.arange(0, 16, steps)

x2 = x(t, 8, 15)
(X2_mag, X2_phi, freq2) = clean_myfft(x2, fs)


#plot7:
    
plt.figure(figsize = (30,30))
plt.subplot(3, 1, 1)
plt.plot(t, x2)
plt.grid() #add a grid to graph
plt.title('Clean Square Wave (N=15)')
plt.ylabel('x(t)')
plt.xlabel("time (s)")

plt.subplot(3, 2, 3)
plt.stem ( freq2 , X2_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.title('Magnitude plot')
plt.ylabel('Magnitude')

plt.subplot(3, 2, 4)
plt.stem ( freq2 , X2_mag ) # you will need to use stem (i.e. matplotlib.pyplot.stem()) to get these plots to be
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Magnitude plot')

plt.subplot(3, 2, 5)
plt.stem ( freq2 , X2_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
plt.title('Phase plot')
plt.ylabel('Phase')
plt.xlabel("frequency (Hz)")

plt.subplot(3, 2, 6)
plt.stem ( freq2 , X2_phi ) # correct , remember to label all plots appropriately
plt.grid() #add a grid to graph
plt.xlim(-2, 2)
plt.title('Phase plot')
plt.ylabel('Phase')
plt.xlabel("frequency (Hz)")

plt.show() #display figure
"""