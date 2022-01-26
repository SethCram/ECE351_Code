# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:49:07 2022

@author: crazy
"""

################################################################
# #
# Seth Cram #
# ECE351-53 #
# Lab 2 part 2 and part 3 #
# Due: 1/25/2022 #
# Any other necessary information needed to navigate the file #
#  
#
################################################################

import numpy
import matplotlib.pyplot as plt

def ramp_funct(t):
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
def step_funct(t): 
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
    
steps = 1e-2 # Define step size
t1 = numpy.arange(-5, 10 + steps , steps) #create array of steps 0-10
t2 = numpy.arange(-5, 10 + steps , steps)

y1 = ramp_funct(t1)
y2 = step_funct(t2)
    
#plot1:
plt.figure(figsize = (10,10)) #1st arg = horizontal space, 2nd arg = vertical space
plt.subplot(2, 1, 1)
plt.plot(t1, y1) # t = step size, smaller it is the more accurate graph is
                # y = array of cos vals at each step
plt.grid() #add a grid to graph
plt.title('Ramp Function')
plt.ylabel('y(t)')

#plot2:
plt.subplot(2, 1, 2)
plt.plot(t2, y2)
plt.grid() #add a grid to graph
plt.title('Step Function')
plt.ylabel('y(t)')
plt.xlabel('t')

plt.show() #print both plots

#implement function:
    #overlap happens where functs meet

def combo_funct(t):
    y = numpy.zeros(t.shape) #zero out y array w/ size of t
    
    for i in range(len(t)):
        y[i] = ramp_funct(t[i]) - ramp_funct(t[i]-3) + 5*step_funct(t[i]-3) - 2*step_funct(t[i]-6) - 2*ramp_funct(t[i]-6)
        
        """Hardcoded combo_funct:
        if( t[i] < 0 ): #if t val is neg
            y[i] = step_funct(t[i]) #calc step funct at val (0)
        elif ( (t[i] < 3) and (t[i] > 0) ): #0 to 3 (&& = and in python)
            y[i] = ramp_funct(t[i]) #calc ramp funct at val 
        elif ( (t[i] > 3) and (t[i] < 6) ): #3 to 6
            y[i] = 8 * step_funct(t[i]) #mult ret'd val by 8 bc set to 1, doesn't add 1
        elif ( (t[i] > 6) and (t[i] < 10) ): #6 to 10
            y[i] = -2 * ramp_funct(t[i]) + 18 #had to mult by -2 to get the same result (and offset up 18)
        """
        #else:  #default for testing
        #    y[i] = 0
    return y

"""actually Hardcoded combo_funct steps:
steps = 1e-2

#Funct for -5 to 0: (t-axis)
tFunct = numpy.arange(-5, 0 + steps , steps)
yFunct = step_funct(tFunct)

#check: print(yFunct)

#funct for 0 to 3:
tFunct1 = numpy.arange(0, 3 + steps , steps) #overwrites, we need to append()
yFunct = numpy.append( yFunct, ramp_funct(tFunct1) ) #1st arg = og array, 2nd = vals to append
tFunct = numpy.append( tFunct, tFunct1 )

#check: print(yFunct)

#Funct for 3 to 6:
tFunct3 = numpy.arange(3, 6 + steps , steps)
yFunct = numpy.append( yFunct, 8 * step_funct(tFunct3) ) #mult ret'd val by 8 bc set to 1, doesn't add 1
tFunct = numpy.append( tFunct, tFunct3 )

#Funct for 6 to 6(ish):
tFunct4 = numpy.arange(6, 6 + steps , steps)
yFunct = numpy.append( yFunct, 6 * step_funct( tFunct4 ) ) 
tFunct = numpy.append( tFunct, tFunct4 )

