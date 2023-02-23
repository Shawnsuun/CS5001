import unittest
import recursion_math

class RecursionTest(unittest.TestCase):
    """
    test cases for all functions in recursion_math

    """    
    def test_recursion_fact(self):
        self.assertEqual(recursion_math.recursive_fact(1), 1)
        self.assertEqual(recursion_math.recursive_fact(3), 6)
        self.assertEqual(recursion_math.recursive_fact(5), 120)
        self.assertEqual(recursion_math.recursive_fact(7), 5040)


    def test_recursion_sqr_sum(self):
        self.assertEqual(recursion_math.recursive_sqr_sum(1), 1)
        self.assertEqual(recursion_math.recursive_sqr_sum(3), 14)
        self.assertEqual(recursion_math.recursive_sqr_sum(5), 55)
        self.assertEqual(recursion_math.recursive_sqr_sum(7), 140)


    def test_recursion_fib(self):
        self.assertEqual(recursion_math.recursive_fib(1), 1)
        self.assertEqual(recursion_math.recursive_fib(3), 2)
        self.assertEqual(recursion_math.recursive_fib(5), 5)
        self.assertEqual(recursion_math.recursive_fib(7), 13)


    def test_recursion_tri_fib(self):
        self.assertEqual(recursion_math.recursive_tri_fib(3), 3)
        self.assertEqual(recursion_math.recursive_tri_fib(5), 11)
        self.assertEqual(recursion_math.recursive_tri_fib(7), 37)
        self.assertEqual(recursion_math.recursive_tri_fib(9), 125)


    def test_recursion_pow(self):
        self.assertEqual(recursion_math.recursive_pow(3, 3), 27)
        self.assertEqual(recursion_math.recursive_pow(2, 5), 32)
        self.assertEqual(recursion_math.recursive_pow(10, 3), 1000)
        self.assertEqual(recursion_math.recursive_pow(9, 3), 729)


    def test_recursion_quick_pow(self):
        self.assertEqual(recursion_math.recursive_quick_pow(3, 3), 27)
        self.assertEqual(recursion_math.recursive_quick_pow(2, 5), 32)
        self.assertEqual(recursion_math.recursive_quick_pow(10, 3), 1000)
        self.assertEqual(recursion_math.recursive_quick_pow(9, 3), 729)


    def test_recursion_search(self):
        nums = [1,3,5,23,45,56,67,89,123,556,890,1002]
        self.assertEqual(recursion_math.recursive_search(nums, 0, 4), -1)
        self.assertEqual(recursion_math.recursive_search(nums, 0, 23), 3)
        self.assertEqual(recursion_math.recursive_search(nums, 0, 123), 8)
        self.assertEqual(recursion_math.recursive_search(nums, 0, 1002), 11)


    def test_recursive_binary_search(self):
        nums = [1,3,5,23,45,56,67,89,123,556,890,1002]
        self.assertEqual(recursion_math.recursive_binary_search(nums, 0, 11, 4), -1)
        self.assertEqual(recursion_math.recursive_binary_search(nums, 0, 11, 23), 3)
        self.assertEqual(recursion_math.recursive_binary_search(nums, 0, 11, 123), 8)
        self.assertEqual(recursion_math.recursive_binary_search(nums, 0, 11, 1002), 11)


unittest.main()