from fill_lib import *

# main menu content
menu = "1. Fill quadrant top left with horizontal bars\n"
menu += "2. Fill quadrant top right with zebra stripes\n"
menu += "3. Fill quadrant bottom left with stairs\n"
menu += "4. Fill quadrant bottom right with wallpaper pattern\n"
menu += "5. Fill all quadrants\n"
menu += "6. Clear screen\n"
menu += "7. Quit\n"
menu += "8. Add text\n"

# set fill status to false for all quads
def reset_fill_status():
	global quad1
	global quad2
	global quad3
	global quad4
	quad1 = False
	quad2 = False
	quad3 = False
	quad4 = False

# clear screen and redraw frame
def init_settings():
	clear_screen()
	set_max_speed()
	frame(window_size)

# draw function to draw patterns based on quad status
def draw_quad():
	fill(quad1, quad2, quad3, quad4, window_size)
	reset_fill_status()

# boolean to decide if the program is running
running = True

# draw patterns based on quad status
window_size = float(input("Please set window size:\n"))
init_settings()
while running:
	reset_fill_status()
	selection = input(menu) 
	if selection == "1":
		quad1 = True
		draw_quad()
	elif selection == "2":
		quad2 = True
		draw_quad()
	elif selection == "3":
		quad3 = True
		draw_quad()
	elif selection == "4":
		quad4 = True
		draw_quad()
	elif selection == "5":
		quad1 = True
		quad2 = True
		quad3 = True
		quad4 = True
		draw_quad()
	elif selection == "6":
		init_settings()
	elif selection == "7":
		running = False
	elif selection == "8":
		add_text(window_size)
	else:
		print ("Please select an option from 1 ~ 8!")






