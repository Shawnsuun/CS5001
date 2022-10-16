from turtle import *
import random

#moves a turtle cursor without drawing 
def goto(x = 0, y = 0):
	penup()
	setx(x)
	sety(y)
	pendown()

# test reset()
# goto(0, 0)
# forward(100)
# goto(100, 100)
# forward(100)

#moves the turtle cursor to home position without drawing
def reset():
	goto(0,0)

# test reset()
# goto(100, 50)
# forward(100)
# reset()
# forward(100)

#draws a square at a given position with a provided side length
def square(x, y, len):
	goto(x, y)
	forward(len)
	left(90)
	forward(len)
	left(90)
	forward(len)
	left(90)
	forward(len)
	left(90)

# test square(x, y, len)
# square(0, 0, 100)
# square(100, 50, 100)

# draws a grid of 4 boxes in the below pattern. Each box should have sides equal to the sent value
def frame(box_size):
	reset()
	color("black");
	square(0, 0, box_size)
	square(0, box_size, box_size)
	square(box_size, box_size, box_size)
	square(box_size, 0, box_size)

# test frame(box_size)
# frame(100)
# frame(5)

# get a random color
def	rand_color():
	colors = {'red', 'blue', 'yellow', 'pink', 'purple', 'brown','green'}
	color = random.sample(colors, 1)
	return color

# set maximum drawing speed
def set_max_speed():
	speed(0)

# clear screen
def clear_screen():
	clear()
