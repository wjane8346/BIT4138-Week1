# Class Activity 2: Randomness Observation
# BIT4138 Week 3

import random

print("=" * 50)
print("ACTIVITY 2: Randomness Observation")
print("=" * 50)

def observe_randomness(generator_type, bits):
    """Observe and report randomness quality"""
    ones = sum(bits)
    zeros = len(bits) - ones
    
    # Frequency balance
    freq_balance = abs(ones - zeros)
    
    # Count runs
    runs = 1
    for i in range(1, len(bits)):
        if bits[i] != bits[i-1]:
            runs += 1
    
    print(f"\n--- {generator_type} ---")
    print(f"Bits: {bits[:40]}...")
    print(f"Ones: {ones}, Zeros: {zeros}, Balance diff: {freq_balance}")
    print(f"Number of runs: {runs}")
    print(f"Longest run: {find_longest_run(bits)}")
    
    # Observation
    if freq_balance < 20 and runs > 20:
        print("Observation: GOOD - Appears random")
    else:
        print("Observation: WEAK - Shows patterns")

def find_longest_run(bits):
    """Find longest consecutive identical bits"""
    max_run = 1
    current = 1
    for i in range(1, len(bits)):
        if bits[i] == bits[i-1]:
            current += 1
            max_run = max(max_run, current)
        else:
            current = 1
    return max_run

# Compare three sources
print("\nComparing randomness from different sources:")

# Source 1: Python random (good)
bits1 = [random.randint(0, 1) for i in range(100)]
observe_randomness("Python random module", bits1)

# Source 2: LCG with good parameters
state = 42
a, c, m = 1664525, 1013904223, 2**32
bits2 = []
for i in range(100):
    state = (a * state + c) % m
    bits2.append(state & 1)
observe_randomness("LCG (good parameters)", bits2)

# Source 3: Weak LCG (poor randomness)
state = 1
a, c, m = 1, 1, 10
bits3 = []
for i in range(100):
    state = (a * state + c) % m
    bits3.append(state & 1)
observe_randomness("LCG (weak parameters: a=1,c=1,m=10)", bits3)

print("\n" + "=" * 50)
print("CONCLUSION: Weak generators show obvious patterns and poor balance")