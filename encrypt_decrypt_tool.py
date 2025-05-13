from cryptography.fernet import Fernet
import os

# Function to generate a key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[✔] Key generated and saved to 'secret.key'")

# Function to load the saved key
def load_key():
    if not os.path.exists("secret.key"):
        print("[!] Key file not found. Please generate a key first.")
        return None
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Function to encrypt a message
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    print("\n[🔐] Encrypted message:")
    print(encrypted.decode())

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    try:
        f = Fernet(key)
        decrypted = f.decrypt(encrypted_message.encode())
        print("\n[🔓] Decrypted message:")
        print(decrypted.decode())
    except Exception as e:
        print("[!] Error decrypting. Check your message and key.")
        print("Details:", e)

# CLI menu
def main():
    print("\nSimple Encryption & Decryption Tool (Python CLI)")
    print("---------------------------------------------------")

    while True:
        print("""
[1] Generate Key
[2] Load Existing Key
[3] Encrypt a Message
[4] Decrypt a Message
[5] Exit
        """)
        choice = input("Select an option: ").strip()

        if choice == '1':
            generate_key()
        elif choice == '2':
            key = load_key()
            if key:
                print("[✔] Key loaded successfully.")
        elif choice == '3':
            key = load_key()
            if key:
                msg = input("Enter the message to encrypt: ")
                encrypt_message(msg, key)
        elif choice == '4':
            key = load_key()
            if key:
                enc_msg = input("Enter the encrypted message: ")
                decrypt_message(enc_msg, key)
        elif choice == '5':
            print("Exiting... Goodbye 👋")
            break
        else:
            print("[!] Invalid option. Try again.")

if __name__ == "__main__":
    main()
