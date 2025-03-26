# Allow user to input the word or sentence.
message = input("Enter the word or sentence: ")

# Check if the word or sentence ends with "er" and print the result.
if message[-2:] == "er":
    print("It ends with 'er'. ")
else: 
    print("It does not ends with 'er'.")