def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted = ord(char) + shift_amount
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                shifted = ord(char) + shift_amount
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

while True:
    print("\nCaesar Cipher Menu:")
    print("1. Encrypt the entered message")
    print("2. Decrypt an encrypted message")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == '1':
        message = input("Enter the message to encrypt: ").strip()
        try:
            shift = int(input("Enter the shift value: ").strip())
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        except ValueError:
            print("Shift value must be an integer.")

    elif choice == '2':
        message = input("Enter the message to decrypt: ").strip()
        try:
            shift = int(input("Enter the shift value: ").strip())
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        except ValueError:
            print("Shift value must be an integer.")

    elif choice == '3':
        print("Thank you!")
        break

    else:
        print("Invalid option! Please choose 1, 2, or 3.")

