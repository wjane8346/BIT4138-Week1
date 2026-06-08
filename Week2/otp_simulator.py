#!/usr/bin/env python3
"""
One-Time Pad (OTP) Simulator
For BIT4138 Week 2 - Stream Ciphers and PRNGs
"""

import secrets
import string
import os

class OneTimePad:
    def __init__(self):
        """Initialize One-Time Pad system"""
        self.message = ""
        self.key = ""
        self.ciphertext = ""
        
    def generate_true_random_key(self, length):
        """
        Generate cryptographically secure random key
        Using secrets module (system random source)
        """
        # Generate random bytes and convert to printable characters
        random_bytes = secrets.token_bytes(length)
        # Convert to uppercase letters for readability
        key = ''.join([chr(65 + (b % 26)) for b in random_bytes])
        return key
    
    def generate_random_key_ascii(self, length):
        """
        Generate true random key in full ASCII range
        """
        return secrets.token_hex(length)  # Returns hex string
    
    def encrypt(self, plaintext, key):
        """Encrypt plaintext using XOR with key"""
        if len(plaintext) != len(key):
            raise ValueError("Plaintext and key must be the same length!")
        
        ciphertext_bytes = []
        for i in range(len(plaintext)):
            plain_char = plaintext[i]
            key_char = key[i]
            encrypted_byte = ord(plain_char) ^ ord(key_char)
            ciphertext_bytes.append(encrypted_byte)
        
        # Return as hex for readability
        return ''.join([f"{b:02x}" for b in ciphertext_bytes])
    
    def decrypt(self, ciphertext_hex, key):
        """Decrypt ciphertext using XOR with same key"""
        # Convert hex string back to bytes
        ciphertext_bytes = bytes.fromhex(ciphertext_hex)
        
        if len(ciphertext_bytes) != len(key):
            raise ValueError("Ciphertext and key must be the same length!")
        
        plaintext_chars = []
        for i in range(len(ciphertext_bytes)):
            encrypted_byte = ciphertext_bytes[i]
            key_char = key[i]
            decrypted_byte = encrypted_byte ^ ord(key_char)
            plaintext_chars.append(chr(decrypted_byte))
        
        return ''.join(plaintext_chars)
    
    def demonstrate_perfect_secrecy(self, message):
        """Demonstrate that any plaintext is possible from same ciphertext"""
        print("\n" + "=" * 60)
        print("PERFECT SECRECY DEMONSTRATION")
        print("=" * 60)
        
        print(f"Original message: '{message}'")
        print(f"Message length: {len(message)} characters")
        
        # Generate a true random key
        key = self.generate_true_random_key(len(message))
        print(f"\nRandom key (same length): {key}")
        
        # Encrypt
        ciphertext = self.encrypt(message, key)
        print(f"Ciphertext (hex): {ciphertext}")
        
        # Show that different keys produce different plaintexts
        print("\n--- Attack Scenario: Attacker tries all possible keys ---")
        print("For demonstration, we try 3 different keys (in real OTP, all are possible)")
        
        fake_keys = [
            self.generate_true_random_key(len(message)),
            self.generate_true_random_key(len(message)),
            self.generate_true_random_key(len(message))
        ]
        
        for idx, fake_key in enumerate(fake_keys, 1):
            fake_plaintext = self.decrypt(ciphertext, fake_key)
            print(f"  Fake key {idx}: {fake_key} → '{fake_plaintext}'")
        
        print("\n★ KEY INSIGHT: Without the real key, the attacker cannot determine")
        print("  which plaintext is correct. All plaintexts are equally possible!")


