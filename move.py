# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:20:52 2017

@author: Himanshu Mittal 

This file is code by Himanshu Mittal, himanshu.mittal224@gmail.com
Purpose: Defining the move Function
            for calculating the updated position

Code compatible:
 -- Python: 2.* or 3.*
"""

import random

def move(PopSize,dim,pos,vel,acc):
    for i in range(0,PopSize):
        for j in range (0,dim):
            r1=random.random()
#           r2=random.random()
            vel[i,j]=r1*vel[i,j]+acc[i,j]
            pos[i,j]=pos[i,j]+vel[i,j]
    
    return pos, vel