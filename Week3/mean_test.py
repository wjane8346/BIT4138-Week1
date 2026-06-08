# Demonstration 5: Mean Test
# BIT4138 Week 3

import random

def mean_test(bits):
    """Calculate mean of binary sequence (should be ~0.5)"""
    mean = sum(bits) / len(bits)
    
    print(f"Mean value: {mean:.4f}")
    print(f"Expected mean (random): 0.5000")
    print(f"Difference: {abs(mean - 0.5):.4f}")
    
    if 0.45 <= mean <= 0.55:
        print("Result: PASS - Mean is close to expected")
    else:
        print("Result: FAIL - Mean deviates too much")

print("=" * 50)
print("DEMO 5: Mean Test")
print("=" * 50)

# Generate 100 random bits
bits = [random.randint(0, 1) for i in range(100)]

print(f"\nBits: {bits[:30]}...")
print(f"Total bits: {len(bits)}\n")

mean_test(bits)