# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Check if all letters is lowercase.
for char in message:
    if "a" <= char <= "z":
        result = "All lowercase."
    else:
        result = "There is a uppercase letter/s."
        break

# Print result.
print(result)