# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Remove the spaces from the right side.
for i in range(len(message) - 1, -1, -1):
    if message[i] != " ":
        message = message[:i + 1]
        break

# Print the result.
print(message)
