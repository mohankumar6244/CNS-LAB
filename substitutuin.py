import string
import random

def generate_key():
    letters = list(string.ascii_lowercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled)), dict(zip(shuffled, letters))

def encrypt(text, key):
    text = text.lower()
    encrypted_text = ''.join(key.get(char, char) for char in text)
    return encrypted_text

def decrypt(text, reverse_key):
    decrypted_text = ''.join(reverse_key.get(char, char) for char in text)
    return decrypted_text

if __name__ == "__main__":
    key, reverse_key = generate_key()
    
    print("Generated Key:", key)
    
    user_input = input("Enter text: ")
    encrypted_text = encrypt(user_input, key)
    decrypted_text = decrypt(encrypted_text, reverse_key)
    
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)
