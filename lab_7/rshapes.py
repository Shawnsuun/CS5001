from turtle import *
import random

# draw recursive boxes
# x, y--coordinate of shape, size--square length, scaledown--scale to reduce recursive shape, min_size--minimum allowed square length
def boxes(x, y, size, scaleDown, min_size):
	if (size > min_size):
		reset(x, y - size / 2, 0)
		color(rand_color())
		rect(size)
		boxes(x, y, size * scaleDown, scaleDown, min_size)

#draw recursive spiral
# x, y--coordinate of shape, lineLen--spiral line length
def drawSpiral(x, y, lineLen):
	if (lineLen > 0):
		forward(lineLen)
		right(90)
		color(rand_color())
		drawSpiral(x, y, lineLen - 5)

#draw recursive circles
# x, y--coordinate of shape, radius--circle radius, scaledown--scale to reduce recursive shape, min_size--minimum allowed radius
def circles(x, y, radius, scaleDown, min_radius):
	if (radius > min_radius):
		reset(x, y - radius, 0)
		color(rand_color())
		circle(radius)
		circles(x, y, radius * scaleDown, scaleDown, min_radius)

# draw a recursive box tree
# x, y--coordinate of shape, size--box side length, scaledown--scale to reduce recursive shape, min_size--minimum allowed square size
def boxTree(x, y, size, scaleDown, min_size):
	if (size > min_size):
		reset(x, y, 0)
		color(rand_color())
		rect(size)
		boxTree(x - size / 2 - size * scaleDown / 4, y + size, size * scaleDown, scaleDown, min_size)
		boxTree(x + size / 2 + size * scaleDown / 4, y + size, size * scaleDown, scaleDown, min_size)

# size--length of the trunk, scaledown--scale to reduce recursive shape, level--max levels of the tree(at least 2 levels)
def recursive_tree(size, scaleDown, level):
	if (level > 0):
		forward(size * 0.8)
		color('red')
		begin_fill()
		circle(size* random.uniform(0.05, 0.1))
		end_fill()
		color('green')
		forward(size * 0.2)
		ang = random.randint(20, 40)
		left(ang)
		recursive_tree(size * scaleDown * random.uniform(0.75, 1.25), scaleDown, level - 1)
		right(60)
		recursive_tree(size * scaleDown * random.uniform(0.75, 1.25), scaleDown, level - 1)
		left(60 - ang)
		forward(-size)

# draw half snowflake
# size--length of snowflake skeleton, scaledown--scale to reduce recursive shape, level--max levels of the snowflake(at least 2 levels)
def recursive_half_snowflake(size, scaleDown, level):
	if (level > 0):
		color('cyan')
		forward(size)
		left(60)
		recursive_half_snowflake(size * scaleDown, scaleDown, level - 1)
		right(120)
		recursive_half_snowflake(size * scaleDown, scaleDown, level - 1)
		left(60)
		recursive_half_snowflake(size * scaleDown, scaleDown, level - 1)	
		forward(-size)

#draw a complete snowflake
def snowflake(x, y, size, scaleDown, level):
	reset(x, y, 90)
	recursive_half_snowflake(size, scaleDown, level)
	forward(2 * size)
	recursive_half_snowflake(- size, scaleDown, level)
	color('black')

#draw forest by nested while loops
def forest():
	x = -300
	y = -200
	while x < 300:
		while y < 200:
			reset(x * random.uniform(0.8, 1.2), y * random.uniform(0.8, 1.2), 90)
			recursive_tree(50, 0.6, 5)
			y += 150
		x += 150
		y = -300

#draw a square with side length size
def rect(size):
	forward(size / 2)
	left(90)
	forward(size)
	left(90)
	forward(size)
	left(90)
	forward(size)
	left(90)
	forward(size / 2)

#go to (x, y), set the heading direction to angle
def reset(x, y, angle):
	penup()
	setheading(angle)
	goto(x, y)
	pendown()

# get a random color
def	rand_color():
	colors = ['red', 'blue', 'yellow', 'pink', 'purple', 'brown','green','cyan']
	color = random.choice(colors)
	return color

# clear screen
def clear_screen():
	clear()

# set max speed
def max_speed():
	speed(0)



