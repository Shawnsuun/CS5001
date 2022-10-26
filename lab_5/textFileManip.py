from text_method_lib import *

#message for input requirement and available functions
msg = "The input format should be:"
msg += "\t1 alice.txt alice_upper.txt\n"
msg += "\t1 represent the function number you want to call\n"
msg += "\talice.txt represent the input filename, make sure the file exists\n"
msg += "\talice_upper.txt represent the output filename\n"
msg += "\t3rd argumrnt is not needed if the function have no out_file argument\n"
msg += "Available functions:\n"
msg += "\t1. all_upper_case(in_file, out_file):\n"
msg += "\t\tconverts everything in in_file to upper case and saves it in out_file\n"
msg += "\t2. remove_a_word(in_file, out_file)\n"	
msg += "\t\tinput a word, removes it from the input file, and writes in out_file\n"
msg += "\t3. reverse_file(in_file, out_file)\n"
msg += "\t\treverses the content of in_file by word not letter, writes it out as out_file\n"
msg += "\t4. pattern_count(in_file)\n"
msg += "\t\tinput a word and prints how many time that pattern occurs\n"
msg += "\t5. encode_file(in_file, out_file)\n"
msg += "\t\tencode the in_file by shifting letters backward 1, saves it in out_file\n"
msg += "\t6. decode_file(in_file, out_file)\n"
msg += "\t\tdecode the in_file by shifting letters backward 1, saves it in out_file\n"
msg += "\t7. complex_encode_file(in_file, out_file)\n"
msg += "\t\tencode the in_file by a dynamic shift of letters and reverse, saves it in out_file\n"
msg += "\t8. complex_decode_file(in_file, out_file)\n"
msg += "\t\tdecode the in_file by a dynamic shift of letters and reverse, saves it in out_file\n"
msg += "\t9. count_all_words(in_file)\n"
msg += "\t\tcount word number of the in_file\n"
msg += "\t10. diagonal_text(in_file, out_file)\n"
msg += "\t\tconverts contents in in_file to diagonal text and saves it in out_file\n"
msg += "\tYou need to input 2 or 3 arguments, separated by a space\n"


#prints a usage message on how the program should be called and lists the available functions and what they do
def usage_msg():
	print(msg)

#CLI main menu content
menu = "Please enter a function number, input filename and output filename(if any), separated by a space:\n"
menu += "(format: 1 alice.txt alice_upper.txt)\n"
menu += "1. Change all letters to uppercas in file\n"
menu += "2. Remove a word\n"
menu += "3. Reverse all the words\n"
menu += "4. Count word pattern\n"
menu += "5. Encode file\n"
menu += "6. Decode file\n"
menu += "7. Complex encode file\n"
menu += "8. Complex decode file\n"
menu += "9. Count all words\n"
menu += "10. Create diagonal text\n"
menu += "Enter q to quit\n"

#checks to make sure the correct number of arguments were given, reads in the file
#processes based on the function requested and creates the output
#If a problem occurs, print a usage message explaining what functions are available and how to use the program
def main():
	running = True
	ouput_funcs = ['1', '2', '3', '5', '6', '7', '8', '10']
	while running:
		user_input = input(menu)
		if user_input == "q":
			break
		try:
			# parse user input and get arguments		
			input_args = user_input.split(' ')
			fun_call = input_args[0]
			in_file = input_args[1]
			if fun_call in ouput_funcs:
				out_file = input_args[2]

			if fun_call == "1":
				all_upper_case(in_file, out_file)
			elif fun_call == "2":
				remove_a_word(in_file, out_file)
			elif fun_call == "3":
				reverse_file(in_file, out_file)
			elif fun_call == "4":
				pattern_count(in_file)
			elif fun_call == "5":
				encode_file(in_file, out_file)
			elif fun_call == "6":
				decode_file(in_file, out_file)
			elif fun_call == "7":
				complex_encode_file(in_file, out_file)
			elif fun_call == "8":
				complex_decode_file(in_file, out_file)
			elif fun_call == "9":
				count_all_words(in_file)
			elif fun_call == "10":
				diagonal_text(in_file, out_file)
			else:
				usage_msg()
			if fun_call in ouput_funcs:
				print(f"File {out_file} has been successfully created\n")
		#handle file not found errors
		except FileNotFoundError:
			print("\nError Message:")
			print(f"File {in_file} not found\n")
		#handle other input errors
		except BaseException:
			print("\nError Message:")
			print("Your input is not valid please check the input format")
			usage_msg()


#Call main function
main()



