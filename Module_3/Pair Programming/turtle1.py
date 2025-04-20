# -*- coding: utf-8 -*-
"""
Turtle1.py

Created on Fri Feb  7 15:30:37 2025

@author: hdavi

The "turtle" drawing system was part of the Logo language from the late 1960s
(which explains a lot, really) and was meant to teach people to think
algorithmically.

Thinking algorithmicly as about thinking about how one does a task, and then 

figuring out how to code it, how to write the program to make that happen.

This code is just some basics on working with a turtle.  Have fun with it,  
think about what it is trying to teach you.

It supports material in chapter 4 of "Think Python"

https://allendowney.github.io/ThinkPython/chap04.html

by Allen Downey


Some available turtle member functions

penup()
pendown()
pensize()
pencolor()

forward()
backward()
left()
right()

home()  - return to home point on screen



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


tess.forward(100) # Make tess draw a straight line

# let's add the code for a 90 degree left turn, from Allen Downey's exmaple in
# section 4.1 of the book


#lift the pen up, so we stop drawing
# and move forward 10 spaces so we are off the line
tess.penup()
tess.forward(10)

# put the pen down, go straight, then turn left and go straight again

tess.pendown()
tess.forward (20)
tess.left(90)
tess.forward(20)

# stop drawing

turtle.done()
turtle.bye()  

#close the turtle window after viewing it and before running another turtle
# program 