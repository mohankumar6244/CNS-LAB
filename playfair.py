import itertools

def generate_key_square(keyword):
    keyword = "".join(dict.fromkeys(keyword.upper().replace("J", "I")))  # Remove duplicates
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_square = keyword + "".join(c for c in alphabet if c not in keyword)
    
    return [list(key_square[i:i+5]) for i in range(0, 25, 5)]  # Create 5x5 matrix

def find_position(square, letter):
    for r, row in enumerate(square):
        for c, col in enumerate(row):
            if col == letter:
                return r, c
    return None

def process_digraphs(text):
    text = text.upper().replace("J", "I")
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"

        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(a + b)
            i += 2

    return pairs

def playfair_encrypt(text, key_square):
    text_pairs = process_digraphs(text)
    encrypted_text = ""

    for a, b in text_pairs:
        r1, c1 = find_position(key_square, a)
        r2, c2 = find_position(key_square, b)

        if r1 == r2:  # Same row
            encrypted_text += key_square[r1][(c1 + 1) % 5] + key_square[r2][(c2 + 1) % 5]
        elif c1 == c2:  # Same column
            encrypted_text += key_square[(r1 + 1) % 5][c1] + key_square[(r2 + 1) % 5][c2]
        else:  # Rectangle swap
            encrypted_text += key_square[r1][c2] + key_square[r2][c1]

    return encrypted_text

def playfair_decrypt(text, key_square):
    text_pairs = process_digraphs(text)
    decrypted_text = ""

    for a, b in text_pairs:
        r1, c1 = find_position(key_square, a)
        r2, c2 = find_position(key_square, b)

        if r1 == r2:  # Same row
            decrypted_text += key_square[r1][(c1 - 1) % 5] + key_square[r2][(c2 - 1) % 5]
        elif c1 == c2:  # Same column
            decrypted_text += key_square[(r1 - 1) % 5][c1] + key_square[(r2 - 1) % 5][c2]
        else:  # Rectangle swap
            decrypted_text += key_square[r1][c2] + key_square[r2][c1]

    return decrypted_text

if __name__ == "__main__":
    keyword = input("Enter the keyword: ")
    text = input("Enter the plaintext: ")

    key_square = generate_key_square(keyword)
    
    encrypted = playfair_encrypt(text, key_square)
    decrypted = playfair_decrypt(encrypted, key_square)

    print("Key Square:")
    for row in key_square:
        print(" ".join(row))

    print("\nEncrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
