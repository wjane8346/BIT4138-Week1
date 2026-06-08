# Demonstration 4: Perform Feistel rounds
# BIT4138 Week 5

print("=" * 50)
print("DEMO 4: Feistel Rounds")
print("=" * 50)

class FeistelCipher:
    def __init__(self, rounds=4):
        self.rounds = rounds
    
    def round_function(self, right_half, round_key):
        """
        F-function: Takes right half and round key, produces output
        In real ciphers, this includes substitution, permutation, and XOR
        """
        # Simple F-function: XOR with key and apply bit rotation
        result = right_half ^ round_key
        # Simple confusion: multiply by 3 and take mod 256
        result = (result * 3) % 256
        return result
    
    def encrypt_block(self, block, keys):
        """
        Encrypt a single block using Feistel structure
        Formula: L_i = R_{i-1}, R_i = L_{i-1} XOR F(R_{i-1}, K_i)
        """
        # Split block into left and right halves (assuming 16-bit block)
        left = (block >> 8) & 0xFF
        right = block & 0xFF
        
        print(f"\nInitial: L0={left:08b} ({left:3d}), R0={right:08b} ({right:3d})")
        
        for i in range(self.rounds):
            # Save old right for left update
            old_right = right
            
            # Calculate new right = left XOR F(right, key)
            f_output = self.round_function(right, keys[i])
            right = left ^ f_output
            
            # New left = old right
            left = old_right
            
            print(f"Round {i+1}: L={left:08b} ({left:3d}), R={right:08b} ({right:3d}), F={f_output:08b}")
        
        # Combine halves (swap final left and right)
        ciphertext = (right << 8) | left
        return ciphertext
    
    def decrypt_block(self, block, keys):
        """Decrypt using same Feistel structure with keys in reverse order"""
        # Split block
        left = (block >> 8) & 0xFF
        right = block & 0xFF
        
        print(f"\nDecrypt - Initial: L0={left:08b}, R0={right:08b}")
        
        for i in range(self.rounds-1, -1, -1):
            old_right = right
            f_output = self.round_function(right, keys[i])
            right = left ^ f_output
            left = old_right
            print(f"Round {self.rounds-i}: L={left:08b}, R={right:08b}")
        
        plaintext = (right << 8) | left
        return plaintext

# Demonstration
print("\n--- Feistel Cipher Demonstration ---")
feistel = FeistelCipher(rounds=4)

# Create round keys
round_keys = [0x42, 0x87, 0xAB, 0xCD]
print(f"Round keys: {[hex(k) for k in round_keys]}")

# Test block
plaintext_block = 0x4865  # "He" in ASCII
print(f"\nPlaintext block: {hex(plaintext_block)} ({plaintext_block})")

# Encrypt
ciphertext = feistel.encrypt_block(plaintext_block, round_keys)
print(f"\nCiphertext: {hex(ciphertext)} ({ciphertext})")

# Decrypt
decrypted = feistel.decrypt_block(ciphertext, round_keys)
print(f"\nDecrypted: {hex(decrypted)} ({decrypted})")
print(f"\nSuccess: {plaintext_block == decrypted} ✓")

# Show Feistel formula
print("\n" + "=" * 50)
print("FEISTEL FORMULA:")
print("L_i = R_{i-1}")
print("R_i = L_{i-1} XOR F(R_{i-1}, K_i)")
print("=" * 50)