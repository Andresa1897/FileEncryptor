import random
from cryptography.fernet import Fernet

ascii_art_list = [
    """
    ███████╗██╗███████╗██████╗ ███████╗███╗   ██╗
    ██╔════╝██║██╔════╝██╔══██╗██╔════╝████╗  ██║
    █████╗  ██║█████╗  ██████╔╝█████╗  ██╔██╗ ██║
    ██╔══╝  ██║██╔══╝  ██╔══██╗██╔══╝  ██║╚██╗██║
    ██║     ██║███████╗██████╔╝███████╗██║ ╚████║
    ╚═╝     ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═══╝
    """,
    """
     _  _ ____ _ _ ____ _  _ _ _  _ ____ _ _ ____ _  _ ____ 
     |\/| |__| | |\ |__| |\ | | |\ | | __ | |\ | |__| |  | 
     |  | |  | | | \|  | | \| | | \| |__] | | \| |  | |__| 
    """
]


# Function to print a random ASCII art from the list
def print_random_ascii_art():
    random_art = random.choice(ascii_art_list)
    print(random_art)


# Function to generate a new symmetric key
def generate_key():
    return Fernet.generate_key()


# Function to write the key to a file
def write_key_to_file(key, filename="key.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)


# Function to load the key from a file
def load_key(filename="key.key"):
    return open(filename, "rb").read()


# Function to encrypt a file
def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filename + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)


# Function to decrypt a file
def decrypt_file(encrypted_filename, key):
    fernet = Fernet(key)
    with open(encrypted_filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(encrypted_filename.replace(".enc", ""), "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)


# Main function
def main():
    print_random_ascii_art()
    choice = input("Choose an option:\n1. Encrypt a file\n2. Decrypt a file\n")

    if choice == "1":
        key = generate_key()
        write_key_to_file(key)
        filename = input("Enter the path of the file to encrypt: ")
        encrypt_file(filename, key)
        print(f"File encrypted and saved as {filename}.enc")
    elif choice == "2":
        key = load_key()
        encrypted_filename = input("Enter the path of the encrypted file: ")
        decrypt_file(encrypted_filename, key)
        print(f"File decrypted and saved as {encrypted_filename.replace('.enc', '')}")
    else:
        print("Invalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
