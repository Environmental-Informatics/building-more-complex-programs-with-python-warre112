#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment #02- Exercise 4.2
Les Warren warre112
Created Thursday, January 30, 2020

Creates functions to draw flowers with 8, 10, and 20 petals using Turtle package
Functions include petal, flower, and a fucntion to draw all three flowers
"""

import turtle #imports turtle package
bob= turtle.Turtle()
def petal(length, angle): #function to draw individual petal with two variables
    for i in range (2): #loop
        bob.circle(length,angle) #length= radius, #angle= extent 
        bob.left(180-angle) #defines angle of movement 

def flower(n, length, angle):   #function to draw "n" petals 
    
    for i in range (n):  #loop to draw n petals                                   
        petal(length, angle) #defines petal length and angle
        bob.left(360/n) #defines angle of movement to left

bob.penup() #raises turtle pen
bob.goto(-200, 0) #moves intital turtle 200 pixals to the left (off center)
bob.pendown() #lowers turtle pen  

flower(8, 110, 60) #first flower with 8 petals

bob.penup() #raises turtle pen
bob.goto(0, 0) #moves turtle 200 pixals to the right (centered)
bob.pendown() #lowers turtle pen  

flower(10,70,90) #second flower with 10 petals

bob.penup() #raises turtle pen
bob.goto(200, 0) #moves turtle 200 pixals to right (off center)
bob.pendown() #lowers turtle pen  

flower(20,170,30) #third flower with 20 petals 


