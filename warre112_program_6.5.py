#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:07:49 2020

@author: warre112
"""
"""
Assignment #02
Exercise 6.5
Les Warren warre112
"""

##GCD Function for 2 Numbers
def gcd(a, b):
    if b == 0:
        ##if b= 0 then gcd returns to a
        return a
    else:
       return gcd(b, a%b)
       ##gcd(a,b)=gcd(b,r)
       ## r= a/b

##Test Function
gcd(48,30)

       






      







    
    
    