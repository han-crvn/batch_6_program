# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Check if all letters is uppercase
for char in message:
    if "A" <= char <= "Z":
        result = "All uppercase."
    else:
        result = "There is a lowercase letter/s."
        break

# Print result
print(result)