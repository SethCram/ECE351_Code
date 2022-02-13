# -*- coding: utf-8 -*-
################################################################
# #
# Seth Cram #
# ECE351-53 #
# Project 4 #
# Due: 2/15/2022 #
# Any other necessary information needed to navigate the file #
#  
#
################################################################

import numpy
import matplotlib.pyplot as plt

#import just the step function:
from step_and_ramp import u, r

#import my convolution funct:
from convolution import convolve


steps = 1e-2 # Define step size
t = numpy.arange(-10, 10 + steps , steps)

h1 = numpy.exp(-2*t) * ( u(t) - u(t-3) )

h2 = u(t-2)-u(t-6)

f0 = 0.25 #Hz
w0 = f0 * numpy.pi * 2 #convert to angular frequency
h3 = numpy.cos(w0*t) * u(t)

#PLOTS 
    
#plot1:
plt.figure(figsize = (10,15)) #1st arg = horizontal space, 2nd arg = vertical space
plt.subplot(3, 1, 1)
plt.plot(t, h1) 
plt.grid() #add a grid to graph
plt.title('h1(t) vs t')
plt.ylabel('h1(t)')

#plot2:
plt.subplot(3, 1, 2)
plt.plot(t, h2)
plt.grid() #add a grid to graph
plt.title('h2(t) vs t')
plt.ylabel('h2(t)')

#plot3:
plt.subplot(3, 1, 3)
plt.plot(t, h3)
plt.grid() #add a grid to graph
plt.title('h3(t) vs t')
plt.ylabel('h3(t)')
plt.xlabel('t')

plt.show() #display figure

#STEP RESPONSE

conv_h1 = numpy.convolve(h1, u(t))

conv_h2 = numpy.convolve(h2, u(t))

conv_h3 = numpy.convolve(h3, u(t))

#PLOTS 

steps = 1e-2 / 2 # Define step size
calcT = numpy.arange(-10, 10+steps, steps)
t = calcT[0:len(calcT)-1] #cutoff the last val
    
#plot1:
plt.figure(figsize = (10,15)) #1st arg = horizontal space, 2nd arg = vertical space
plt.subplot(3, 1, 1)
plt.plot(t, conv_h1) 
plt.grid() #add a grid to graph
plt.title('h1(t) step response')
plt.ylabel('h1(t)')

#plot2:
plt.subplot(3, 1, 2)
plt.plot(t, conv_h2)
plt.grid() #add a grid to graph
plt.title('h2(t) step response')
plt.ylabel('h2(t)')

#plot3:
plt.subplot(3, 1, 3)
plt.plot(t, conv_h3)
plt.grid() #add a grid to graph
plt.title('h3(t) step response')
plt.ylabel('h3(t)')
plt.xlabel('t')

plt.show() #display figure

# HAND CALCS:
    
steps = 1e-2 # Define step size
t = numpy.arange(-10, 10 + steps , steps)

hconv_h1 = 0.5 * (-1*numpy.exp(-2*t)+1) * u(t) - 0.5 * (-1*numpy.exp(-2*(t-3))+1) * u(t-3)

hconv_h2 = (t-2) * u(t-2) - (t-6) * u(t-6)

hconv_h3 = 0.63662 * numpy.sin(1.5708*t) * u(t)

#PLOTS

"""
steps = 1e-2 / 2 # Define step size
calcT = numpy.arange(-10, 10+steps, steps)
t = calcT[0:len(calcT)-1] #cutoff the last val
"""

#plot1:
plt.figure(figsize = (10,15)) #1st arg = horizontal space, 2nd arg = vertical space
plt.subplot(3, 1, 1)
plt.plot(t, hconv_h1) 
plt.grid() #add a grid to graph
plt.title('h1(t) step response')
plt.ylabel('h1(t)')

#plot2:
plt.subplot(3, 1, 2)
plt.plot(t, hconv_h2)
plt.grid() #add a grid to graph
plt.title('h2(t) step response')
plt.ylabel('h2(t)')

#plot3:
plt.subplot(3, 1, 3)
plt.plot(t, hconv_h3)
plt.grid() #add a grid to graph
plt.title('h3(t) step response')
plt.ylabel('h3(t)')
plt.xlabel('t')

plt.show() #display figure
