# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 20:53:33 2022

"""
################################################################
# #
# Seth Cram #
# ECE351-53 #
# Lab 1 part 2#
# Due: 1/25/2022 #
# Any other necessary information needed to navigate the file #
#  
#
################################################################

import numpy
import scipy.signal
import time

#printing:
t = 1
print(t)
print("t =",t)
print('t =', t, "seconds")
print('t is now =', t/3, '\n..and can be rounded using `round()`', round(t/3, 4))

#sqring a number:
print(3**2)

#lists:
list1 = [0, 1, 2, 3] #row vect
print("list1:", list1)
list2 = [[0] ,[1] ,[2] ,[3]] #col vect
print('list2:',list2)
list3 = [[0 ,1] ,[2 ,3]] #2d array/2x2 matrix
print('list3:',list3)

#numpy arrays:
array1 = numpy.array ([0,1,2,3])
print('array1:',array1)
array2 = numpy.array ([[0] ,[1] ,[2] ,[3]])
print('array2:',array2)
array3 = numpy.array ([[0 ,1] ,[2 ,3]])
print('array3:',array3)

#should rename 'numpy' module call before array funct call:
import numpy as np #renames 
import scipy.signal as sig

print(np.pi)

# This is a comment , and the following statement is not executed:
# print(t+5)

#generate a sequential array:
print(np.arange (4),'\n', #stop
      np.arange (0, 2, 0.5), '\n', #start,stop,stepSize
      np.linspace(0, 1.5, 4)) #start,stop, numSteps Tween
#arange: upper bounce exclusive, lower bound inclusive

#range() useful for for-loops (almost same as numpy.arange() )

#numpy arrays have more flexible indexing:
list1 = [1,2,3,4,5]
array1 = np.array(list1) # definition of a numpy array using a list
print('list1 :', list[0], list[4])
print('array1:',array1[0], array1[4])
array2 = np.array ([[1,2,3,4,5], [6,7,8,9,10]])
list2 = list(array2)
print('array2:', array2[0,2], array2[1,4])
print('list2 :', list2[0], list2[1])

#access entire row/col in numpy arr:
print(array2 [:,2], array2 [0,:])

#def an array of all zeros:
print('1x3:', np.zeros(3))
print('2x2:', np.zeros((2,2)))

#def arr of all 1's:
print('2x3:', np.ones((2,3)))

#plotting in python:
# lookup documentation on 'matplotlib.pyplot'
import matplotlib.pyplot as plt

# Define vars
steps = 0.1 # step size
x = np . arange ( -2 ,2+ steps , steps ) # notice the final value is
# ‘2+ steps ‘ to include ‘2 ‘
y1 = x + 2
y2 = x **2

# Code for plots
plt . figure ( figsize =(12 ,8) ) # start a new figure , with
# a custom figure size
plt . subplot (3 ,1 ,1) # subplot 1: subplot format (row , column , number )
plt . plot (x , y1 ) # choosing plot variables for x and y axes
plt . title ('Sample Plots for Lab 1') # title for entire figure
# (all three subplots )
plt . ylabel ('Subplot 1') # label for subplot 1
plt . grid ( True ) # show grid on plot

plt . subplot (3 ,1 ,2) # subplot 2
plt . plot (x , y2 )
plt . ylabel ('Subplot 2') # label for subplot 2
plt . grid ( which ='both') # use major and minor grids (cant be 'both ')
# ( minor grids not available
# since plot is small )

plt . subplot (3 ,1 ,3) # subplot 3
plt . plot (x , y1 ,'--r', label ='y1')
plt . plot (x , y2 ,'o', label ='y2' ) # plotting both functions on one plot
plt . axis ([ -2.5 , 2.5 , -0.5 , 4.5]) # define axis
plt . grid ( True )
plt . legend ( loc ='lower right' ) # prints a legend on the plot
plt . xlabel ('x') # x- axis label for all three subplots ( entire figure )
plt . ylabel ('Subplot 3') # label for subplot 3
plt . show () ### --- This MUST be included to view your plots ! --- ###
#subplots and traces shown above

#complex nums:
cRect = 2 + 3j
print(cRect)

cPol = abs(cRect) * np.exp(1j* np.angle ( cRect ))
print ( cPol ) # notice Python will store this in rectangular form

cRect2 = np.real ( cPol ) + 1j * np.imag ( cPol )
print ( cRect2 ) # converting from polar to rectangular (prints out in rect?)

#if get 'nan', add '0j' [to specify complex #]:
#fails: print ( numpy.sqrt (3*5 - 5*5) )
print ( numpy.sqrt (3*5 - 5*5 + 0j ) )

#list of packages used this semester:
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.signal as sig
import pandas as pd
import control
import time
from scipy.fftpack import fft, fftshift

#usefull functions:
#range () # create a range of numbers ( nice for ‘for ‘ loops )
#np . arange () # create a numpy array that is a range of number with a defined
# step size
#np . append () # add values to the end of a numpy array
#np . insert () # add values to the beginning of a numpy array
#np . concatenate () # combine two numpy arrays
#np . linspace () # create a numpy array that contains a specified ( linear ) range
# of values with a specified number of elements
#np . logspace () # create a numpy array that contains a specified ( logarithmic ,
# base specified ) range of values with a specified number of
# elements
#np . reshape () # reshape a numpy array
#np . transpose () # transpose a numpy array
#len () # return the number of elements in an array ( horizontal )
#.size # return the number of elements in an array ( vertical )
#.shape # return the dimensions of an array
#.reshape # reshape the dimensions of an array ( similar to numpy . reshape ()
# above )
#.T # transpose an array ( similar to np. transpose () above )

