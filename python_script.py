#!/usr/bin/env python3
import secrets
import string
from password_strength import PasswordPolicy
from pyfiglet import figlet_format
import time

# Define the password policy
policy = PasswordPolicy.from_names(
    length=8,  # min length
    uppercase=1,  # need min. 1 uppercase letter
    numbers=1,  # need min. 1 number
    special=1  # need min. 1 special character
)

# Load the RockYou wordlist
def load_rockyou_wordlist():
    with open('rockyou.txt', 'r', encoding='latin-1') as file:
        return set(line.strip() for line in file)

# Function to estimate brute-force time
def estimate_bruteforce_time(password):
    charset_size = len(string.ascii_letters + string.digits + string.punctuation)
    password_length = len(password)
    combinations = charset_size ** password_length
    guesses_per_second = 1e6  # Assuming 1 million guesses per second
    total_seconds = combinations / guesses_per_second
    return total_seconds

# Generate password based on user choice
def generate_password(password_type, length):
    charset_options = {
        1: string.ascii_lowercase,  # Lowercase only
        2: string.ascii_uppercase,  # Uppercase only
        3: string.digits,  # Numbers only
        4: string.punctuation,  # Special characters only
        5: string.ascii_lowercase + string.ascii_uppercase,  # Lowercase + Uppercase
        6: string.ascii_lowercase + string.digits,  # Lowercase + Numbers
        7: string.ascii_uppercase + string.digits,  # Uppercase + Numbers
        8: string.ascii_lowercase + string.ascii_uppercase + string.digits,  # Lowercase + Uppercase + Numbers
        9: string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation  # All types
    }

    charset = charset_options.get(password_type)
    if charset:
        return ''.join(secrets.choice(charset) for _ in range(length))
    else:
        return None

# Check the password's strength
def check_password_strength(password, rockyou_set):
    # Check against the RockYou wordlist
    if password in rockyou_set:
        return False, "Password is in the RockYou wordlist. It's too common."

    # Check password strength with policy
    issues = policy.test(password)
    if issues:
        return False, f"Password does not meet the strength policy: {issues[0]}"

    # Estimate brute-force attack time
    time_seconds = estimate_bruteforce_time(password)
    time_hours = time_seconds / 3600
    time_days = time_hours / 24

    if time_days < 1:
        return False, f"Password is weak. Estimated time to brute-force: {time_hours:.2f} hours."

    return True, f"Password is strong. Estimated time to brute-force: {time_days:.2f} days."

# Generate a password based on user input
def password_generator_menu():
    print("\nPassword Generation Options:")
    print("1. Lowercase letters only")
    print("2. Uppercase letters only")
    print("3. Numbers only")
    print("4. Special characters only")
    print("5. Lowercase + Uppercase")
    print("6. Lowercase + Numbers")
    print("7. Uppercase + Numbers")
    print("8. Lowercase + Uppercase + Numbers")
    print("9. Lowercase + Uppercase + Numbers + Special characters")

    password_type = int(input("Select the type of password you want to generate (1-9): "))
    password_length = int(input("Enter the desired length of the password: "))

    generated_password = generate_password(password_type, password_length)
    if generated_password:
        print(f"Generated Password: {generated_password}")
    else:
        print("Invalid option. Please try again.")

# Prompt the user to go back to the main menu or exit
def return_to_main_menu():
    while True:
        choice = input("\nWould you like to return to the main menu or exit? (1 for Main Menu, 2 for Exit): ")
        if choice == "1":
            return True
        elif choice == "2":
            print("Exiting... Goodbye!")
            return False
        else:
            print("Invalid choice. Please select 1 or 2.")

# Main menu for user interaction
def main_menu(rockyou_set):
    while True:
        # Display main menu with pyfiglet
        print(figlet_format("Password Manager", font="slant"))
        print("Welcome to the Password Manager!")
        print("1. Check password strength")
        print("2. Generate a strong password")
        print("3. Exit")
        choice = input("Please select an option (1, 2, 3): ")

        if choice == "1":
            # Check password strength
            password = input("Enter the password you want to check: ")
            is_strong, message = check_password_strength(password, rockyou_set)
            print(message)
            if not is_strong:
                print("Suggested stronger password:", generate_password(9, 12))  # Default to strong password
            if not return_to_main_menu():
                break

        elif choice == "2":
            # Generate a strong password
            password_generator_menu()
            if not return_to_main_menu():
                break

        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

def main():
    print("Loading RockYou wordlist, please wait...")
    start_time = time.time()
    rockyou_set = load_rockyou_wordlist()
    end_time = time.time()
    print(f"RockYou wordlist loaded in {end_time - start_time:.2f} seconds.")

    # Run the main menu
    main_menu(rockyou_set)

if __name__ == "__main__":
    main()
