plaintext = "HELLO"
key = "X"
ciphertext = ''.join(chr(ord(p) ^ ord(key[i % len(key)])) for i,p in enumerate(plaintext))
decrypted = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i,c in enumerate(ciphertext))
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Ciphertext: {repr(ciphertext)}")
print(f"Decrypted: {decrypted}")