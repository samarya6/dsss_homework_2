import unittest
from .math_quiz import generate_random_integer, choose_random_operator, solve_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        """
        Test if random numbers generated are within the specified range.
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val,
                            f"Generated number {rand_num} out of range [{min_val}, {max_val}]")

    def test_choose_random_operator(self):
        """
        Test if random operator generated are same as expected.
        """
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random operators
            rand_operator = choose_random_operator()
            self.assertIn(rand_operator, operators,
                          f"Chosen operator {rand_operator} is not in the list of expected operators")

    def test_solve_problem(self):
        """
        Test if the solve_problem function returns the correct problem description and answer.
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (1, 10, '+', '1 + 10', 11),
            (10, 0, '-', '10 - 0', 10),
            (5, 7, '-', '5 - 7', -2),
            (4, 3, '*', '4 * 3', 12),
            (4, 0, '*', '4 * 0', 0),
            # More tests are even better.
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = solve_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem,
                             f"Generated problem description {problem} does not match expected {expected_problem}")
            self.assertEqual(answer, expected_answer,
                             f"Generated answer {answer} does not match expected {expected_answer}")


if __name__ == "__main__":
    unittest.main()
