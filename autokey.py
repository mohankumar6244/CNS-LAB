def generate_key(plaintext, key):
    # Make the key long enough by appending the plaintext to the key
    key = key + plaintext
    return key

def encrypt(plaintext, key):
    key = generate_key(plaintext, key)
    encrypted_text = ""
    
    # Encrypt each letter of the plaintext
    for i in range(len(plaintext)):
        pt_char = plaintext[i]
        key_char = key[i]
        
        # Ensure the letters are in uppercase
        pt_pos = ord(pt_char) - ord('A')
        key_pos = ord(key_char) - ord('A')
        
        # Perform encryption and apply modulo 26 to handle wrapping
        encrypted_char = chr((pt_pos + key_pos) % 26 + ord('A'))
        encrypted_text += encrypted_char
    
    return encrypted_text

def decrypt(ciphertext, key):
    key = generate_key(ciphertext, key)
    decrypted_text = ""
    
    # Decrypt each letter of the ciphertext
    for i in range(len(ciphertext)):
        ct_char = ciphertext[i]
        key_char = key[i]
        
        # Ensure the letters are in uppercase
        ct_pos = ord(ct_char) - ord('A')
        key_pos = ord(key_char) - ord('A')
        
        # Perform decryption and apply modulo 26 to handle wrapping
        decrypted_char = chr((ct_pos - key_pos + 26) % 26 + ord('A'))
        decrypted_text += decrypted_char
    
    return decrypted_text

# User input for plaintext and key
plaintext = input("Enter the plaintext: ").upper()
key = input("Enter the key: ").upper()

# Ensure both plaintext and key consist of only alphabetic characters
plaintext = ''.join(filter(str.isalpha, plaintext))
key = ''.join(filter(str.isalpha, key))

# Generate the new key by appending plaintext to the key
new_key = generate_key(plaintext, key)

# Encrypt the text
encrypted_text = encrypt(plaintext, key)

# Decrypt the text back to original plaintext
decrypted_text = decrypt(encrypted_text, key)

# Output the results
print(f"Plaintext: {plaintext}")
print(f"Original Key: {key}")
print(f"Generated Key: {new_key}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
