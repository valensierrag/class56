# I want to print a multiplication table from 1 to 10
for i in range(1,11):
    for j in range(i, 11):
        print(i, "x", j, "=", i*j)
    print()

num = 0
count = 0
while num <= 19:
    if num % 3 == 0:
        count += 1
    num += 1

print("Numbers divisible by 3", count)

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
