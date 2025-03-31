# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Remove the suffix "less".
if message.endswith("less"):
    message = message[0:-4]

# Print the result.
print(message)