from queue import *


#additional_space: an int variable represent available place for the course
additional_space = 0

#waitlist: a FIFO queue to save students in waitlist, max size is 5
waitlist = Queue(maxsize = 5)


def add_to_waitlist(student):
	"""
	add a student to the waitlist

	Keyword arguments:

	student -- a string of the student name

	"""
	# enqueue the student in the queue waitlist
	waitlist.put(student)


def print_waitlist():
	"""
	print all the students on the waitlist

	"""
	print("student in waitlist:")
	# if the queue waitlist is empty, give a message of no students
	if waitlist.empty():
		print("no student in waitlist")
	
	# if the queue waitlist is not empty, traverse waitlist queue and print all names
	for name in waitlist.queue:
		print(name)
	print("-------------------------------------------")


def drop_class(n):
	"""
	n students drop the class

	additional space will be plus n 

	letting students on the waitlist register for the course automatically
	
	Keyword arguments:

	n -- an int for the number of students dropping the class	

	"""
	# globalize variable additional_space
	global additional_space
	print(f"{n} students has droped the class.")

	# update additional_space
	additional_space += n

	# dequeue until waitlist is empty or no additional space
	while additional_space > 0 and not waitlist.empty():
		# dequeue the waitlist
		student = waitlist.get()

		# register the dequeued student and update additional space
		additional_space -= 1;	
		print(f"{student} from waitlist is registered, available space for register: {additional_space}.")
	print("-------------------------------------------")
	print_waitlist()


def request_register(student):

	"""
	Send a request for course registration, in this function: 

	If there is available space for the course, register for the student, available_space minus 1

	If there is no available space of course and the waitlist is not full, add student to waitlist

	If the waitlist is full, give a message that the waitlist is full. 

	Keyword arguments:

	student -- an string student for the name of student to be registered	

	"""
	global additional_space
	print(f"{student} send a request for register.")
	# there is no available space for the course
	if additional_space == 0:
		print("There is no space for the course")
		# waitlist is full
		if waitlist.full():
			print("No space in waitlist, please try later.")
		# waitlist is not full, add student to the waitlist
		else:
			add_to_waitlist(student)
			print(f"{student} have been in waitlist")
	# there is available space for the course
	else:
		additional_space -= 1
		print(f"{student} is registered.")
	print("-------------------------------------------")
	print_waitlist()


def test():
	"""
	use a combination of functions to test the outcome and the supposed result

	"""	
	drop_class(1)
	request_register('student1')
	request_register('student2')
	request_register('student3')
	request_register('student4')
	request_register('student5')
	drop_class(2)
	request_register('student6')
	request_register('student7')
	request_register('student8')
	drop_class(1)
	request_register('student9')
	request_register('student10')
	drop_class(1)

def main():
	"""
	main function

	"""		
	test()


main()