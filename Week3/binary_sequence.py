# Demonstration 1: Generate binary random sequences
# BIT4138 Week 3

import random

print("=" * 50)
print("DEMO 1: Generate Binary Random Sequences")
print("=" * 50)

# Method 1: Using random module
binary_sequence = [random.randint(0, 1) for i in range(20)]
print(f"\nBinary sequence (20 bits): {binary_sequence}")

# Method 2: Using LCG to generate bits
state = 42
a, c, m = 1664525, 1013904223, 2**32
lcg_bits = []

for i in range(20):
    state = (a * state + c) % m
    bit = state & 1  # Take least significant bit
    lcg_bits.append(bit)

print(f"LCG binary sequence (20 bits): {lcg_bits}")

# Visual representation
visual = ''.join(['1' if b==1 else '0' for b in lcg_bits])
print(f"\nVisual: {visual}")