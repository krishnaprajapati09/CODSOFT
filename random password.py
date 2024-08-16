import random
import string

def generate_password(length):
    # Define possible characters: uppercase, lowercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired password length: "))
        
        # Ensure the length is a positive integer
        if length <= 0:
            print("Please enter a positive integer for the length.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
