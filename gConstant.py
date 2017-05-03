# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:20:52 2017

@author: Himanshu Mittal 

This file is code by Himanshu Mittal, himanshu.mittal224@gmail.com
Purpose: Defining the gConstant Function
            for calculating the Gravitational Constant

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy

def gConstant(l,iters):
    alfa = 20
    G0 = 100
    Gimd = numpy.exp(-alfa*float(l)/iters)
    G = G0*Gimd
    return G