# Demonstration 3: Frequency Test
# BIT4138 Week 3

import random

def frequency_test(bits):
    """Count number of 0s and 1s in binary sequence"""
    ones = sum(bits)
    zeros = len(bits) - ones
    total = len(bits)
    
    print(f"Total bits: {total}")
    print(f"Number of 1s: {ones} ({ones/total*100:.1f}%)")
    print(f"Number of 0s: {zeros} ({zeros/total*100:.1f}%)")
    
    if 45 <= (ones/total*100) <= 55:
        print("Result: PASS - Bits are balanced")
    else:
        print("Result: FAIL - Bits are imbalanced")

print("=" * 50)
print("DEMO 3: Frequency Test")
print("=" * 50)

# Generate 100 random bits
bits = [random.randint(0, 1) for i in range(100)]

print(f"\nFirst 20 bits: {bits[:20]}")
print(f"Total bits: {len(bits)}\n")

frequency_test(bits)