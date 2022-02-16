# -*- coding: utf-8 -*-
################################################################
# #
# Seth Cram #
# ECE351-53 #
# Project 4 #
# Due: 2/22/2022 #
# Any other necessary information needed to navigate the file #
#  
#
################################################################

import numpy
import matplotlib.pyplot as plt
import scipy.signal as sig #cant just import scipy
from step_and_ramp import u


L = 27e-3 #27*10^-3
R = 1000
C = 100e-9 #100*10^-9

steps = 1e-8 # Define step size
#s = numpy.arange(0, 0.0012 + steps , steps)
 
#H_s = L*s / (L*s + R*(1+L*C*s^2)) #what def 's' as?

#h_t1 = scipy.signal.impules( H_s )

num = [0, L, 0]
denom = [R*L*C, L, R]

t = numpy.arange(0, 1.2e-3 + steps , steps)

#gives output y and ouput t, so use for graphing:
tout, yout = sig.impulse( (num, denom), T = t)

#h_t2 = 0.02796*numpy.exp(-5000*t)*numpy.sin(18584.14*t + 105.06) * u(t)
h_t2 = 10000*numpy.exp(-5000*t)*(numpy.cos(18584*t) - 0.269*numpy.sin(18584*t))

#PLOTS 
    
#plot1:
plt.figure(figsize = (10,15)) #1st arg = horizontal space, 2nd arg = vertical space
plt.subplot(2, 1, 1)
plt.plot(tout, yout) 
plt.grid() #add a grid to graph
plt.title('Library Impulse Response')
plt.ylabel('h(t)')

#plot2:
plt.subplot(2, 1, 2)
plt.plot(t, h_t2)
plt.grid() #add a grid to graph
plt.title('Hand-Calculated Impulse Response')
plt.ylabel('h(t)')
plt.xlabel('t')

plt.show() #display figure

#STEP RESPONSE

tout, yout = sig.step( (num, denom), T = t)

h_t2 = numpy.full(t.shape, 0) #ph for calc'd val

#PLOTS 
    
#plot1:
plt.figure(figsize = (10,15)) #1st arg = horizontal space, 2nd arg = vertical space
plt.plot(tout, yout) 
plt.grid() #add a grid to graph
plt.title('Library Step Response of H(s)')
plt.ylabel('h(t)')
plt.xlabel('t')

plt.show() #display figure


