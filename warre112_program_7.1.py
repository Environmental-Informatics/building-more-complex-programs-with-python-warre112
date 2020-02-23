#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:51:00 2020

@author: warre112
"""
"""
Assignment #02
Exercise 7.2
Les Warren warre112
Created Thursday, January 30, 2020

This program develops a functon to calculate the square root usign Newtons method
and compares it against Python's square root function (from Math). Creates a table 
comparing both values 
"""

import math #imports math package 

"Function for SqRt using Newton's Method"
def mysqrt(a): #function with one variable
    x = a/2 #estimates value of x
    while True: #loop
        y= (x + a/x)/2 #Newtons equation
        if abs(y-x) <0.00000000000000000001:        
            return(x) #returns value of x
            break #ends loop
        x=y
##above informtion is from textbook chapter 7 and Newton's method
mysqrt(2)


"Function to create table"

def test_square_root():
    print('a  ','mysqrt(a)    ','math.sqrt(a) ','diff') # column headers
    print('-  ','---------    ','------------ ','----') # space
    for i in range(1, 10): #loop in range of 9 (n-1)
        print('%-4i%-14g%-14g%-10g' % (i,mysqrt(i),math.sqrt(i),(abs(mysqrt(i)-math.sqrt(i)))))
    #prints table---("4i%") is spacing after printed variable)
    #uses mysqrt to calculate using Newtons method, math.sqrt to get actual
test_square_root()