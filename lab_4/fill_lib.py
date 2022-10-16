from base_lib import *

# draws horizontal stripes at the given position equidistant apart based on the block size
def windowSlates(x, y, block_size, width):
	y -= width
	while y < width:
		y += block_size
		goto(x, y + width)
		if y + block_size < width:
			n = y + block_size
		else:
			n = width
		color(rand_color())
		while y < n:
			forward(width)
			y += 0.1
			goto(x, y + width)

# test windowSlates(x, y, block_size, width)
# frame(100)
# windowSlates(0, 100, 5,100)

# creates vertical strips across the screen to fill a given block
def zebra_stripes(x, y, block_size):
	goto(x, y)
	left(90)
	width = y
	x -= width
	while x < width:
		x += block_size
		goto(x + width, y)
		if x + block_size < width:
			n = x + block_size
		else:
			n = width
		color(rand_color())
		while x < n:
			forward(width)
			x += 0.1
			goto(x + width, y)
	right(90)
# test windowSlates(x, y, block_size, width)
# set_max_speed()
# frame(100)
# zebra_stripes(100, 100, 5)

# creates steps from the bottom left to the top right of a block with the given step size
def steps(x, y, block_size, step_size):
	init_x = x
	init_y = y
	while x <= block_size - step_size:
		x += step_size
		y += step_size
		goto(x, y)
		color(rand_color())
		if block_size - x >= step_size:
			forward(step_size)
		else:
			forward(block_size - x)

	x = init_x
	y = init_y - step_size
	left(90)
	while x <= block_size - step_size:
		x += step_size
		y += step_size
		goto(x, y)
		color(rand_color());
		if block_size - y >= step_size:
			forward(step_size)
		else:
			forward(block_size - y)
	right(90)
	reset()

# test steps(x, y, block_size, step_size)
# frame(100)
# steps(0, 0, 100, 7)

# creates a while paper pattern with interlocking circles based on the provided radius. Make sure to stay within the block
def wall_paper(x, y, block_size, radius):
	while y <= block_size - 2 * radius:
		while x <= 2 * block_size - 2 * radius:
			x += radius
			goto(x, y)
			color(rand_color())
			circle(radius)
		x = block_size
		y += radius
		goto(x, y)

# test wall_paper(x, y, block_size, radius)	
# frame(100)	
# wall_paper(100, 0, 100, 5)

# fill quadrants, quad1 ~ quad4 are boolean variables decide which quadrants to fill, window_size is the size of square to be filled
def fill(quad1, quad2, quad3, quad4, window_size):
	if quad1 == True:
		block_size = float(input("Please enter slate width:\n"))
		width = window_size
		windowSlates(0, window_size, block_size, width)
	if quad2 == True:
		block_size = float(input("Please enter stripe width:\n"))
		zebra_stripes(window_size, window_size, block_size)
	if quad3 == True:
		step_size = float(input("Please enter step size:\n"))
		steps(0, 0, window_size, step_size)
	if quad4 == True:
		radius = float(input("Please enter radius:\n"))
		wall_paper(window_size, 0, window_size, radius)

# test fill(quad1, quad2, quad3, quad4, window_size)
# set_max_speed()
# frame(100)
# window_size = 100
# fill(True, True, True, True, 100)

# add text
def add_text(length):
	x = 2 * length + 10
	while x < 2 * length + 300:
		y = 0
		while y < 2 * length:
			goto(x, y)
			color(rand_color()) 
			write("Hello python world!",font = ("Arial", 10)) 
			penup()
			y += 10
		x += 150