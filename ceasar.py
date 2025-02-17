def caesar_cipher(text, shift):
    """
    Encrypts or decrypts a message using the Caesar Cipher.

    Args:
      texheed or decrypted.
      shift: The number of positions to shift the letters. 
             For encryption, use a positive shift.
             For decryption, use a negative shift.

    Returns:
      The encrypted or decrypted message.
    """

    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result

# Get input from the user
text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Encrypt the message
encrypted_text = caesar_cipher(text, shift)
print("Encrypted message:", encrypted_text)

# Decrypt the message
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted message:", decrypted_text)