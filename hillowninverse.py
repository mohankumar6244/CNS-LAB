import numpy as np

def mod26_inverse(matrix):
    """Find the modular inverse of a matrix modulo 26 using adjugate method."""
    
    # Calculate the determinant modulo 26
    det = int(round(np.linalg.det(matrix)))
    det_mod26 = det % 26
    
    # Check if the determinant is invertible (det_mod26 should not be 0)
    if det_mod26 == 0:
        raise ValueError("The matrix is not invertible because its determinant modulo 26 is 0.")
    
    # Find the modular inverse of the determinant modulo 26
    det_inv = pow(det_mod26, -1, 26)

    # Find the adjugate matrix (transpose of cofactor matrix)
    adjugate = np.zeros(matrix.shape, dtype=int)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cofactor = ((-1) ** (i + j)) * int(round(np.linalg.det(minor))) % 26
            adjugate[j, i] = cofactor  # Transpose the cofactor matrix

    # Multiply the adjugate by the modular inverse of the determinant
    inverse_matrix = (det_inv * adjugate) % 26
    return inverse_matrix.astype(int)

def encrypt_hill(plaintext, key):
    """Encrypt a message using the Hill cipher."""
    # Convert plaintext to numerical values (A=0, B=1, ..., Z=25)
    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    
    # Ensure the plaintext length is a multiple of the key matrix size
    while len(plaintext_vector) % len(key) != 0:
        plaintext_vector.append(ord('X') - ord('A'))  # Padding with 'X' (value 23)
    
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

# Function to input matrix from user
def input_key_matrix():
    """Prompt the user to input a key matrix."""
    print("Enter the key matrix (e.g. 3x3 matrix):")
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    
    if rows != columns:
        raise ValueError("The matrix must be square (same number of rows and columns).")
    
    matrix = []
    
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} (space separated values): ").split()))
        matrix.append(row)
        
    return np.array(matrix)

# Function to input plaintext from user
def input_plaintext():
    """Prompt the user to input plaintext."""
    plaintext = input("Enter the plaintext: ").upper()
    return plaintext

# Main execution
if __name__ == "__main__":
    try:
        # Input key matrix from user
        key_matrix = input_key_matrix()

        # Check if the matrix is invertible (determinant modulo 26 should not be 0)
        det = int(round(np.linalg.det(key_matrix))) % 26
        if det == 0:
            print("The key matrix is not invertible because its determinant modulo 26 is 0.")
        else:
            # Input plaintext from user
            plaintext = input_plaintext()

            # Encrypt the plaintext
            ciphertext = encrypt_hill(plaintext, key_matrix)
            print("Encrypted text:", ciphertext)

            # Decrypt the ciphertext
            decrypted_text = decrypt_hill(ciphertext, key_matrix)
            print("Decrypted text:", decrypted_text)

    except ValueError as e:
        print("Error:", e)
