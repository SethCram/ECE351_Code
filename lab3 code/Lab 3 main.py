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
import matplotlib.pyplot as plt
#import scipy #for convolve funct

#import the step and ramp functs I def'd:
from Lab_3_ramp_and_step_functs import u, r #don't use .py extension on file name
#from Lab_3_ramp_and_step_functs import r #don't use * to import

steps = 1e-2 # Define step size
t = numpy.arange(0, 20 + steps , steps)

f1 = u(t-2) - u(t-9)
f2 = u(t) * numpy.exp(-t) #exp can use a non-user def'd function
f3 = r(t-2) * ( u(t-2) - u(t-3) ) + r(4-t) * ( u(t-3) - u(t-4) )

#PLOTS 
    
#plot1:
plt.figure(figsize = (10,15)) #1st arg = horizontal space, 2nd arg = vertical space
plt.subplot(3, 1, 1)
plt.plot(t, f1) # t = step size, smaller it is the more accurate graph is
                # y = array of cos vals at each step
plt.grid() #add a grid to graph
plt.title('f1(t) vs t')
plt.ylabel('f1(t)')

#plot2:
plt.subplot(3, 1, 2)
plt.plot(t, f2)
plt.grid() #add a grid to graph
plt.title('f2(t) vs t')
plt.ylabel('f2(t)')

#plot3:
plt.subplot(3, 1, 3)
plt.plot(t, f3)
plt.grid() #add a grid to graph
plt.title('f3(t) vs t')
plt.ylabel('f3(t)')
plt.xlabel('t')

plt.show() #print both plots

#CONVOLUTION

#convultion w/ overlap:
def convolve(f1, f2): #convolve f1 and f2
    
    #debug: print("input f2: ", f2)

    Nf1 = len(f1) #num of f1 entries
    Nf2 = len(f2)

    #add zeros onto the end of functs so they're same size:
    f1Extend = numpy.append( f1, numpy.zeros((1, Nf2-1))) #had to make numpy.zero() arg a tupple
    f2Extend = numpy.append( f2, numpy.zeros((1, Nf1-1)))
    
    #make result array the same size as above arrays:
    result = numpy.zeros( f1Extend.shape )
    
    #look thru all elly's in arrays:
    for i in range( Nf2 + Nf1 - 2 ):
        result[i] = 0; #zero out result
        
        for j in range(Nf1): #Nf1 bc f1 convolved w/ f2
            if( i-j+1 > 0 ):
                try:
                    #compute the result by adding up multiplied overlapping pnts:
                    result[i] += f1Extend[j] * f2Extend[i-j+1]  
                except: #out of bounds in one of the 3 arrs
                    print( "Failed at i = %d, j = %d" % (i, j) )
    return result  
    
    #pass #filler keyword bc can't leave empty
    
    #compare this funct to lib convolve

#test case:
x = numpy.array([4, 3, 6])
y = numpy.array([1, 2, 5, 6])

print("x: ", x)
print ("y: ", y)

result = numpy.convolve(x, y)
print("Library test case rslt: ", result)

result = convolve(x, y)
print("My test case rslt: ", result)

#PLOT1   

y1 = convolve( f1, f2 )   
 
#use numpy instead of scipy convolve:
y2 = numpy.convolve(f1, f2) #results in twice as many pnts

#plot1:
plt.figure(figsize = (10,10)) #1st arg = horizontal space, 2nd arg = vertical space
plt.subplot(2, 1, 1)

#debug: print(len(y2))

plt.plot(t, y1[0:len(t)]) #have to cut of y-vals bc alot more of them than t (twice as many) 
plt.grid() #add a grid to graph
plt.title('My Convolve of f1 and f2')
plt.ylabel('y(t)')
plt.xlabel('t')

#plot2:
plt.subplot(2, 1, 2)
plt.plot(t, y2[0:len(t)])
plt.grid() #add a grid to graph
plt.title('Library Convolve of f1 and f2')
plt.ylabel('y(t)')
plt.xlabel('t')

plt.show() #print both plots

#PLOT2

y1 = convolve( f2, f3 )   
 
#use numpy instead of scipy convolve:
y2 = numpy.convolve(f2, f3) #results in twice as many pnts

#plot1:
plt.figure(figsize = (10,10)) #1st arg = horizontal space, 2nd arg = vertical space
plt.subplot(2, 1, 1)

#debug: print(len(y2))

plt.plot(t, y1[0:len(t)]) #have to cut of y-vals bc alot more of them than t (twice as many) 
plt.grid() #add a grid to graph
plt.title('My Convolve of f2 and f3')
plt.ylabel('y(t)')
plt.xlabel('t')

#plot2:
plt.subplot(2, 1, 2)
plt.plot(t, y2[0:len(t)])
plt.grid() #add a grid to graph
plt.title('Library Convolve of f2 and f3')
plt.ylabel('y(t)')
plt.xlabel('t')

