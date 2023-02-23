import unittest
import iteration_math

class IterationTest(unittest.TestCase):
    """
    test cases for all functions in iteration_math

    """  
    def test_iteration_fact(self):
        self.assertEqual(iteration_math.iteration_fact(1), 1)
        self.assertEqual(iteration_math.iteration_fact(3), 6)
        self.assertEqual(iteration_math.iteration_fact(5), 120)
        self.assertEqual(iteration_math.iteration_fact(7), 5040)


    def test_iteration_sqr_sum(self):
        self.assertEqual(iteration_math.iteration_sqr_sum(1), 1)
        self.assertEqual(iteration_math.iteration_sqr_sum(3), 14)
        self.assertEqual(iteration_math.iteration_sqr_sum(5), 55)
        self.assertEqual(iteration_math.iteration_sqr_sum(7), 140)


    def test_iteration_fib(self):
        self.assertEqual(iteration_math.iteration_fib(1), 1)
        self.assertEqual(iteration_math.iteration_fib(3), 2)
        self.assertEqual(iteration_math.iteration_fib(5), 5)
        self.assertEqual(iteration_math.iteration_fib(7), 13)


    def test_iteration_tri_fib(self):
        self.assertEqual(iteration_math.iteration_tri_fib(3), 3)
        self.assertEqual(iteration_math.iteration_tri_fib(5), 11)
        self.assertEqual(iteration_math.iteration_tri_fib(7), 37)
        self.assertEqual(iteration_math.iteration_tri_fib(9), 125)


    def test_iteration_pow(self):
        self.assertEqual(iteration_math.iteration_pow(3, 3), 27)
        self.assertEqual(iteration_math.iteration_pow(2, 5), 32)
        self.assertEqual(iteration_math.iteration_pow(10, 3), 1000)
        self.assertEqual(iteration_math.iteration_pow(9, 3), 729)


    def test_iteration_search(self):
        nums = [1,3,5,23,45,56,67,89,123,556,890,1002]
        self.assertEqual(iteration_math.iteration_search(nums, 4), -1)
        self.assertEqual(iteration_math.iteration_search(nums, 23), 3)
        self.assertEqual(iteration_math.iteration_search(nums, 123), 8)
        self.assertEqual(iteration_math.iteration_search(nums, 1002), 11)


    def test_iteration_binary_search(self):
        nums = [1,3,5,23,45,56,67,89,123,556,890,1002]
        self.assertEqual(iteration_math.iteration_binary_search(nums, 4), -1)
        self.assertEqual(iteration_math.iteration_binary_search(nums, 23), 3)
        self.assertEqual(iteration_math.iteration_binary_search(nums, 123), 8)
        self.assertEqual(iteration_math.iteration_binary_search(nums, 1002), 11)


unittest.main()