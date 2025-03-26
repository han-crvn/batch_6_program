# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Change the first letter of the word to uppercase and the remaining to lowercase.
title_message = ""

for word in message.split():
    if word:
        title_message += word[0].upper() + word[1:].lower() + " "

# Print the result.
print(title_message)
