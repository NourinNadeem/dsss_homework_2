import unittest
from math_quiz import random_integer_generator, random_operator_generator, random_problem_generator


class TestMathGame(unittest.TestCase):
    
    # Test if random numbers generated are within the specified range
    def test_random_integer_generator(self):
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    # Test for random_operator_generator
    def test_random_operator_generator(self):
        for _ in range(1000):
            operator = random_operator_generator()
            self.assertIn(operator, ['+', '-', '*'])
        pass

    def test_random_problem_generator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 3, '-', '4 - 3', 1),
                (7, 3, '*', '7 * 3', 21),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = random_problem_generator(num1, num2, operator)
                self.assertEqual(problem, expected_problem)  # Check if problem string matches
                self.assertEqual(answer, expected_answer)     # Check if the answer is correct
            pass

if __name__ == "__main__":
    unittest.main()
