#Read an int number. Check if the number is a palindrome. (# read backwards has the same value. Example of palindrome numbers: 123454321, 999, 1598951)

def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    # Compare the original string with its reverse
    return num_str == num_str[::-1]

# Read an integer from the user
user_input = input("Enter an integer: ")

try:
    # Convert the user input to an integer
    user_number = int(user_input)
# Check if the number is a palindrome
    if is_palindrome(user_number):
        print(f"{user_number} is a palindrome!")
    else:
        print(f"{user_number} is not a palindrome.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

punctuation = ",.?!'/* "
start = 0
while True:
    string = str(input("Type something"))
    for p in punctuation:
        string = string.replace(p,"")
    if string == string[::-1]:
        print("palindrome")
        break
    else:
        print("not palindrome")
        continue
