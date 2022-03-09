# -*- coding: utf-8 -*-
################################################################
# #
# Seth Cram #
# ECE351-53 #
# Project 8 #
# Due: 3/15/2022 #
# Any other necessary information needed to navigate the file #
#  
#
################################################################

import numpy
import matplotlib.pyplot as plt
import scipy.signal as sig #cant just import scipy
import scipy 

print("When k = 0 or 1, a_k = ", 0)

k = 1
b_k = 1/(k*numpy.pi)*(1-numpy.cos(k*numpy.pi))
print("When k=1, b_k = ", b_k)
k = 2
b_k = 1/(k*numpy.pi)*(1-numpy.cos(k*numpy.pi))
print("When k=2, b_k = ", b_k)
k = 3
b_k = 1/(k*numpy.pi)*(1-numpy.cos(k*numpy.pi))
print("When k=3, b_k = ", b_k)

#pass in time arr, period, and number of iterations:
def x(t, T, N):
    #vars needed for loops:
    k = 1
    w_0 = 2 * numpy.pi / T
    i = 0
    
    #alloc enough space for x arr:
    x = numpy.zeros( t.shape)

    #sum for each time:
    while ( k <= N):
        x += 2/(k*numpy.pi)*(1-numpy.cos(k*numpy.pi))*numpy.sin(k*w_0*t)
        k = k + 1
        
    return x

steps = 13e-3

t = numpy.arange(0, 20 + steps , steps)

x1 = x(t, 8, 1)
x2 = x(t, 8, 3)
x3 = x(t, 8, 15)
x4 = x(t, 8, 50)
x5 = x(t, 8, 150)
x6 = x(t, 8, 1500)

#PLOTS 

#plot:
plt.figure(figsize = (10,15))
plt.subplot(3, 1, 1)
plt.plot(t, x1)
plt.grid() #add a grid to graph
plt.title('Fourier Series Approx for N = 1')
plt.ylabel('x(t)')

plt.subplot(3, 1, 2)
plt.plot(t, x2)
plt.grid() #add a grid to graph
plt.title('Fourier Series Approx for N = 3')
plt.ylabel('x(t)')

plt.subplot(3, 1, 3)
plt.plot(t, x3)
plt.grid() #add a grid to graph
plt.title('Fourier Series Approx for N = 15')
plt.ylabel('x(t)')
plt.xlabel('t')

plt.show() #display figure


#plot:
plt.figure(figsize = (10,15))
plt.subplot(3, 1, 1)
plt.plot(t, x4)
plt.grid() #add a grid to graph
plt.title('Fourier Series Approx for N = 50')
plt.ylabel('x(t)')

plt.subplot(3, 1, 2)
plt.plot(t, x5)
plt.grid() #add a grid to graph
plt.title('Fourier Series Approx for N = 150')
plt.ylabel('x(t)')

plt.subplot(3, 1, 3)
plt.plot(t, x6)
plt.grid() #add a grid to graph
plt.title('Fourier Series Approx for N = 1500')
plt.ylabel('x(t)')
plt.xlabel('t')

plt.show() #display figure