plt.show() #print both plots

#PLOT3

y1 = convolve( f1, f3 )   
 
#use numpy instead of scipy convolve:
y2 = numpy.convolve(f1, f3) #results in twice as many pnts

#plot1:
plt.figure(figsize = (10,10)) #1st arg = horizontal space, 2nd arg = vertical space
plt.subplot(2, 1, 1)

#debug: print(len(y2))

plt.plot(t, y1[0:len(t)]) #have to cut of y-vals bc alot more of them than t (twice as many) 
plt.grid() #add a grid to graph
plt.title('My Convolve of f1 and f3')
plt.ylabel('y(t)')
plt.xlabel('t')

#plot2:
plt.subplot(2, 1, 2)
plt.plot(t, y2[0:len(t)])
plt.grid() #add a grid to graph
plt.title('Library Convolve of f1 and f3')
plt.ylabel('y(t)')
plt.xlabel('t')

plt.show() #print both plots





#ALOTS DIFFERENT KINDS OF CONVOLUTION











""" verify imported modules:

steps = 1e-2 # Define step size
t1 = numpy.arange(-5, 10 + steps , steps) #create array of steps 0-10
t2 = numpy.arange(-5, 10 + steps , steps)

y1 = r(t1)
y2 = u(t2)
    
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
"""


"""Extra:
    
    #if funct 1 has more entries than funct 2:
    if( Nf1 > Nf2 ): #f1 bigger
        newf1 = numpy.append( [], f1[0:Nf1] ) #copy over array vals
        
        diff = Nf1 - Nf2 #difference
        newf2 = numpy.zeros( Nf2 + diff ) #zero out bigger array
        newf2 = numpy.append( [], f2[0:Nf2] )
        
        biggestSize = Nf1 #set biggest size
    elif( Nf2 > Nf1 ): #f2 bigger
        diff = Nf2 - Nf1
        newf1 = numpy.zeros( Nf1 + diff )
        newf1 = numpy.append( [], f1[0:Nf1] )
        
        biggestSize = Nf2

        newf2 = numpy.append( [], f2[0:Nf2] )
    else: #same size
        newf1 = numpy.append( [], f1[0:Nf1] )
        newf2 = numpy.append( [], f2[0:Nf2] )
    
    #now, newf1 and newf2 should be same size
    
    #use Nf1,Nf2, and np.append() to initialize new f1 and f2 arrays that will have the same length.
     #copy over vals index'd 0 to len (not len-1)
     #newf2[Nf2] #doesnt work
                                            # have to include '0:' or else gives only last elly 
    

    #debug: 
    #print ("new f1", newf1)
    #print("new f2: ", newf2)

    #initialize new result array using one of the new arrays from above and use .shape
    #rslt = newf1.shape
    rslt = numpy.zeros( Nf1 + Nf2 - 1 ) #can zero arr bc will fill it all
    
    #debug: 
    print("init'd result arr: ", rslt)
    
    mult = numpy.zeros( rslt.shape ) #zeros out ph mult arr w/ f1 entries
    
    print("ph array for results: ", mult)
    
    #have to reverse one of the functs: (chose f2)
    flipped_f2 = newf2[::-1] #step backwards thru arr
    
    #debug: print( "flipped f2: ", newf2)
    
    #outer for loop stores an entry in result arr for every i
    #try setting up a for loop within a for loop, with the first for loop going through the combined lengths of f1 and f2. 
    for i in range(0, Nf1+Nf2 ): # not -1 bc last val not inclusive
        #second for loop should go through 'range' of placeholder function you used to initialize your result array.
        for j in range(0, biggestSize): #could do min of Nf1 and Nf2

            #debug: print("i = %d, j = %d" % (i, j) ) #syntax is important, must us tuple to print alota vars
        
            #if functs not yet overlapping:
                
            try:
                mult[j] = newf1[j] * flipped_f2[j+i] #fill ph array
            except:
                print("failed at i = %d, j = %d" % (i, j) )
                break
            
            
            #debug:
            print("mult %d: %d" % (j, mult[j]) )
            
            #if 1st iteration: (use if rslt arr not init'd to zeros)
            if( j == 0):
                rslt[i] = mult[j] #copy val over
            else: #other iteration
                rslt[i] = rslt[i] + mult[j] #add val to pre-existing one(s)

    #check that length of both functions are greater than length of whatever function you have used to set up your result array.
    if( Nf2 + Nf1 > len(rslt) ):
        print("Good job, result arr is smaller than input arrs added together")

        # if they are, go ahead and calculate the current index in your result array using the definition of the duration of the convolution. You shouldn't need to use integrals.
        #duration: [t1+t2, T1+T2]
    else: # if they aren't, see if you can print out where in the combined and placeholder function that's happening. Printing out arrays or looking in the variable watcher is a great way to debug your code!
        print("Incorrect result: ", rslt)

"""
