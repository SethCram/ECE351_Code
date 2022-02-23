# -*- coding: utf-8 -*-
################################################################
# #
# Seth Cram #
# ECE351-53 #
# Project 6 #
# Due: 3/01/2022 #
# Any other necessary information needed to navigate the file #
#  
#
################################################################

import numpy
import matplotlib.pyplot as plt
import scipy.signal as sig #cant just import scipy
from step_and_ramp import u

steps = 1e-3 # Define step size
t = numpy.arange(0, 2 + steps , steps)

#prelab funct:
y1 = ( 0.5-0.5*numpy.exp(-4*t)+numpy.exp(-6*t) ) * u(t)

#step response using lib

#from prelab:
num = [1, 6, 12] #okay if deg of num = deg of denom?
denom = [1, 10, 24]    
    
tout, yout = sig.step( (num, denom), T = t)


#PLOTS 
    
#plot1:
plt.figure(figsize = (10,15)) #1st arg = horizontal space, 2nd arg = vertical space
plt.subplot(2, 1, 1)
plt.plot(t, y1) 
plt.grid() #add a grid to graph
plt.title('Prelab y(t) vs t')
plt.ylabel('y(t)')

#plot2:
plt.subplot(2, 1, 2)
plt.plot(tout, yout)
plt.grid() #add a grid to graph
plt.title('library y(t) vs t')
plt.ylabel('y(t)')
plt.xlabel('t')

plt.show() #display figure

#Partial Fraction

num = [0, 1, 6, 12 ]
denom = [ 1, 10, 24, 0 ]

# r = Residues corresponding to the poles (coeffs on s-vals)
# p = Poles ordered by magnitude in ascending order. (s vals applied to get the coeffs)
# k = Coefficients of the direct polynomial term.

[r_in, p_in, k_in] = sig.residue( num, denom )

print("partial fraction results: ", r_in)

print("Corresponding poles: ", p_in)

print("Coeffs of the direct polynomial terms: ", k_in)

#New Function

#taken from converting given syst to s-dom, then taking step response:
num = [25250]
denom = [1, 18, 218, 2036, 9085, 25250, 0]

[r_in, p_in, k_in] = sig.residue( num, denom )

print("partial fraction results: ", r_in)

print("Corresponding poles: ", p_in)

print("Coeffs of the direct polynomial terms: ", k_in)


#STEP RESPONSE

t = numpy.arange(0, 4.5 + steps , steps)

#use the sin method using the results:
#y1 = u(t)*(1 - 0.2146*numpy.exp(-10*t) + 156.594*numpy.exp(-3*t)*numpy.sin(4*t - numpy.radians(156.615)) + 18.675*numpy.exp(-1*t)*numpy.sin(10*t - numpy.radians(143.723))) #angle needs to be in rads for numpy.sin()

def cos_method(r, p, t):
    y = 0;
    for i in range(0, len(r)):
        kmag = numpy.absolute(r[i])
        kang = numpy.angle(r[i])
        alpha = numpy.real(p[i])
        omega = numpy.imag(p[i])
        y += kmag*numpy.exp(alpha*t)*numpy.cos(omega*t+kang)*u(t) #used to be mult'd by 2 but taken out bc didnt line up w/ expected
    return y

y1 = cos_method(r_in, p_in, t)

#H(s):
num = [25250]
denom = [1, 18, 218, 2036, 9085, 25250]

tout, yout = sig.step( (num, denom), T = t)

#PLOTS 
    
#plot1:
plt.figure(figsize = (10,15)) #1st arg = horizontal space, 2nd arg = vertical space
plt.subplot(2, 1, 1)
plt.plot(t, y1) 
plt.grid() #add a grid to graph
plt.title('My funct y(t) vs t')
plt.ylabel('y(t)')

#plot2:
plt.subplot(2, 1, 2)
plt.plot(tout, yout)
plt.grid() #add a grid to graph
plt.title('library y(t) vs t')
plt.ylabel('y(t)')
plt.xlabel('t')

plt.show() #display figure
