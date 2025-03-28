# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Format the input to left justify.
spaces = 50 - len(message)
message = message + " " * spaces

# Print the result.
print(message)