import random
import string

def get_user_options():
 
    while True:
        try:
            length = int(input("Enter the desired password length (greater than 4): "))
            if length < 5:
                print("Password length should be at least 5 for security reasons.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nSelect the types of characters to include in the password:")
    include_lowercase = input("Include lowercase letters (a-z)? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase letters (A-Z)? (y/n): ").lower() == 'y'
    include_digits = input("Include digits (0-9)? (y/n): ").lower() == 'y'
    include_specials = input("Include special characters (!@#$%^&*)? (y/n): ").lower() == 'y'

    while not (include_lowercase or include_uppercase or include_digits or include_specials):
        print("\nYou must select at least one type of character.")
        include_lowercase = input("Include lowercase letters (a-z)? (y/n): ").lower() == 'y'
        include_uppercase = input("Include uppercase letters (A-Z)? (y/n): ").lower() == 'y'
        include_digits = input("Include digits (0-9)? (y/n): ").lower() == 'y'
        include_specials = input("Include special characters (!@#$%^&*)? (y/n): ").lower() == 'y'

    return length, include_lowercase, include_uppercase, include_digits, include_specials


def generate_password(length, include_lowercase, include_uppercase, include_digits, include_specials):
    
    pool = ''
    if include_lowercase:
        pool += string.ascii_lowercase
    if include_uppercase:
        pool += string.ascii_uppercase
    if include_digits:
        pool += string.digits
    if include_specials:
        pool += string.punctuation


    if not pool:
        raise ValueError("No character types selected. Cannot generate password.")

    password = ''.join(random.choice(pool) for _ in range(length))

    if include_lowercase and not any(c in string.ascii_lowercase for c in password):
        password = password[:length-1] + random.choice(string.ascii_lowercase)
    if include_uppercase and not any(c in string.ascii_uppercase for c in password):
        password = password[:length-1] + random.choice(string.ascii_uppercase)
    if include_digits and not any(c in string.digits for c in password):
        password = password[:length-1] + random.choice(string.digits)
    if include_specials and not any(c in string.punctuation for c in password):
        password = password[:length-1] + random.choice(string.punctuation)

    
    password = ''.join(random.sample(password, len(password)))
    return password


def main():
    
    print("Welcome to the Custom Password Generator!\n")
    
   
    length, include_lowercase, include_uppercase, include_digits, include_specials = get_user_options()

    try:
        password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_specials)
       
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
