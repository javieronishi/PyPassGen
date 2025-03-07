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
    def __init__(
        self, password_length, include_numbers=True, include_special_chars=True
    ):
        self.password_length = password_length
        self.include_numbers = include_numbers
        self.include_special_chars = include_special_chars

    def generate_password(self):
        # Define the allowed characters
        characters = string.ascii_letters
        if self.include_numbers:
            characters += string.digits
        if self.include_special_chars:
            characters += string.punctuation

        # Generate the password
        password = "".join(
            random.choice(characters) for _ in range(self.password_length)
        )
        return password


# Ask the user for the password length
try:
    length = int(input(f"{CYAN}Enter the desired password length (max 64): {RESET}"))
    if length < 1:
        print(f"{RED}Error: Password length must be at least 1.{RESET}")
    elif length > 64:
        print(f"{RED}Error: Password length cannot exceed 64.{RESET}")
    else:
        include_numbers = input(f"{CYAN}Include numbers? (y/n): {RESET}").lower() == "y"
        include_special_chars = (
            input(f"{CYAN}Include special characters? (y/n): {RESET}").lower() == "y"
        )

        password_generator = PasswordGenerator(
            length, include_numbers, include_special_chars
        )
        print(
            f"{BLUE}Generated password: {RESET} {GREEN}{password_generator.generate_password()}{RESET}"
        )
except ValueError:
    print(f"{RED}Error: Please enter a valid number.{RESET}")
