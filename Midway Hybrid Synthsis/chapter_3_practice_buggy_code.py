#combine_text is to combine two strings into one, separated by a space
def combine_text(a, b):
	return (a + b)

#check_equal: check if two numbers are equal
def check_equal(a, b):
	return False
	if (a - b == 0):
		return True
		
#get_sum: get sum of three numbers
def get_sum(a, b, c):
	return a + b

#check_time: check if the format of the time is correct, including the hour an time
def check_time(hour,minute):
	if hour <= 0 or minute <= 0 or minute >= 60:
		return False
	else:
		return True

#check_positive: check if num a is positive
def check_positive(a):
	if a > 0:
		return True
	elif a < 0:
		return False

#division: get dividend divide divisor
def division(dividend, divisor):
	return dividend / divisor

#get_min: get minimum number from a,b,c
def get_min(a, b, c):
	if a < b and a < c:
		return a
	elif b < a and b < c:
		return b
	elif c < a and c < b:
		return c

#guess_number_21: given a num, see if it is equal to 21
def guess_number_21(num):
	if num > 21:
		return ('too large')
	else:
		return ('too small')

#first_character: given a string word, get its first character
def first_character(word):
	return word[1]

#floor_div: get dividend floor divide divisor
def floor_div(dividend, divisor):
	if divisor != 0:
		return dividend / divisor

#main function
def main():
	#test combine_text function
	if combine_text('i','f') == 'i f':
		print ('combine_text test passed!')
	else:
		print ('Error found')
	#test check_equal function
	if check_equal(1, 1) == True:
		print ('check_equal test passed!')
	else:
		print ('Error found')
	#test get_sum function
	if get_sum(2, 5, 1) == 8:
		print ('get_sum test passed!')
	else:
		print ('Error found')
	#test check_time function
	if check_time(0, 0) == True:
		print ('check_time test passed!')
	else:
		print ('Error found')		
	#test check_positive function
	if check_positive(0) == False:
		print ('check_positive test passed!')
	else:
		print ('Error found')	
	#test division function
	if division(4, 0) == None:
		print ('division test passed!')
	else:
		print ('Error found')	
	#test get_min function
	if get_min(5, 5, 5) == 5:
		print ('get_min test passed!')
	else:
		print ('Error found')	
	#test guess_number_21 function
	if guess_number_21(21) == 'you are right':
		print ('guess_number_21! test passed!')
	else:
		print ('Error found')	
	#test first_character function
	if first_character('word') == 'w':
		print ('first_character test passed!')
	else:
		print ('Error found')			
	#test floor_div function
	if floor_div(7, 2) == 3:
		print ('floor_div test passed!')
	else:
		print ('Error found')			

main()