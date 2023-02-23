def iteration_fact(n):
	'''
	calculate the fact of number n, which is n * (n - 1) * ... * 3 * 2 *  1

	single time traverse n numbers in list

	time efficiency is O(N) since the traverse takes N operation, same as argument n

	key arguments:

	n -- the number for fact operation	

	'''
	factorial = 1
	# traverse number 1 ~ n
	for i in range(1, n + 1):
		factorial = factorial * i
	return factorial



def iteration_sqr_sum(n):
	'''
	calculate the square sum from 1 to number n, which is f(n) = 1^2 + 2^2 + 3^2 + 4^2 + … + n^2

	single time traverse n numbers in list, there are 2 operations

	time efficiency is O(N) since the traverse takes 2N operation, about twice as argument n

	key arguments:

	n -- the number for sqr_sum operation	

	'''	
	sum = 0
	i = 1
	while i <= n:
		sum += i * i
		i += 1
	return sum


def iteration_fib(n):
	'''
	calculate fibonacci number from 1 to number n, which is F(0) = 0, F(1) = 1, ... ,F(n) = F(n - 1) + F (n - 2) 

	single time traverse n numbers in list, each number have 3 operations

	time efficiency is O(N) since the traverse takes about 3N operation

	key arguments:

	n -- the index for fibonacci num	

	'''	
	# condition for n = 0, 1
	if n <= 1:
		return n

	# a list save 2 numbers F(n - 1) and F (n - 2), it is used to calculate F(n)
	cache = [0, 1]
	# traverse 2 ~ n
	for i in range(2, n + 1):
		#get current fib number
		fib_num = cache[0] + cache[1]
		#update cache to calculate the next fib number
		cache.pop(0)
		cache.append(fib_num)
	return fib_num


def iteration_tri_fib(n):
	'''
	calculate triple fibonacci number from 1 to number n

	which is F(0) = 0, F(1) = 1, F(2) = 2, ... ,F(n) = F(n - 1) + F (n - 2)  + F (n - 3)

	single time traverse n numbers in list, each number have 3 operations

	time efficiency is O(N) since the traverse takes about 3N operation

	key arguments:

	n -- the index for triple fibonacci num	

	'''	
	# condition for n = 0, 1, 2	
	if n <= 2:
		return n
	# a list save 2 numbers F(n - 1), F (n - 2), F (n - 3), it is used to calculate F(n)
	cache = [0, 1, 2]
	# traverse 3 ~ n
	for i in range(3, n + 1):
		fib_num = cache[0] + cache[1] + cache[2]
		cache.pop(0)
		cache.append(fib_num)
	return fib_num



def iteration_pow(x, n):
	'''
	single time traverse each number of 1~n

	time efficiency is O(N) since the traverse takes N operation at most

	key arguments:

	x -- base of power operation	

	n -- the times for power operation	

	'''
	# initial value of result
	power = 1
	# traverse 1 ~ n, update the result
	for i in range(1, n + 1):
		power *= x
	return power


# You do not have to write an iteration_quick_pow(x, n) function 
# since it is much more complicated to use iteration than recursion.


def iteration_search(nums, target):
	'''
	single time traverse each number in list,

	time efficiency is O(N) since the traverse takes N operation at most

	key arguments:

	nums -- a sorted number list

	target -- target number to be searched in the list nums	

	'''
	# traverse the list
	for i in range (0, len(nums)):
		# target found in index i
		if nums[i] == target:
			return i
	# return -1 if target not found
	return -1


def iteration_binary_search(nums, target):
	'''
	a binary search in sorted list

	time efficiency O(logN) 

	each time we cut half of the search range

	it would take about log2n comparations to get the target at most

	In big-O notation, the time efficiency is O(logN)

	key arguments:

	nums -- a sorted number list

	target -- target number to be searched in the list nums

	'''
	# index of initial binary search boundry
	left = 0
	right = len(nums) - 1

	# end the loop if left > right
	while left <= right:
		#middle index of search range
		mid = int((left + right) / 2)

		# target found in index mid
		if (nums[mid] == target):
			return mid
		# target at the right half of the range
		# narrow the searching range to right half 
		elif nums[mid] > target:
			right = mid - 1
		# target at the left half of the range
		# narrow the searching range to left half 
		else:
			left = mid + 1
	# return -1 if target not found
	return -1

