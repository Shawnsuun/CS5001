from collections import deque

# create a new deque object as a stack for pancakes
plate = deque()

def make_pancake(pancake):
	"""
	make a pancake and put it on the top of the plate(or top pancake)

	Keyword arguments:

	pancake -- a string of the pancake name

	"""
	plate.append(pancake)
	print(f"{pancake} pancake is made")
	print("-------------------------------------------")


def top_pancake():
	"""
	see the pancake on the top and print it

	"""	
	# the plate[-1] is similar as peek(), it is used to get the top item of the stack
	print(f"top pancake is " + plate[-1])
	print("-------------------------------------------")


def serve_pancakes(n):
	"""
	pick top n pancakes to serve

	Keyword arguments:

	n -- number of top pancakes to serve

	"""
	# loop top n pancakes
	for i in range (0, n):
		# if the stack plate is not empty, pop the top pancake and give a message of serving
		if plate:
			print(plate.pop() + " pancake is served")
		# if the stack plate is empty, give a message of no pancake, stop trying to serve pancakes
		else:
			print("no pancake left")
			break
	print("-------------------------------------------")


def check_plate():
	"""
	print all the pancakes on the plate from bottom to top

	"""
	# if the stack plate is not empty, loop the stack and print all pancakes
	if plate:
		print("here are pancakes from bottom to top:")
		for pancake in plate:
			print(pancake + " pancake")
	# if the stack plate is empty, give a message
	else:
		print("Plate is empty")
	print("-------------------------------------------")


def test():
	"""
	use a combination of functions to test the outcome and the supposed result

	"""	
	make_pancake('strawberry')
	make_pancake('plain')
	make_pancake('apple')
	top_pancake()
	check_plate()
	serve_pancakes(2)
	top_pancake()
	serve_pancakes(2)
	make_pancake('strawberry')
	make_pancake('plain')
	serve_pancakes(1)
	top_pancake()
	serve_pancakes(2)
	serve_pancakes(2)
	serve_pancakes(2)


def main():
	"""
	main function

	"""		
	test()


main()