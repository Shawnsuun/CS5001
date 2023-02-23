def recursive_fact(n):
	'''
	calculate the fact of number n, which is n * (n - 1) * ... * 3 * 2 *  1

	time efficiency is O(N) since there is n recursion calls

	key arguments:

	n -- the number for fact operation	

	'''	
	#This is the base case
	if n == 1:
		return 1		
	#recursive call
	return n * recursive_fact(n - 1);


def recursive_sqr_sum(n):
	'''
	calculate the square sum from 1 to number n, which is f(n) = 1^2 + 2^2 + 3^2 + 4^2 + … + n^2

	time efficiency is O(N) since there is n recursion calls

	key arguments:

	n -- the number for sqr_sum operation	

	'''		
	#base case
	if n == 1:
		return 1
	#recursive call
	return n * n + recursive_sqr_sum(n - 1)


def recursive_fib(n):
	'''
	calculate fibonacci number from 1 to number n, which is F(0) = 0, F(1) = 1, ... ,F(n) = F(n - 1) + F (n - 2) 

	time efficiency is O(2^N) since there are 2 recursion calls in each recursion calls

	key arguments:

	n -- the index for fibonacci num	

	'''	
	# base case for n = 0, 1	
	if n <= 1:
		return n 
	#recursive call
	return recursive_fib(n - 1) + recursive_fib(n - 2)


def recursive_tri_fib(n):
	'''
	calculate triple fibonacci number from 1 to number n

	which is F(0) = 0, F(1) = 1, F(2) = 2, ... ,F(n) = F(n - 1) + F (n - 2)  + F (n - 3)

	time efficiency is O(3^N) since there are 3 recursion calls in each recursion calls

	key arguments:

	n -- the index for triple fibonacci num	

	'''	
	# base case for n = 0, 1, 2	
	if n <= 2:
		return n 
	#recursive call
	return recursive_tri_fib(n - 1) + recursive_tri_fib(n - 2) + recursive_tri_fib(n - 3)


def recursive_pow(x, n):
	'''
	recursion to get x power n

	time efficiency is O(N) since the traverse takes N recursive calls

	key arguments:

	x -- base of power operation	

	n -- the times for power operation	

	'''	
	# base case
	if n == 0:
		return 1
	#recursive call
	return recursive_pow(x, n - 1) * x


def recursive_quick_pow(x, n):
	'''
	recursion to get x power n in a quicker way

	time efficiency is O(logN) 

	since in each recursion call, n is halved, takes about log2N recursive calls

	key arguments:

	x -- base of power operation	

	n -- the times for power operation	

	'''	

	# base case
	if n == 0:
		return 1
	# why use a variable temp here:
	# if use quick_pow(x, int(n / 2)) * quick_pow(x, int(n / 2)) instead
	# if n is odd, additional x need to be mutiplied
	# it is two recursion calls and will increase the time used
	# use int(n / 2) to round down
	temp = recursive_quick_pow(x, int(n / 2))
	if n % 2 == 1:
		return temp * temp * x
	# if n is even, no additional x need to be mutiplied
	return temp * temp


def recursive_search(nums, index, target):

	'''
	search a target number in a sorted list

	time efficiency is O(N) since there are n recursion calls

	key arguments:

	nums -- a sorted number list

	index -- curent index in nums

	target -- target number to be searched in the list nums	

	'''	
	# base case for target not found
	if index == len(nums):
		return -1
	# base case for target found	
	if nums[index] == target:
		return index
	# recursive calls
	return recursive_search(nums, index + 1, target)


def recursive_binary_search(nums, left, right, target):
	'''
	a binary search in sorted list

	time efficiency O(logN) 

	each time we cut half of the search range

	it would take about log2n comparations to get the target at most

	In big-O notation, the time efficiency is O(logN)

	key arguments:
	
	left -- left boundry of searching range

	right -- right boundry of searching range

	nums -- a sorted number list

	target -- target number to be searched in the list nums

	'''
	#base case for target not found
	if left > right:
		return -1
	#base case for finding the target
	mid = int((left + right) / 2)
	if (nums[mid] == target):
		return mid
	# target at the left half of the range
	# narrow the searching range to left half, recursive call to search left half
	elif nums[mid] > target:
		return recursive_binary_search(nums, left, mid - 1, target)
	# target at the right half of the range
	# narrow the searching range to right half , recursive call to search right half
	else:
		return recursive_binary_search(nums, mid + 1, right, target)
