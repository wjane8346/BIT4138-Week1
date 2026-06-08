#!/usr/bin/env python3
"""
BIT4138 - Advanced Cryptography
Week 2: XOR Stream Cipher - Full Sentence Encryption

This program encrypts user input (including spaces and special characters)
using XOR stream cipher and displays the ciphertext in hexadecimal format.
"""

# ============================================================
# SIMPLE VERSION (What you requested)
# ============================================================

print("=" * 60)
print("XOR STREAM CIPHER - TEXT ENCRYPTION")
print("=" * 60)

# Get input from user
text = input("\nEnter text to encrypt: ")
key = input("Enter key: ")

# Encrypt using XOR
# For each character in text, XOR with corresponding key character
# Key repeats if shorter than text using i % len(key)
ciphertext = ''.join(chr(ord(t) ^ ord(key[i % len(key)])) for i, t in enumerate(text))

# Display results
print("\n" + "=" * 60)
print("ENCRYPTION RESULTS")
print("=" * 60)
print(f"Original text: {text}")
print(f"Key: {key}")
print(f"Key length: {len(key)} characters")
print(f"Text length: {len(text)} characters")
print(f"Ciphertext (hex): {ciphertext.encode().hex()}")
print("=" * 60)


# ============================================================
# ENHANCED VERSION WITH BOTH ENCRYPT AND DECRYPT
# ============================================================

def xor_encrypt_decrypt(text, key):
    """
    XOR encryption and decryption (same function works for both)
    Preserves all characters including spaces and special symbols
    """
    result = ''.join(chr(ord(t) ^ ord(key[i % len(key)])) for i, t in enumerate(text))
    return result

def main():
    print("\n" + "=" * 60)
    print("XOR STREAM CIPHER - ENCRYPTION & DECRYPTION")
    print("=" * 60)
    
    while True:
        print("\n--- MENU ---")
        print("1. Encrypt a message")
        print("2. Decrypt a message (provide hex ciphertext)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ")
        
        if choice == '1':
            # ENCRYPTION MODE
            plaintext = input("\nEnter text to encrypt: ")
            key = input("Enter encryption key: ")
            
            if len(key) == 0:
                print("Error: Key cannot be empty!")
                continue
            
            ciphertext = xor_encrypt_decrypt(plaintext, key)
            hex_output = ciphertext.encode().hex()
            
            print("\n--- ENCRYPTION RESULT ---")
            print(f"Original: {plaintext}")
            print(f"Key: {key}")
            print(f"Ciphertext (hex): {hex_output}")
            print(f"\nTo decrypt later, use this hex value with the same key: {hex_output}")
            
        elif choice == '2':
            # DECRYPTION MODE
            hex_input = input("\nEnter ciphertext (hex): ")
            key = input("Enter decryption key: ")
            
            if len(key) == 0:
                print("Error: Key cannot be empty!")
                continue
            
            try:
                # Convert hex back to bytes then to string
                ciphertext_bytes = bytes.fromhex(hex_input)
                ciphertext = ciphertext_bytes.decode('latin1')  # Use latin1 to preserve all bytes
                
                # Decrypt
                decrypted = xor_encrypt_decrypt(ciphertext, key)
                
                print("\n--- DECRYPTION RESULT ---")
                print(f"Ciphertext (hex): {hex_input}")
                print(f"Key: {key}")
                print(f"Decrypted text: {decrypted}")
                
            except ValueError:
                print("Error: Invalid hex input! Please enter valid hexadecimal.")
                
        elif choice == '3':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


# ============================================================
# RUN THE ENHANCED VERSION
# ============================================================

if __name__ == "__main__":
    # First show the simple version
    print("\n" + "=" * 60)
    print("SIMPLE ENCRYPTION DEMONSTRATION")
    print("=" * 60)
    
    # Simple test
    test_text = "Hello World 123"
    test_key = "secret"
    test_cipher = ''.join(chr(ord(t) ^ ord(test_key[i % len(test_key)])) for i, t in enumerate(test_text))
    print(f"\nTest Example:")
    print(f"  Plaintext: {test_text}")
    print(f"  Key: {test_key}")
    print(f"  Ciphertext (hex): {test_cipher.encode().hex()}")
    
    # Then run the interactive menu
    main()