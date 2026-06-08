def vigenere_decrypt(ciphertext, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            start = ord('A')
            result += chr((ord(char) - start - shift) % 26 + start)
            key_index += 1
        else:
            result += char

    return result


ciphertext = "RIJVS"
key = "KEY"

plaintext = vigenere_decrypt(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted Text:", plaintext)