#!/usr/bin/env python3
"""
BIT4138 Week 3 - Assignment 1
Randomness Testing Program

Requirements:
- Generates 100+ random bits
- Performs statistical tests (Frequency, Runs, Mean, Chi-Square)
- Displays interpretations

Student Name: [Your Name]
Student ID: [Your ID]
Date: [Current Date]
"""

import random
import math

def generate_bits(n=100, method="lcg", seed=42):
    """Generate n random bits using specified method"""
    bits = []
    
    if method == "lcg":
        state = seed
        a, c, m = 1664525, 1013904223, 2**32
        for i in range(n):
            state = (a * state + c) % m
            bits.append(state & 1)
    else:
        # Python random
        for i in range(n):
            bits.append(random.randint(0, 1))
    
    return bits

def frequency_test(bits):
    """Test 1: Frequency Test - Check balance of 0s and 1s"""
    n = len(bits)
    ones = sum(bits)
    zeros = n - ones
    ones_pct = ones / n * 100
    
    print("\n" + "-" * 40)
    print("TEST 1: FREQUENCY TEST")
    print("-" * 40)
    print(f"Total bits: {n}")
    print(f"Number of 1s: {ones} ({ones_pct:.1f}%)")
    print(f"Number of 0s: {zeros} ({100-ones_pct:.1f}%)")
    
    if 45 <= ones_pct <= 55:
        print(">> Interpretation: PASS - Bits are well balanced")
        return True
    else:
        print(">> Interpretation: FAIL - Bits are imbalanced")
        return False

def runs_test(bits):
    """Test 2: Runs Test - Check patterns of consecutive bits"""
    n = len(bits)
    runs = []
    current = 1
    
    for i in range(1, n):
        if bits[i] == bits[i-1]:
            current += 1
        else:
            runs.append(current)
            current = 1
    runs.append(current)
    
    total_runs = len(runs)
    avg_run = sum(runs) / len(runs)
    expected_runs = (2 * n - 1) / 3
    
    print("\n" + "-" * 40)
    print("TEST 2: RUNS TEST")
    print("-" * 40)
    print(f"Total runs: {total_runs}")
    print(f"Run lengths: {runs[:10]}{'...' if len(runs)>10 else ''}")
    print(f"Average run length: {avg_run:.2f}")
    print(f"Expected runs (random): {expected_runs:.0f}")
    
    if abs(total_runs - expected_runs) < math.sqrt(n):
        print(">> Interpretation: PASS - Run pattern appears random")
        return True
    else:
        print(">> Interpretation: FAIL - Unusual run pattern detected")
        return False

def mean_test(bits):
    """Test 3: Mean Test - Check average value"""
    n = len(bits)
    mean = sum(bits) / n
    
    print("\n" + "-" * 40)
    print("TEST 3: MEAN TEST")
    print("-" * 40)
    print(f"Mean value: {mean:.4f}")
    print(f"Expected mean: 0.5000")
    print(f"Difference: {abs(mean - 0.5):.4f}")
    
    if 0.45 <= mean <= 0.55:
        print(">> Interpretation: PASS - Mean is close to expected")
        return True
    else:
        print(">> Interpretation: FAIL - Mean deviates too much")
        return False

def chi_square_test(bits):
    """Test 4: Chi-Square Test - Statistical confidence"""
    n = len(bits)
    ones = sum(bits)
    zeros = n - ones
    expected = n / 2
    
    chi_square = ((ones - expected)**2 / expected) + ((zeros - expected)**2 / expected)
    
    print("\n" + "-" * 40)
    print("TEST 4: CHI-SQUARE TEST")
    print("-" * 40)
    print(f"Chi-square value: {chi_square:.4f}")
    print(f"Critical value (95% confidence): 3.841")
    
    if chi_square < 3.841:
        print(">> Interpretation: PASS - Statistically random")
        return True
    else:
        print(">> Interpretation: FAIL - Shows statistical bias")
        return False

def main():
    print("=" * 60)
    print("RANDOMNESS TESTING PROGRAM")
    print("=" * 60)
    
    # Get user input for sequence length
    try:
        n = int(input("\nEnter number of bits to generate (minimum 100): "))
        if n < 100:
            print("Using minimum of 100 bits")
            n = 100
    except:
        print("Using default: 100 bits")
        n = 100
    
    # Generate bits
    bits = generate_bits(n, method="lcg")
    
    # Display first 50 bits
    print(f"\nGenerated {n} bits (first 50 shown):")
    print(bits[:50])
    
    # Visual representation
    visual = ''.join(['█' if b==1 else '░' for b in bits[:50]])
    print(f"Visual: {visual}")
    
    # Run all tests
    results = []
    results.append(frequency_test(bits))
    results.append(runs_test(bits))
    results.append(mean_test(bits))
    results.append(chi_square_test(bits))
    
    # Overall result
    print("\n" + "=" * 60)
    print("OVERALL RESULT")
    print("=" * 60)
    
    passed = sum(results)
    print(f"Tests passed: {passed} out of {len(results)}")
    
    if passed == 4:
        print("\nFINAL INTERPRETATION: The sequence appears RANDOM")
        print("(But remember: LCG is still cryptographically weak!)")
    elif passed >= 2:
        print("\nFINAL INTERPRETATION: The sequence shows MIXED results")
    else:
        print("\nFINAL INTERPRETATION: The sequence is WEAK - not random")
    
    print("\n" + "=" * 60)
    print("IMPORTANT NOTE:")
    print("Statistical randomness does NOT equal cryptographic security.")
    print("LCG passes these tests but is still predictable.")
    print("Use CSPRNGs like ChaCha20 for real encryption.")
    print("=" * 60)

if __name__ == "__main__":
    main()