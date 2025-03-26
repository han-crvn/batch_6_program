# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Change uppercase to lowercase and lowercase to uppercase.
reverse_message = ""

for char in message:
    if "A" <= char <= "Z":
        reverse_message += chr(ord(char) + 32)
    elif "a" <= char <= "z":
        reverse_message += chr(ord(char) - 32)
    else:
        reverse_message += char 

# Print the result.
print(reverse_message)