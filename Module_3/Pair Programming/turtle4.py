# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 09:14:20 2025

@author: SheetsH

Approximating a Circle

From ThinkPython

Section 4.4

https://allendowney.github.io/ThinkPython/chap04.html

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


def polygon(n, length):
    """ This is a function to draw a polygon, where n is the number of side
    and length is the length of each side.  It uses the variable tess, which
    is the name of a turtle """
    angle = 360 / n
    for i in range(n):
        tess.forward(length)
        tess.left(angle)

def circle(radius):
    "circle function uses polygon, radius is the circle radius"
    circumference =2*math.pi*radius
    n=30
    length=circumference/n
    polygon(n,length)
    
polygon(8,20)

tess.penup()
tess.forward(100)
tess.pendown()
circle(60)

# stop drawing

turtle.done()


#close the turtle window after viewing it and before running another turtle
# program
