#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:06:26 2021

@author: niraj
"""

def read_file(filename):

    f = open(filename,"r")
    
    data_set = []
    
    while True:
        
       line = f.readline()
       
       if len(line)== 0:
           break
       
       line = line.replace("\n","") 
       
       xy = line.split(" ")
       
       xyline = (float(xy[0]), float(xy[1]))
       data_set.append(xyline)    
       
    return data_set
    
    f.close()
    
    