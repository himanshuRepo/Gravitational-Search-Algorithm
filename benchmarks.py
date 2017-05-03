# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:46:20 2016

@author: Hossam Faris

This file is part of edited code. 
Edited by Himanshu Mittal, himanshu.mittal224@gmail.com
 -- Purpose: Defining the benchmark function code 
              and its parameters: function Name, lowerbound, upperbound, dimensions

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy
import math


    
def F1(x):
  """ Spere Function """
  s=numpy.sum(x**2);
  return s



def getFunctionDetails(a):
  # [name, lb, ub, dim]
  param = {  0: ["F1",-100,100,30],
            }
  return param.get(a, "nothing")



