import random


def generate_password(length, use_lower, use_upper, use_numbers, use_symbols):
    lower_case = "abcdefghijklmnopqrstuvwxyz" if use_lower else ""
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if use_upper else ""
    numbers = "0123456789" if use_numbers else ""
    symbols = "@#$%^&*/\?" if use_symbols else ""

    all_characters = lower_case + upper_case + numbers + symbols

    if len(all_characters) == 0:
        print("You need to select at least one type of character to generate a password!")
        return None

    return "".join(random.sample(all_characters, length))


if __name__ == "__main__":
    print("Welcome to the Dynamic Password Generator! 🎉")

    # Get user preferences
    try:
        length = int(input("Enter the length for your password (e.g. 12): "))
        if length < 1:
            print("Password length should be at least 1.")
            exit()
    except ValueError:
        print("Invalid input! Please enter a number.")
        exit()

    use_lower = input("Include lower-case characters? (y/n): ").strip().lower() == 'y'
    use_upper = input("Include upper-case characters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    purpose = input("What will you use this password for? ")

    password = generate_password(length, use_lower, use_upper, use_numbers, use_symbols)

    if password:
        print(f"Your super-secure password is: {password} 🌟")

        # Save to txt file
        with open("passwords.txt", "a") as f:
            f.write(f"Purpose: {purpose}\n")
            f.write(f"Password: {password}\n")
            f.write("=" * 30 + "\n")

        print("Your password has been saved to 'passwords.txt'. 📝")
