# Demonstration 4: Runs Test
# BIT4138 Week 3

import random
import math

def runs_test(bits):
    """Count runs of consecutive identical bits"""
    if not bits:
        return
    
    runs = []
    current_run = 1
    
    for i in range(1, len(bits)):
        if bits[i] == bits[i-1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1
    runs.append(current_run)
    
    total_runs = len(runs)
    avg_run_length = sum(runs) / len(runs)
    expected_runs = (2 * len(bits) - 1) / 3
    
    print(f"Total runs found: {total_runs}")
    print(f"Run lengths: {runs}")
    print(f"Average run length: {avg_run_length:.2f}")
    print(f"Expected runs (random): {expected_runs:.0f}")
    
    if abs(total_runs - expected_runs) < math.sqrt(len(bits)):
        print("Result: PASS - Run pattern appears random")
    else:
        print("Result: FAIL - Unusual run pattern detected")

print("=" * 50)
print("DEMO 4: Runs Test")
print("=" * 50)

# Generate 100 random bits
bits = [random.randint(0, 1) for i in range(100)]

print(f"\nBits: {bits[:30]}...")
print(f"Total bits: {len(bits)}\n")

runs_test(bits)