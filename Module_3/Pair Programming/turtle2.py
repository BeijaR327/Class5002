# -*- coding: utf-8 -*-
"""
Turtle2.py

Created on Fri Feb  7 15:30:37 2025

@author: hdavi

This is material from section 4.2 of



https://allendowney.github.io/ThinkPython/chap04.html

by Allen Downey

on drawing a square, using two different appraoches

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


# Make Tess draw a square

tess.forward(50)
tess.left(90)
tess.forward(50)
tess.left(90)
tess.forward(50)
tess.left(90)
tess.forward(50)
tess.left(90)

#move tess forward 100, to avoid our square
#straighten tess out first, so tess moves horizontally
tess.penup()
tess.left(90)
tess.forward(100)
tess.color("red")

# use a loop to control tess,  since she needs to do things four times in a row

tess.pendown()

# this is a standard python for loop, by the way

for i in range(4):
    tess.forward(60)
    tess.left(90)


#Question/Action

# lift the pen up,   turn tess 180 degrees and move 120 steps down toward
# the bottom of the screen
# then draw a hexagon in green with sides of length 50
# what angle will be needed?  How many turns in the for loop

tess.penup()
tess.left(180)
tess.down(120)


# stop drawing

turtle.done()
turtle.bye()

#close the turtle window after viewing it and before running another turtle
# program 
