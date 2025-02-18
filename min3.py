import random  # Import the random module for generating random numbers and choosing random operators
import time  # Import the time module for measuring the time taken to complete the quiz

OPERATORS = ["+", "-", "/", "*"]  # List of arithmetic operators to choose from
MIN_OPERAND = 3  # Minimum value for the operands in the problems
MAX_OPERAND = 12  # Maximum value for the operands in the problems
TOTAL_PROBLEMS = 3  # Number of math problems in the quiz

def generate_problem():
    """Generates a random math problem and returns the expression and the answer."""
    left = random.randint(MIN_OPERAND, MAX_OPERAND)  # Generate a random integer for the left operand
    right = random.randint(MIN_OPERAND, MAX_OPERAND)  # Generate a random integer for the right operand
    operator = random.choice(OPERATORS)  # Choose a random operator from the list of operators

    expr = str(left) + " " + operator + " " + str(right)  # Create the math expression as a string
    answer = eval(expr)  # Evaluate the expression to get the correct answer
    print(expr)  # Print the expression to the console
    return expr, answer  # Return the expression and the answer as a tuple

wrong = 0  # Initialize a variable to keep track of the number of wrong answers

input("Press Enter to start!")  # Prompt the user to press Enter to begin the quiz
print("-----------------")  # Print a separator line

start_time = time.time()  # Record the starting time of the quiz

for i in range(TOTAL_PROBLEMS):  # Loop through the specified number of problems
    expr, answer = generate_problem()  # Generate a math problem

    while True:  # Inner loop to keep asking for the answer until it's correct
        guess = input("Problem #" + str(i + 1) + ": " + expr + "=")  # Get the user's guess
        if guess == str(answer):  # Check if the guess is correct (convert answer to string for comparison)
            break  # Exit the inner loop if the guess is correct
        wrong += 1  # Increment the wrong answer counter if the guess is incorrect

end_time = time.time()  # Record the ending time of the quiz
total_time = end_time - start_time  # Calculate the total time taken to complete the quiz

print("-----------------")  # Print a separator line
print("Nice work! You finished in", total_time, "seconds")  # Print the total time taken to complete the quiz