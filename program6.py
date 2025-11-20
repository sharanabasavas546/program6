import sys

# Check if the correct number of arguments is provided
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    string = sys.argv[1]
else:
    script_name = sys.argv[0]
    string = "madan"
    print("Invalid input. Using default value.")

# Check if the string is a palindrome
if string == string[::-1]:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
