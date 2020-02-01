#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:07:49 2020

@author: warre112
"""
"""
Assignment #2
Exercise 5.2
Les Warren warre112
"""


def check_fermat(a,b,c,n):
    if a**n + b**n == c**n and n > 2:
    #Fermats Theroem needs four perameters and "n" must be greater than "2"
        print ("Yes, that works")
    else:
        print ("No, that doesn't work")

def userinput():
    a = input("Value of a: ")
    b = input("Value of b: ")
    c = input("Value of c: ")
    n = input("Value of d: ")
#input function allows user to input value in console
#userinput uses function check-fermat from above 
    
    check_fermat(int(a), int(b), int(c), int(n))
#converts input to integers

userinput()
    
    

