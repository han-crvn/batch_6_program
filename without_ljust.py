# Add storage for lines of messages
line_of_message = []

# Allow user to input the word or sentence.
while True:
    message = input("Enter the word or sentence (enter a digit to stop): ")
    
    # Inputting number will break if a number is inputted.
    if message.isdigit():
        break

    else:

        # Format the input to left justify.
        line_of_message.append(message + " " * ( 50 - len(message)))

# Print the result.
for message in line_of_message:
    print(message)