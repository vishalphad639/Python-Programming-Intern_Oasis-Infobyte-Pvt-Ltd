import random
import string

def get_user_input():
    """Get user input for password length and character types."""
    while True:
        try:
            length = int(input("Enter password length (at least 6): "))
            if length < 6:
                raise ValueError("Length must be at least 6.")
            break
        except ValueError as e:
            print(e)

    print("Choose character types to include:")
    include_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    return length, include_letters, include_numbers, include_symbols

def generate_password(length, include_letters, include_numbers, include_symbols):
    """Generate a random password based on user-defined criteria."""
    character_set = ''
    if include_letters:
        character_set += string.ascii_letters
    if include_numbers:
        character_set += string.digits
    if include_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    """Main function to run the password generator."""
    try:
        length, include_letters, include_numbers, include_symbols = get_user_input()
        password = generate_password(length, include_letters, include_numbers, include_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()



# running the programme by using this command in your terminal -python password_generator.py
