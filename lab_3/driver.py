import shapelib
import turtle

def scene1():
	shapelib.clear_screen()
	shapelib.draw_skyline(90,40)
	shapelib.draw_houses(40,25)
	shapelib.block(0,0,100,50, True)
	shapelib.goto(x = -100, y = 0)
	shapelib.draw_houses(30,30)
	shapelib.goto(x = -10, y = -50)
	shapelib.add_text("Portland","CityView")


def scene2():
	shapelib.clear_screen()
	shapelib.draw_lighthouse()
	shapelib.goto(x = 125, y = 0)
	shapelib.draw_house(45,60)
	shapelib.goto(x = 100, y = 0)
	shapelib.draw_house(60,70)
	shapelib.goto(x = 150, y = 0)
	shapelib.draw_house(40,60)
	shapelib.goto(x = -10, y = -70)
	shapelib.add_text("Portland","Lighthouse")

flag = True
while flag == True:
	selection = input("which scene would you like to see?(input 1 or 2)\n")
	if selection == '1':
		scene1()
	elif selection == '2':
		scene2()
	else:
		print("please input 1 or 2")
