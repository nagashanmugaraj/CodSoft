import random
import string

def generate_password(length):
    # Combine uppercase, lowercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user to specify the desired password length
try:
    length = int(input("Enter the desired password length: "))
    if length < 1:
        print("Password length must be at least 1.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print(f"Your generated password is: {password}")
except ValueError:
    print("Please enter a valid number.")