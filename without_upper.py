# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Format the input to uppercase.
upper_message = ""

for char in message:
    if "a" <= char <= "z":
        upper_message += chr(ord(char) - 32)
    else:
        upper_message += char

# Print the result.
print(upper_message)