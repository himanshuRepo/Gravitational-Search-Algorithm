# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
           Information sciences 179.13 (2009): 2232-2248.	

Coded by: Mukesh Saraswat (saraswatmukesh@gmail.com), Himanshu Mittal (emailid: himanshu.mittal224@gmail.com) and Raju Pal (emailid: raju3131.pal@gmail.com)
The code template used is similar given at link: https://github.com/7ossam81/EvoloPy and matlab version of GSA at mathworks.

Purpose: Defining the gField Function
            for calculating the Force and acceleration

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy
import random
import math

def gField(PopSize,dim,pos,M,l,iters,G,ElitistCheck,Rpower):
    final_per = 2
    if ElitistCheck == 1:
        kbest = final_per + (1-l/iters)*(100-final_per)
        kbest = round(PopSize*kbest/100)
    else:
        kbest = PopSize
            
    kbest = int(kbest)
    ds = sorted(range(len(M)), key=lambda k: M[k],reverse=True)
        
    Force = numpy.zeros((PopSize,dim))
    # Force = Force.astype(int)
    
    for r in range(0,PopSize):
        for ii in range(0,kbest):
            z = ds[ii]
            R = 0
            if z != r:                    
                x=pos[r,:]
                y=pos[z,:]
                esum=0
                imval = 0
                for t in range(0,dim):
                    imval = ((x[t] - y[t])** 2)
                    esum = esum + imval
                    
                R = math.sqrt(esum)
                
                for k in range(0,dim):
                    randnum=random.random()
                    Force[r,k] = Force[r,k]+randnum*(M[z])*((pos[z,k]-pos[r,k])/(R**Rpower+numpy.finfo(float).eps))
                    
    acc = numpy.zeros((PopSize,dim))
    for x in range(0,PopSize):
        for y in range (0,dim):
            acc[x,y]=Force[x,y]*G
    return acc