def demonstrate_otp_requirements():
    """Demonstrate the three OTP requirements"""
    print("\n" + "=" * 60)
    print("ONE-TIME PAD REQUIREMENTS")
    print("=" * 60)
    
    otp = OneTimePad()
    message = "HELLOOTP"
    
    print("\nRequirement 1: Key length = Message length")
    print(f"  Message length: {len(message)}")
    key = otp.generate_true_random_key(len(message))
    print(f"  Key length: {len(key)}")
    print(f"  ✓ Equal length: {len(message) == len(key)}")
    
    print("\nRequirement 2: Key must be truly random")
    print(f"  Key generated: {key}")
    print(f"  Source: secrets.token_bytes() uses OS random source")
    print(f"  ✓ Cryptographically secure: Yes")
    
    print("\nRequirement 3: Key used only once")
    print("  After using this key, it MUST be discarded")
    print("  Never reuse OTP keys - this breaks perfect secrecy")


def demonstrate_key_reuse_attack():
    """Demonstrate why key reuse is dangerous"""
    print("\n" + "=" * 60)
    print("DANGERS OF KEY REUSE - CRYPTOGRAPHIC DISASTER")
    print("=" * 60)
    
    otp = OneTimePad()
    
    # Same key for two messages (BAD PRACTICE)
    key = "ABCDEFGHIJ"  # Fixed key for demonstration
    
    message1 = "HELLO THERE"
    message2 = "SECRET DATA"
    
    # Pad messages to same length
    message1 = message1.ljust(len(message2), ' ')
    message2 = message2.ljust(len(message1), ' ')
    
    print(f"\nSame key: '{key}'")
    print(f"Message 1: '{message1.strip()}'")
    print(f"Message 2: '{message2.strip()}'")
    
    cipher1 = otp.encrypt(message1, key)
    cipher2 = otp.encrypt(message2, key)
    
    print(f"\nCiphertext 1: {cipher1}")
    print(f"Ciphertext 2: {cipher2}")
    
    # XOR the two ciphertexts
    bytes1 = bytes.fromhex(cipher1)
    bytes2 = bytes.fromhex(cipher2)
    
    xor_ciphers = []
    for b1, b2 in zip(bytes1, bytes2):
        xor_ciphers.append(b1 ^ b2)
    
    print(f"\nXOR of both ciphertexts: {bytes(xor_ciphers).hex()}")
    print("\n★ WARNING: XOR of two ciphertexts = XOR of two plaintexts")
    print("  An attacker can recover both messages using language patterns!")
    print("  This is why OTP keys must NEVER be reused.")


def main():
    print("=" * 60)
    print("ONE-TIME PAD (OTP) SIMULATOR")
    print("Theoretically Unbreakable Encryption")
    print("=" * 60)
    
    otp = OneTimePad()
    
    # Get user input
    print("\nEnter a message to encrypt (or press Enter for default):")
    user_message = input("Message: ").strip()
    
    if not user_message:
        user_message = "CONFIDENTIAL MESSAGE"
        print(f"Using default message: '{user_message}'")
    
    # Generate true random key
    print(f"\nGenerating true random key of length {len(user_message)}...")
    key = otp.generate_true_random_key(len(user_message))
    print(f"Key (KEEP SECRET): {key}")
    
    # Encrypt
    print("\n--- ENCRYPTION ---")
    ciphertext = otp.encrypt(user_message, key)
    print(f"Ciphertext (hex): {ciphertext}")
    
    # Decrypt
    print("\n--- DECRYPTION ---")
    decrypted = otp.decrypt(ciphertext, key)
    print(f"Decrypted message: {decrypted}")
    print(f"✓ Success: {user_message == decrypted}")
    
    # Demonstrations
    otp.demonstrate_perfect_secrecy(user_message)
    demonstrate_otp_requirements()
    demonstrate_key_reuse_attack()
    
    print("\n" + "=" * 60)
    print("CONCLUSION:")
    print("• OTP provides mathematically perfect secrecy")
    print("• Requires true random keys equal to message length")
    print("• Keys must be used exactly once")
    print("• Key distribution is the main practical challenge")
    print("• Used only for extremely high-security applications")
    print("=" * 60)


if __name__ == "__main__":
    main()