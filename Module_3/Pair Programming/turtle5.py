# -*- coding: utf-8 -*-
"""
Refactoring

Refactoring is to rework code to make it work better in some way
without altering it's behavior

This example shows a good deal about stacking,  the idea that complicated
programming behavior is built of "stacked" functions (and objects and classes
as we will see later)



Created on Sat Feb  8 09:21:16 2025

@author: SheetsH
"""

# import the turtle library

import turtle
import math

#Create a turtle screen,  with a yellow background

wn=turtle.Screen()
wn.bgcolor("lightyellow")

#our turtle is named tess

tess = turtle.Turtle() # Create tess and set some attributes
tess.color("blue")
tess.pensize(5)

# Create a more general version of polygon called polyline
# that draws part of a polygon

def polyline(n, length, angle):
    """ function polyline """
    for i in range(n):
        tess.forward(length)
        tess.left(angle)

#QUESTION/ACTION

# what do the parameters n, length and angle do?
# Modify the docstring in the function so that it explains
# what the input variables are and what the function does
# write code to draw an L shape

# Now rewrite polygon so that it works by using polyline
# This is a refactored version of the earlier polygon code

def polygon(n,length):
    angle=360/n
    polyline(n,length,angle)

# create a function arc to draw curved lines

def arc(radius,angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)

# use arc to draw the circle

def circle(radius):
    arc(radius,  360)


# now do some drawing

polygon(n=5, length=120)

arc(radius=80, angle=90)

circle(radius=20)

# stop drawing

turtle.done()
turtle.bye()

#close the turtle window after viewing it and before running another turtle
# program
 