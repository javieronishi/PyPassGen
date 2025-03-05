import random
import string

# Colors in ANSI
RED = "\033[31m"
CYAN = "\033[36m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

# Display the header
print("{:->30}".format(""))
print("|{:^30}|".format("Python"))
print("|{:^30}|".format("Password Generator"))
print("{:->30}".format(""))


class PasswordGenerator:
    def __init__(self, password_length):
        self.password_length = password_length

    def generate_password(self):
        # Define the allowed characters
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate the password
        password = "".join(
            random.choice(characters) for _ in range(self.password_length)
        )
        return password


# Ask the user for the password length
try:
    length = int(input(f"{CYAN}Enter the desired password length: {RESET}"))
    if length < 1:
        print(f"{RED}Error: Password length must be at least 1.{RESET}")
    else:
        password = PasswordGenerator(length)
        print(
            f"{BLUE}Generated password: {RESET} {GREEN}{password.generate_password()}{RESET}"
        )
except ValueError:
    print(f"{RED}Error: Please enter a valid number.{RESET}")
