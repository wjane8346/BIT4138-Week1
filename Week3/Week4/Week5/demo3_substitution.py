# Demonstration 3: Simulate substitutions (S-Boxes)
# BIT4138 Week 5

print("=" * 50)
print("DEMO 3: Simulate Substitutions (S-Boxes)")
print("=" * 50)

# Simple 4x4 S-Box (maps 4-bit input to 4-bit output)
# This is a simplified version of actual AES S-Box
S_BOX = {
    0b0000: 0b1001,  # 0 -> 9
    0b0001: 0b0100,  # 1 -> 4
    0b0010: 0b1010,  # 2 -> 10
    0b0011: 0b1011,  # 3 -> 11
    0b0100: 0b1101,  # 4 -> 13
    0b0101: 0b0001,  # 5 -> 1
    0b0110: 0b1000,  # 6 -> 8
    0b0111: 0b0101,  # 7 -> 5
    0b1000: 0b0110,  # 8 -> 6
    0b1001: 0b0010,  # 9 -> 2
    0b1010: 0b0000,  # 10 -> 0
    0b1011: 0b0011,  # 11 -> 3
    0b1100: 0b1100,  # 12 -> 12
    0b1101: 0b1110,  # 13 -> 14
    0b1110: 0b1111,  # 14 -> 15
    0b1111: 0b0111,  # 15 -> 7
}

# Inverse S-Box for decryption
INV_S_BOX = {v: k for k, v in S_BOX.items()}

def substitute(value, sbox=S_BOX):
    """Apply substitution using S-Box"""
    return sbox.get(value, value)

def substitute_byte(byte, sbox=S_BOX):
    """Substitute each 4-bit nibble in a byte"""
    high_nibble = (byte >> 4) & 0x0F
    low_nibble = byte & 0x0F
    new_high = substitute(high_nibble, sbox)
    new_low = substitute(low_nibble, sbox)
    return (new_high << 4) | new_low

print("\n--- S-Box Demonstration ---")
print("S-Box mapping (4-bit input → 4-bit output):")
for i in range(8):
    row = []
    for j in range(4):
        val = i*4 + j
        row.append(f"{val:04b}→{S_BOX[val]:04b}")
    print("  " + " | ".join(row))

# Demonstrate substitution
print("\n--- Substitution Examples ---")
test_values = [0b0000, 0b0101, 0b1010, 0b1111]
for val in test_values:
    sub_val = substitute(val)
    print(f"Input:  {val:04b} ({val:2d}) → Output: {sub_val:04b} ({sub_val:2d})")

# Demonstrate confusion
print("\n--- Confusion via Substitution ---")
print("Substitution creates CONFUSION - hides relationship between plaintext and ciphertext")
input1 = 0b0001  # 1
input2 = 0b0010  # 2 (only 1 bit different)
output1 = substitute(input1)
output2 = substitute(input2)

print(f"Input 1: {input1:04b} ({input1}) → Output: {output1:04b} ({output1})")
print(f"Input 2: {input2:04b} ({input2}) → Output: {output2:04b} ({output2})")
print(f"Inputs differ by 1 bit, outputs differ significantly → CONFUSION!")

# Character substitution example
print("\n--- Character Substitution (Caesar-style but nonlinear) ---")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Create simple nonlinear substitution
import random
random.seed(42)
char_sub = list(alphabet)
random.shuffle(char_sub)
substitution_map = {alphabet[i]: char_sub[i] for i in range(26)}

plain = "HELLO"
cipher = ''.join(substitution_map[c] for c in plain)
print(f"Plaintext:  {plain}")
print(f"Ciphertext: {cipher}")
print("Note: 'L' maps to same output both times? This is weakness of simple substitution")
print("Modern S-boxes ensure each input maps to unique output (bijective)")