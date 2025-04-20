# -*- coding: utf-8 -*-
"""
Turtle3.py

Created on Fri Feb  7 15:30:37 2025

@author: hdavi

This is material from section 4.3 of



https://allendowney.github.io/ThinkPython/chap04.html

by Allen Downey

on creating functions for the turtle

"""

# import the turtle library

import turtle

#Create a turtle screen,  with a yellow background

wn=turtle.Screen()
wn.bgcolor("lightyellow")

#our turtle is named tess

tess = turtle.Turtle() # Create tess and set some attributes
tess.color("blue")
tess.pensize(5)


# last time, we had tess the turtle drawing squares

# we can encapsulate that operation into a function, so it
# can be re-used

def square():
    for i in range(4):
        tess.forward(50)
        tess.left(90)

# we can call this by using square()


square()

# We can make this fancier by passing an input parameter into the function
# such as the length

def square2(length):
    for i in range(4):
        tess.forward(length)
        tess.left(90)

# we will move tess forward 120, to move away from the first square and then
# drawn another square

tess.penup()
tess.forward(120)
tess.pendown()

square2(75)

# making a function more useful, so it can be used in different contexts
# is call generalization


#Question/Action

# lift the pen up,   turn tess 180 degrees and move 120 steps down toward
# the bottom of the screen
# then draw a hexagon in green with sides of length 50
# what angle will be needed?  How many turns in the for loop


# stop drawing

turtle.done()
turtle.bye()  

#close the turtle window after viewing it and before running another turtle
# program 

