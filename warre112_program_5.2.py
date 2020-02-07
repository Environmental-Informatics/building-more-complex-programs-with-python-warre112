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
Created Monday, January 27, 2020

This program creates several functions to check Fermat's Therom and allows a
user to input values into console
"""


def check_fermat(a,b,c,n):
    if a**n + b**n == c**n and n > 2:
    #Fermats Theroem needs four perameters and "n" must be greater than "2"
        print ("Yes, that works") #prints if all parameters are met
    else:
        print ("No, that doesn't work") #prints if one or more parameter is not met

def userinput(): #function to allow user to input values 
    a = input("Value of a: ") #input value of a
    b = input("Value of b: ") #input value of b
    c = input("Value of c: ") #input value of c
    n = input("Value of d: ") #input value of n
#userinput uses function check-fermat from above 
    
    check_fermat(int(a), int(b), int(c), int(n))
#converts input to integers and runs check_fermat function

userinput() #test function
    
    

