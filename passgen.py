import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        length = int(input("Enter the length of the password you want to generate (0 to exit): "))
        if length == 0:
            print("Exiting the program...")
            break
        elif length < 0:
            print("Please enter a valid length greater than or equal to 0.")
            continue
        password = generate_password(length)
        print("Your generated password is:", password)

if __name__ == "__main__":
    main()
