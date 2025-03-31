# Allow users to input the word or sentence.
message = input("Enter the word or sentence: ")

# Allow users to choose what character to count.
find_char = input("Enter a character to find: ")

# Count the numbers of chosen character.
count = 0
for char in message:
    if char == find_char:
        count += 1

# Print result.
print(f"{find_char}: {count}")