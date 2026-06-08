# Class Activity 1: Finding Sequence Period
# BIT4138 Week 3

print("=" * 50)
print("ACTIVITY 1: Finding Sequence Period")
print("=" * 50)

def find_period(sequence):
    """Find the period of a repeating sequence"""
    seen = {}
    for i, value in enumerate(sequence):
        if value in seen:
            period = i - seen[value]
            return period, seen[value], value
        seen[value] = i
    return None, None, None

# Test sequence with period 3
test_sequence = [2, 5, 7, 2, 5, 7, 2, 5, 7]
print(f"\nTest sequence: {test_sequence}")
period, position, value = find_period(test_sequence)
print(f"Period found: {period} (repeating every {period} values)")

# LCG sequence period test
print("\n--- LCG Period Analysis ---")
state = 1
a, c, m = 1664525, 1013904223, 2**32
lcg_values = []
seen = {}

for i in range(10000):
    state = (a * state + c) % m
    if state in seen:
        period = i - seen[state]
        print(f"LCG period: {period} (found at position {i})")
        break
    seen[state] = i
else:
    print("Period not found within 10000 values (period > 10000)")

# Effect of modulus on period
print("\n--- Effect of Modulus on Period ---")
small_m = 16
state = 1
a, c = 5, 1
values = []
seen = {}

for i in range(100):
    state = (a * state + c) % small_m
    if state in seen:
        period = i - seen[state]
        print(f"Modulus {small_m}: Period = {period}")
        break
    seen[state] = i