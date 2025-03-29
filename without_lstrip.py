# Allow user to input the words or sentences with left padded spaces.
message = input("Enter the word or sentence: ")

# Remove the spaces from left.
for i in range(len(message)):
    if message[i] != " ":
        message = message[i:]
        break

# Print the result.
print(message)
