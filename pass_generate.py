import random  # Import the random library for generating random characters
import time  # Import the time library for sleep function

# Function to simulate typing like a human for fun effect
def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Print newline at the end

# Function to generate a password based on the user's requirements
def generate_password(length, use_lower, use_upper, use_numbers):
    # Adding a dramatic pause for effect
    slow_print("Generating your super-secure password...", 0.05)

    # Define available characters based on the user's choice
    lower_case = "abcdefghijklmnopqrstuvwxyz" if use_lower else ""
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if use_upper else ""
    numbers = "0123456789" if use_numbers else ""

    # Combine all selected characters into a single string
    all_characters = lower_case + upper_case + numbers

    # Check if at least one type of character is selected
    if len(all_characters) == 0:
        slow_print("Oops! You need to select at least one type of character.")
        return None

    # Generate and return the password
    return "".join(random.sample(all_characters, length))

# Main code starts here
if __name__ == "__main__":
    slow_print("Welcome to the most fun Dynamic Password Generator ever!")

    # Get the username
    username = input("First, what's your username? ")

    # Get password length from the user
    while True:
        try:
            length = int(input("How long should your password be? (e.g. 12): "))
            if length < 1:
                slow_print("A password should have at least 1 character, come on!")
            else:
                break
        except ValueError:
            slow_print("That's not a number! Try again.")

    # Get user's character preferences
    use_lower = input("Want some lower-case characters? (y/n): ").strip().lower() == 'y'
    use_upper = input("How about upper-case characters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("You like numbers, don't you? (y/n): ").strip().lower() == 'y'

    # Ask the user what the password is for
    purpose = input("What's this password for? ")

    # Generate the password
    password = generate_password(length, use_lower, use_upper, use_numbers)

    if password:
        slow_print("Your super-secure, absolutely amazing password is: " + password)

        # Save the password to a text file
        with open("passwords.txt", "a") as f:
            f.write(f"Username: {username}\n")
            f.write(f"Details: {purpose}\n")
            f.write(f"Password: {password}\n")
            f.write("=" * 30 + "\n")

        slow_print("Your password is now saved in a 'passwords.txt' file.")
