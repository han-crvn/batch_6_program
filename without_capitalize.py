# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Change the first letter of the word or sentence to uppercase and the remaining to lowercase.
capitalize_message = message[0].upper() + message[1:].lower()

# Print the result.
print(capitalize_message)