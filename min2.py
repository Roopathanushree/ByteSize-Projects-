# Mad Libs Generator

# Load the story from the "story.txt" file
with open("story.txt", "r") as f:
    story = f.read()

# Find the placeholder words in the story (words enclosed in <>)
words = set()  # Use a set to store the words (sets avoid duplicates)
start_of_word = -1  # Initialize the starting position of a word to -1

target_start = "<"  # Define the start delimiter for placeholder words
target_end = ">"  # Define the end delimiter for placeholder words

# Iterate through the story character by character
for i, char in enumerate(story):
    if char == target_start:  # If we find the start delimiter
        start_of_word = i  # Record the starting position

    if char == target_end and start_of_word != -1:  # If we find the end delimiter and a start was found
        word = story[start_of_word : i + 1]  # Extract the word (including the delimiters)
        words.add(word)  # Add the word to the set
        start_of_word = -1  # Reset the starting position

# Get user input for each placeholder word
answers = {}  # Create a dictionary to store the user's answers
for word in words:  # Iterate through the set of unique placeholder words
    answer = input("Enter a word for " + word + ": ")  # Prompt the user for a word
    answers[word] = answer  # Store the user's answer in the dictionary

# Replace the placeholder words in the story with the user's answers
for word in words:  # Iterate through the set of unique placeholder words
    story = story.replace(word, answers[word])  # Replace each placeholder with the corresponding answer

# Print the completed Mad Lib story
print(story)