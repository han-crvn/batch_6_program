# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Check if the word or sentence starts with "dis" and print the result.
if message[:3] == "dis":
    print("It starts with 'dis'. ")
else: 
    print("It does not starts with 'dis'.")