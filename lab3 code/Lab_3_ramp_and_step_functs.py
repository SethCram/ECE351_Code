# -*- coding: utf-8 -*-

################################################################
# #
# Seth Cram #
# ECE351-53 #
# Lab 3 #
# Due: 2/08/2022 #
# Any other necessary information needed to navigate the file #
#  
#
################################################################

import numpy
#import matplotlib.pyplot as plt

def r(t):
    #check:print("Ramp function")
    
    y = numpy.zeros(t.shape) #zero out y array w/ size of t
    
    try: #case for array
        for i in range(len(t)): #run loop once each step
            if( t[i] < 0):
                y[i] = 0 #zero
            else:
                y[i] = t[i] #fill y with t for slope of 1
    except: #case for single val
        if( t < 0):
            y = 0
        else:
            y = t #fill y with t for slope of 1    
    
    return y

#expects an array:
def u(t): 
    #check: print("Step funct")
    
    y = numpy.zeros(t.shape) #zero out y array w/ size of t

    try: #case for array of vals passed
        for i in range(len(t)): #run loop once each step
            if(t[i] < 0): #less than 0
                y[i] = 0;
            else:    #equal to great than zero
                y[i] = 1 #fill y with flat line at 1
    
    except: #case for a single value passed
        if(t < 0): #less than 0
            y = 0;
        else:    #equal to great than zero
            y = 1 #fill y with flat line at 1
    return y

