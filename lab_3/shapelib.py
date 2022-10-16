from turtle import *
import random

#go to a certain coordintae
def goto(x = 0, y = 0):
	penup()
	setx(x)
	sety(y)
	pendown()

#draw a retangle	
def draw_rect(length,width):
	left(90)
	forward(length)
	right(90)
	forward(width)
	right(90)
	forward(length)
	right(90)
	forward(width)
	right(90)
	forward(length)
	right(90)
	forward(0.25 * width)

#get a different color	
def	rand_color():
	colors = {'red', 'blue', 'yellow', 'pink', 'purple', 'brown','green'}
	color = random.sample(colors, 1)
	return color

#test 1
def test1():
	goto(0, 0)
	color(rand_color(), rand_color())
	begin_fill()
	draw_rect(100,200)
	end_fill()
	goto(300, 300)
	draw_rect(200,100)
#test1()

#draw a tower in random color	
def	draw_tower(length,width,filled = False):
	n = 0
	while n < 3:
		if filled == True:	
			color(rand_color(), rand_color())
			begin_fill()
		draw_rect(length,width)
		if filled == True:	
			end_fill()
		length = 0.5 * length
		width = 0.5 * width
		n += 1

#draw 3 towers in a decreasing scale in random colors
def	block(x,y,length,width,filled = False):
	n = 0
	while n < 3:
		goto(x,y)
		draw_tower(length,width,filled)
		x += width + 10
		length /= 2
		width /= 2
		n += 1

#test 2
def test2():
	goto()
	draw_tower(230,122,True)
	block(400, 400, 100, 200, True)
#test2()


#draw a house
def draw_house(height,width):
	scale = random.uniform(0.5, 1.5)
	color(rand_color(), rand_color())
	begin_fill()
	left(90)
	forward(height * scale)
	right(90)
	forward(width * scale)
	right(90)
	forward(height * scale)
	right(90)
	forward(width * scale)
	end_fill()
	right(90)
	forward(height * scale)
	right(45)
	forward(1.414 * width / 2 * scale)
	right(90)
	forward(1.414 * width / 2 * scale)
	left(45)

#draw houses in random height and color
def draw_houses(height,width):
	x = -150
	while x < 250:
		goto(x, 0)
		draw_house(height,width)
		x += random.randint(20, 35)

#test 3
def test3():
	goto()
	draw_house(45,45)
	goto(100, 100)
	draw_houses(100,100)
#test3()


#draw a building in random height and color
def draw_building(height,width):
	scale = random.uniform(0.5, 1.5)
	color(rand_color())

	left(90)
	forward(height * scale)
	right(90)
	forward(width * scale)
	right(90)
	forward(height * scale)
	right(90)
	forward(width * scale)
	right(180)

#draw skyline formed by buildings in random height and color
def draw_skyline(height,width):
	x = -100
	while x < 125:
		goto(x, 0)
		draw_building(height,width)
		x += random.randint(20, 35)

#test 4
def test4():
	goto()
	draw_building(45,45)
	goto(100, 100)
	draw_skyline(100,100)
#test4()


# draw a circle
def draw_circle(x,y,radius):
	goto(x,y)
	circle(radius)

# draw a lighthouse
def draw_lighthouse():
	color('blue')
	left(180)
	forward(500)
	left(180)
	goto()
	color('brown')
	forward(500)
	left(180)
	forward(500)
	left(180)

	color('black')
	forward(110)
	left(95)
	forward(200)
	color('white', 'yellow')
	begin_fill()
	left(55)
	forward(1000)
	left(120)
	forward(500)
	left(90)
	forward(1732.05/2)
	left(95)
	end_fill()
	color('black', 'red')
	begin_fill()
	circle(30)
	right(95)
	end_fill()

	color('black', 'white')
	begin_fill()
	goto()
	forward(110)
	left(95)
	forward(200)
	left(85)
	forward(60)
	left(85)
	forward(200)
	left(95)
	end_fill()

#test 5
def test5():
	goto()
	draw_lighthouse()
#test5()

#add custom texts
def add_text(text1 = "",text2 = ""):
	color('black') 
	write(text1,font = ("Arial", 25)) 
	penup()
	forward(150)
	pendown()
	scale = 9
	color('pink','red')        
	begin_fill()
	left(135)
	forward(2 * scale)
	circle(-1 * scale, 180)
	left(90)
	circle(-1 * scale, 180)
	forward(2* scale)       
	end_fill()
	left(135)
	penup()
	forward(40)
	pendown()
	color('black') 
	write(text2,font = ("Arial", 25)) 

#test 6
def test6():
	add_text("Hello","Maine")
#test6()


def clear_screen():
	clearscreen()

def main():
	goto(0, 0)
	block(0, 0, 100, 50, True)

#main()