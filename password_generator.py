import random
import string

def get_user_input():
    length = int(input("Enter the length of the password: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    return length, use_letters, use_numbers, use_symbols

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Please choose at least one character set.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length, use_letters, use_numbers, use_symbols = get_user_input()

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
