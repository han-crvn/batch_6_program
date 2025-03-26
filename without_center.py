# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Add total width of line and adjust left and right padding
width = 176

left_pad = (width - len(message)) // 2
right_pad = width - len(message) - left_pad

# Add the padding
center_message = " " * left_pad + message + " " * right_pad

# Print the result
print(center_message)