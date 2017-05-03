# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:20:52 2017

@author: Himanshu Mittal 

This file is code by Himanshu Mittal, himanshu.mittal224@gmail.com
Purpose: Defining the massCalculation Function
            for calculating the mass

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy 

def massCalculation(fit,PopSize,M):
    Fmax = max(fit)
    Fmin = min(fit)
    Fsum = sum(fit)        
    Fmean = Fsum/len(fit)
        
    if Fmax == Fmin:
        M = numpy.ones(PopSize)
    else:
        best = Fmin
        worst = Fmax
        
    for p in range(0,PopSize):
        M[p] = (fit[p]-worst)/(best-worst)
            
    Msum=sum(M)
    for q in range(0,PopSize):
        M[q] = M[q]/Msum
            
    return M