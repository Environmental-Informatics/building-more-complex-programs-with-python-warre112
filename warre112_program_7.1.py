#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:51:00 2020

@author: warre112
"""

#Exercise 7.1
#Les Warren warre112

import math

##Function for SqRt using Newton's Method
def mysqrt(a):
    x = a/2
    while True:
        print(x)
        y= (x + a/x)/2
        if y == x:
            break
        x = y
        return x
##above informtion is from textbook chapter 7 and Newton's method
        
##Function using Pythons internal SqRt
def sqrt(a):
    return math.sqrt(a)



        