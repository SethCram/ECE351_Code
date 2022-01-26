# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:10:36 2022

@author: crazy
"""

################################################################
# #
# Seth Cram #
# ECE351-53 #
# Lab 2 part 1 #
# Due: 1/25/2022 #
# Any other necessary information needed to navigate the file #
#  
#
################################################################

import numpy
import matplotlib.pyplot as plt

#cos plotting funct:
def func1(t): #arg is step size
    y = numpy.zeros(t.shape) #init y to array of zeros w/ same # of entries as t
    
    for i in range(len(t)): #run loop once each step
        y[i] = numpy.cos(t[i]) #fill y w/ cos() evaluation at each step
    return y

#check args: print(plt.rcParams.keys())

params = {'axes.labelsize': 15,'axes.titlesize':15, 'xtick.labelsize': 12, 'ytick.labelsize': 12}
plt.rcParams.update (params) # Set font size in plots

steps = 1e-2 # Define step size
t = numpy.arange(0, 10 + steps , steps) #create array of steps 0-10

#test: print("t: ", t)

y = func1(t)
    
#plot:
plt.figure(figsize = (10,7))
plt.plot(t, y) # t = step size, smaller it is the more accurate graph is
                # y = array of cos vals at each step
plt.grid() #add a grid to graph
plt.title('Cosine Function')
plt.ylabel('y(t)')
plt.xlabel('t')
plt.show() #print plot



