# Allow user to input a number.
numbers = input("Enter a number from range 1-999999: ")

# Format the input.
if 1 <= int(numbers) <= 999999:
    zero_fill = 6 - len(numbers)
    formatted_number = "0" * zero_fill + numbers

    # Print result.
    print(formatted_number)

else:
    print("Number must be from range 1-999999.")
    