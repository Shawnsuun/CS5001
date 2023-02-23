def fact(n):
	#This is the base case
	if n == 1:
		return 1		
	#recursive call
	return n * fact(n - 1);

print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))


def sqr_sum(n):
	if n == 1:
		return 1
	return n * n + sqr_sum(n - 1)

print(sqr_sum(1))
print(sqr_sum(2))
print(sqr_sum(3))
print(sqr_sum(4))
print(sqr_sum(5))


def fib(n):
	if n <= 1:
		return n 
	return fib(n - 1) + fib(n - 2)

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))


def tri_fib(n):
	if n <= 1:
		return n 
	if n == 2:
		return 3
	return fib(n - 1) + fib(n - 2) + fib(n - 3)

print(tri_fib(1))
print(tri_fib(2))
print(tri_fib(3))
print(tri_fib(4))
print(tri_fib(5))

def pow(x, n):
	if n == 0:
		return 1
	return pow(x, n - 1) * x

print(pow(2, 1))
print(pow(2, 2))
print(pow(2, 3))
print(pow(2, 4))
print(pow(2, 5))

def quick_pow(x, n):
	# base case
	if n == 0:
		return 1
	# why use a variable temp here:
	# if use quick_pow(x, int(n / 2)) * quick_pow(x, int(n / 2)) instead
	# it is two recursion calls and will double the time used
	temp = quick_pow(x, int(n / 2))
	if n % 2 == 1:
		return temp * temp * x
	return temp * temp

print(quick_pow(2, 1))
print(quick_pow(2, 2))
print(quick_pow(2, 3))
print(quick_pow(2, 4))
print(quick_pow(2, 5))



nums = [1,2,3,5,7,8,10]

def recursive_search(nums, index, target):
	'''
	single traverse search, time efficiency O(N)

	'''
	if index == len(nums):
		return -1
	if nums[index] == target:
		return index
	return recursive_search(nums, index + 1, target)

print(recursive_search(nums, 0, 1))
print(recursive_search(nums, 0, 3))
print(recursive_search(nums, 0, 4))
print(recursive_search(nums, 0, 7))


def recursive_binary_search(nums, left, right, target):
	'''
	a binary search, time efficiency O(logN)


	'''
	#base case for target not found
	if left > right:
		return -1
	#base case for finding the target
	mid = int((left + right) / 2)
	if (nums[mid] == target):
		return mid
	elif nums[mid] > target:
		return recursive_binary_search(nums, left, mid - 1, target)
	else:
		return recursive_binary_search(nums, mid + 1, right, target)

print(recursive_binary_search(nums, 0, 6, 1))
print(recursive_binary_search(nums, 0, 6, 3))
print(recursive_binary_search(nums, 0, 6, 4))
print(recursive_binary_search(nums, 0, 6, 7))