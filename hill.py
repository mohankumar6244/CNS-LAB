import numpy as np
from sympy import Matrix

def mod26_inverse(matrix):
    """Find the modular inverse of a matrix modulo 26."""
    det = int(round(np.linalg.det(matrix)))
    det_mod26 = det % 26

    # Find the modular inverse of the determinant modulo 26
    det_inv = pow(det_mod26, -1, 26)

    # Compute the adjugate matrix and then multiply by the determinant's modular inverse
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % 26

    # Modular inverse of the matrix
    inverse_matrix = (det_inv * adjugate) % 26
    return inverse_matrix.astype(int)

def encrypt_hill(plaintext, key):
    """Encrypt a message using the Hill cipher."""
    # Convert plaintext to numerical values (A=0, B=1, ..., Z=25)
    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    plaintext_matrix = np.array(plaintext_vector).reshape(-1, len(key))

    # Encrypt: C = (K * P) % 26
    ciphertext_matrix = (np.dot(key, plaintext_matrix.T) % 26).T
    ciphertext_vector = ciphertext_matrix.flatten()

    # Convert numerical values back to letters
    ciphertext = ''.join(chr(num + ord('A')) for num in ciphertext_vector)
    return ciphertext

def decrypt_hill(ciphertext, key):
    """Decrypt a message using the Hill cipher."""
    # Find the modular inverse of the key matrix
    key_inverse = mod26_inverse(key)

    # Convert ciphertext to numerical values (A=0, B=1, ..., Z=25)
    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext_vector).reshape(-1, len(key))

    # Decrypt: P = (K_inv * C) % 26
    plaintext_matrix = (np.dot(key_inverse, ciphertext_matrix.T) % 26).T
    plaintext_vector = plaintext_matrix.flatten()

    # Convert numerical values back to letters
    plaintext = ''.join(chr(int(num) + ord('A')) for num in plaintext_vector)
    return plaintext

# Given key matrix
key_matrix = np.array([
    [17, 17, 5],
    [21, 18, 21],
    [2, 2, 19]
])

# Print the key matrix
print("Key Matrix:")
print(key_matrix)

# Plaintext to encrypt
plaintext = "PAY"

# Encrypt the plaintext
ciphertext = encrypt_hill(plaintext, key_matrix)
print("Encrypted text:", ciphertext)

# Decrypt the ciphertext
decrypted_text = decrypt_hill(ciphertext, key_matrix)
print("Decrypted text:", decrypted_text)
