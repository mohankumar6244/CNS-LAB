import string
from math import gcd

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    
    alphabet = string.ascii_uppercase
    encrypted_text = ''
    
    for char in text.upper():
        if char in alphabet:
            x = alphabet.index(char)
            encrypted_text += alphabet[(a * x + b) % 26]
        else:
            encrypted_text += char
    
    return encrypted_text

def affine_decrypt(ciphertext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    
    alphabet = string.ascii_uppercase
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Modular inverse of 'a' does not exist.")
    
    decrypted_text = ''
    
    for char in ciphertext.upper():
        if char in alphabet:
            y = alphabet.index(char)
            decrypted_text += alphabet[(a_inv * (y - b)) % 26]
        else:
            decrypted_text += char
    
    return decrypted_text

if __name__ == "__main__":
    choice = input("Do you want to encrypt or decrypt? (E/D): ").strip().upper()
    text = input("Enter the text or equation: ")
    a = int(input("Enter the key 'a' (must be coprime with 26): "))
    b = int(input("Enter the key 'b': "))
    
    if gcd(a, 26) != 1:
        print("Error: Key 'a' must be coprime with 26.")
    else:
        if choice == 'E':
            encrypted = affine_encrypt(text, a, b)
            print("Encrypted text:", encrypted)
        elif choice == 'D':
            decrypted = affine_decrypt(text, a, b)
            print("Decrypted text:", decrypted)
        else:
            print("Invalid choice! Please enter 'E' or 'D'.")
