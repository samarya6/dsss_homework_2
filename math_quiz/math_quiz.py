import random

# Constants
MIN_NUMBER1 = 1
MAX_NUMBER1 = 10
MIN_NUMBER2 = 0
MAX_NUMBER2 = 10
NUM_QUESTIONS = 5


def generate_random_integer(min_val, max_val):
    """
    Generates a random integer between min_val and max_val inclusive.
    """
    return random.randint(min_val, max_val)


def choose_random_operator():
    """
    Chooses an random operator from the list.
    """
    return random.choice(['+', '-', '*'])


def solve_problem(num1, num2, operator):
    """
    Creates and shows a math problem, and then calculates the answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer


def math_quiz():
    """
    Generates "NUM_QUESTIONS" questions and gives a final feedback of score.
    """
    score = 0

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(NUM_QUESTIONS):
        num1 = generate_random_integer(MIN_NUMBER1, MAX_NUMBER1)
        num2 = generate_random_integer(MIN_NUMBER2, MAX_NUMBER2)
        operator = choose_random_operator()

        problem, answer = solve_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nGame over! Your score is: {score}/{NUM_QUESTIONS}")


if __name__ == "__main__":
    math_quiz()