#Funct for 6(ish) to 10:
tFunct5 = numpy.arange( 6 + steps, 10 + steps, steps)
yFunct = numpy.append( yFunct, (-2) * ramp_funct(tFunct5) + 18 ) #eqt: mult by -1/2 bc want neg, steeper slope
                                                                #here: had to mult by -2 to get the same result and offset up 18
tFunct = numpy.append( tFunct, tFunct5 )

plt.figure(figsize = (10,10)) #1st arg = horizontal space, 2nd arg = vertical space
plt.plot(tFunct, yFunct) 
plt.grid() 
plt.title('Combo Function')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
"""


steps = 1e-2

tFunct = numpy.arange(-5, 10 + steps , steps)
yFunct = combo_funct(tFunct)

plt.figure(figsize = (10,10)) #1st arg = horizontal space, 2nd arg = vertical space
plt.plot(tFunct, yFunct) 
plt.grid() 
plt.title('Combo Function')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()

#PART 3:

#apply a time reserval and plot it:
tFunct = numpy.arange(-10, 5 + steps , steps)
newTfunct = tFunct * -1
yFunct = combo_funct(newTfunct)

plt.figure(figsize = (10,10)) #1st arg = horizontal space, 2nd arg = vertical space
plt.plot(tFunct, yFunct) 
plt.grid() 
plt.title('Time Reversal of Combo Function')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()

#Apply time-shift operations f (t −4) and f (−t −4) and plot the results.
tFunct = numpy.arange(0, 15 + steps , steps)
newTfunct = tFunct - 4
yFunct = combo_funct(newTfunct)

plt.figure(figsize = (10,10)) #1st arg = horizontal space, 2nd arg = vertical space
plt.plot(tFunct, yFunct) 
plt.grid() 
plt.title('Time Shift t - 4 of Combo Function')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()

tFunct = numpy.arange(-15, 0 + steps , steps)
newTfunct = -1 * tFunct - 4
yFunct = combo_funct(newTfunct)

plt.figure(figsize = (10,10)) #1st arg = horizontal space, 2nd arg = vertical space
plt.plot(tFunct, yFunct) 
plt.grid() 
plt.title('Time shift -t - 4 of Combo Function')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()

#Apply time scale operations f (t/2) and f (2t) and plot the results:
tFunct = numpy.arange(-5, 18 + steps , steps)
newTfunct = (1/2) * tFunct
yFunct = combo_funct(newTfunct)

plt.figure(figsize = (10,10)) #1st arg = horizontal space, 2nd arg = vertical space
plt.plot(tFunct, yFunct) 
plt.grid() 
plt.title('Time Scale t/2 of Combo Function')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()

tFunct = numpy.arange(-5, 5 + steps , steps)
newTfunct = 2 * tFunct
yFunct = combo_funct(newTfunct)

plt.figure(figsize = (10,10)) #1st arg = horizontal space, 2nd arg = vertical space
plt.plot(tFunct, yFunct) #should NOT be newTfunct!!
plt.grid() 
plt.title('Time Scale 2t of Combo Function')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()

#plot the derivative of your user-defined function with
# respect to time:
tFunct = numpy.arange(-5, 10 + steps , steps)
tChange = numpy.diff( tFunct, axis = 0)
yChange = numpy.diff( combo_funct(tFunct), axis = 0 ) #take difference of each value in funct
#tChange = numpy.diff( tFunct, axis = 0)

#print(yChange)

yDeriv = yChange / tChange #calc change in y / change in t

#print(yDeriv)

#newtFunct = numpy.arange(-5, 10, steps) #bc had 1 too many time vals

plt.figure(figsize = (10,10)) #1st arg = horizontal space, 2nd arg = vertical space
plt.plot(tFunct[0:len(tFunct)-1], yDeriv) #need to slice off last t bc that difference is never taken
plt.grid() 
plt.ylim([-5,10]) #bound the function to see 
plt.title('Derivative of Combo Function')
plt.xlabel('t')
plt.ylabel('y\'(t)')
plt.show()
