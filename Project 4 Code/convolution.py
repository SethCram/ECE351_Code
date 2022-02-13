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

