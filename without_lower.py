# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Change the input to lowercase.
lower_message = ""

for char in message:
    if "A" <= char <= "Z":
        lower_message += chr(ord(char) + 32)
    else:
        lower_message += char

# Print the result.
print(lower_message)