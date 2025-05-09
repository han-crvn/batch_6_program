# Allow users to input the word or sentence.
message = input("Enter the word or sentence: ")

# Allow users to choose what character to find.
locate_char = input("Enter a character to find: ")

# Find the first index of chosen character starting from right.
position = -1

for i in range(len(message) - 1, -1, -1):
    if message[i] == locate_char :
        position = i
        break

# Print result.
if position != -1:
    print(f"{locate_char}: at index ({position})")
else:
    print("Not found.")