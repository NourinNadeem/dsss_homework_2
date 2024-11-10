import random

def random_integer_generator(min, max):
    """
    Generate a random integer between min and max.
    Parameters:
        min (int): The minimum value the random integer can be.
        max (int): The maximum value the random integer can be.
    Returns:
        random_integer(int): A random integer between min and max.
    """
    return random.randint(min, max)

def random_operator_generator():
    """
    Generate a random operator from '+', '-', and '*'.
    
    Returns:
        random_operator (str): A randomly chosen operator.
    """
    return random.choice(['+', '-', '*'])

def random_problem_generator(n1, n2, operator):
    """
    Generate a mathematical problem and its solution.

    Parameters:
        n1 (int): The first number in the problem.
        n2 (int): The second number in the problem.
        operator (str): The operator to use for the operation.

    Returns:
        equation (tuple): A tuple containing the problem as a string and the correct
        answer.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+': answer = n1 + n2
    elif operator == '-': answer = n1 - n2
    else: answer = n1 * n2
    return problem, answer

def math_quiz():
    """
    Main function to run the math quiz game.
    
    The game will present a series of math problems and ask the user to solve them.
    The user's score will be calculated based on correct answers.
    """
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = random_integer_generator(1, 10)
        n2 = random_integer_generator(1, 5)
        operator = random_operator_generator()

        problem, correct_answer = random_problem_generator(n1, n2, operator)
        print(f"\nQuestion: {problem}")
         # Error handling for user input
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        # Check the answer and update the score
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")
    
    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
