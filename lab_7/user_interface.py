from rshapes import*
import sys

#CLI main menu content
menu = "Please select a recursive drawing:\n"
menu += "1. Psychedelic boxes\n"
menu += "2. Bull’s Eye\n"
menu += "3. Inward Turning Spiral\n"
menu += "4. Box Tree\n"
menu += "5. Realistic tree\n"
menu += "6. Snowflake\n"
menu += "7. Forest Drawing\n"
menu += "Enter q to quit\n"

#main function
def main():
	running = True
	while running:
		user_input = input(menu)
		if user_input == "q":
			break
		valid_input = ['1','2','3','4','5','6']
		try:
			# parse user input and get arguments	
			if user_input in valid_input:
				x = float(input("please enter x:\n"))
				y = float(input("please enter y:\n"))
				size = float(input("please enter size/radius/length:\n"))
				if user_input == '1' or user_input == '2' or user_input == '4':
					scale_down = float(input("please enter scale down:\n"))
					min_size = float(input("please enter min size:\n"))
				elif user_input == '5' or user_input == '6':
					scale_down = float(input("please enter scale down:\n"))
					level = float(input("please enter the levels of tree:\n"))			
			# set max speed
			max_speed()
			# draw different drawings based on user selection
			if user_input == "1":
				clear_screen()
				boxes(x, y, size, scale_down, min_size)
			elif user_input == "2":
				clear_screen()
				circles(x, y, size, scale_down, min_size)				
			elif user_input == "3":
				clear_screen()
				drawSpiral(x, y, size)
			elif user_input == "4":
				clear_screen()
				boxTree(x, y, size, scale_down, min_size)
			elif user_input == "5":
				clear_screen()
				reset(x, y, 90)
				recursive_tree(size, scale_down, level)
			elif user_input == "6":
				clear_screen()
				snowflake(x, y, size, scale_down, level)
			elif user_input == "7":
				clear_screen()
				forest()
			else:
				print("Your input is not valid, please retry")
		#handle input errors
		except BaseException:
			print("Your input is not valid, please retry")

main()
