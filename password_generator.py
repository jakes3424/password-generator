import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    character_pool = ""

    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return None

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def get_user_preferences():
    try:
        length = int(input("Enter desired password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        return length, use_upper, use_lower, use_digits, use_symbols
    except ValueError:
        print("Invalid input. Please enter a number for length.")
        return None

def save_password_to_file(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

def main():
    print("🔐 Password Generator 🔐")

    preferences = get_user_preferences()
    if not preferences:
        return

    length, use_upper, use_lower, use_digits, use_symbols = preferences
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    if password:
        print(f"\nGenerated Password: {password}")
        save = input("Do you want to save this password to a file? (y/n): ").lower()
        if save == 'y':
            save_password_to_file(password)
            print("Password saved to 'passwords.txt'.")
    else:
        print("No character types selected. Cannot generate password.")

if __name__ == "__main__":
    main()
