# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ").lower()

# Remove the prefix (the prefix in this program is 'mis').
if message.startswith("mis"):
    message = message[3:]

# Print the result.
print(message)