def generate_key(text, key):
    # Repeat the key to match the length of the text
    key = list(key)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(plaintext, key):
    # Generate the full key
    key = generate_key(plaintext, key)
    
    encrypted_text = []
    for i in range(len(plaintext)):
        # Get the corresponding shift for each letter
        shift = ord(key[i].lower()) - ord('a')
        # Encrypt the letter using the shift value
        if plaintext[i].isalpha():
            char = plaintext[i].lower()
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            # If the letter was uppercase, keep it uppercase
            if plaintext[i].isupper():
                encrypted_text.append(encrypted_char.upper())
            else:
                encrypted_text.append(encrypted_char)
        else:
            # If it's not a letter, keep it unchanged
            encrypted_text.append(plaintext[i])
    
    return ''.join(encrypted_text)

def decrypt(ciphertext, key):
    # Generate the full key
    key = generate_key(ciphertext, key)
    
    decrypted_text = []
    for i in range(len(ciphertext)):
        # Get the corresponding shift for each letter
        shift = ord(key[i].lower()) - ord('a')
        # Decrypt the letter using the shift value
        if ciphertext[i].isalpha():
            char = ciphertext[i].lower()
            decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            # If the letter was uppercase, keep it uppercase
            if ciphertext[i].isupper():
                decrypted_text.append(decrypted_char.upper())
            else:
                decrypted_text.append(decrypted_char)
        else:
            # If it's not a letter, keep it unchanged
            decrypted_text.append(ciphertext[i])
    
    return ''.join(decrypted_text)

# Main program
def main():
    # User inputs the key and text
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")
    
    encrypted_text = encrypt(plaintext, key)
    print("Encrypted Text:", encrypted_text)
    
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
