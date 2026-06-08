# Demonstration 5: Observe Avalanche Effect
# BIT4138 Week 5

print("=" * 50)
print("DEMO 5: Avalanche Effect")
print("=" * 50)

class SimpleBlockCipher:
    def __init__(self, rounds=4):
        self.rounds = rounds
    
    def f_function(self, right, key):
        """Simple F-function for demonstration"""
        result = right ^ key
        result = (result * 7) % 256
        result = result ^ (result >> 4)
        return result & 0xFF
    
    def encrypt(self, plaintext, key):
        """Simple Feistel encryption"""
        # Convert text to number
        if isinstance(plaintext, str):
            plaintext = int.from_bytes(plaintext.encode(), 'big')
        
        left = (plaintext >> 8) & 0xFF
        right = plaintext & 0xFF
        
        for i in range(self.rounds):
            old_right = right
            f_out = self.f_function(right, key ^ i)
            right = left ^ f_out
            left = old_right
        
        return (right << 8) | left

def hamming_distance(a, b):
    """Calculate Hamming distance (number of differing bits)"""
    xor_result = a ^ b
    return bin(xor_result).count('1')

# Test the avalanche effect
cipher = SimpleBlockCipher(rounds=4)
key = 0x42

print("\n--- Avalanche Effect Test ---")
print("Changing 1 bit in plaintext should change ~50% of ciphertext bits")

# Original plaintext
plaintext1 = 0b1010101010101010  # 16 bits
ciphertext1 = cipher.encrypt(plaintext1, key)

print(f"\nOriginal plaintext:  {plaintext1:016b}")
print(f"Ciphertext:          {ciphertext1:016b}")

# Test multiple single-bit changes
results = []
for bit_pos in range(16):
    # Flip one bit
    plaintext2 = plaintext1 ^ (1 << bit_pos)
    ciphertext2 = cipher.encrypt(plaintext2, key)
    
    # Calculate avalanche
    diff = hamming_distance(ciphertext1, ciphertext2)
    avalanche_pct = (diff / 16) * 100
    results.append(avalanche_pct)
    
    if bit_pos < 5:  # Show first 5
        print(f"\nFlip bit {bit_pos}:")
        print(f"  Modified plaintext: {plaintext2:016b}")
        print(f"  New ciphertext:     {ciphertext2:016b}")
        print(f"  Bits changed: {diff}/16 ({avalanche_pct:.0f}%)")

# Summary
print("\n" + "-" * 40)
print("AVALANCHE EFFECT SUMMARY")
print("-" * 40)
print(f"Average avalanche: {sum(results)/len(results):.1f}%")
print(f"Minimum: {min(results):.0f}%")
print(f"Maximum: {max(results):.0f}%")
print(f"Standard deviation: {__import__('statistics').stdev(results):.1f}%")

print("\n" + "=" * 50)
print("AVALANCHE PRINCIPLE:")
print("A small change in plaintext (1 bit) causes large change")
print("in ciphertext (~50% of bits). This hides patterns and")
print("makes cryptanalysis much harder.")
print("=" * 50)