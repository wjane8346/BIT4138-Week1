# Demonstration 4: Analyze weak patterns in LFSR
# BIT4138 Week 4

print("=" * 50)
print("DEMO 4: Analyze Weak Patterns in LFSR")
print("=" * 50)

class LFSR:
    def __init__(self, seed, taps):
        self.state = list(seed)
        self.taps = taps
        self.initial_state = list(seed)
    
    def next_bit(self):
        feedback = 0
        for tap in self.taps:
            feedback ^= self.state[tap]
        output_bit = self.state[-1]
        self.state = [feedback] + self.state[:-1]
        return output_bit
    
    def generate_sequence(self, length):
        bits = []
        for i in range(length):
            bits.append(self.next_bit())
        return bits
    
    def reset(self):
        self.state = list(self.initial_state)

def analyze_weakness(bits, name):
    """Analyze sequence for weak patterns"""
    print(f"\n--- Analyzing {name} ---")
    print(f"Bits: {bits[:30]}...")
    
    # Check for repeating pattern
    ones = sum(bits)
    zeros = len(bits) - ones
    print(f"Ones: {ones}, Zeros: {zeros}")
    
    # Check for long runs
    max_run = 1
    current = 1
    for i in range(1, len(bits)):
        if bits[i] == bits[i-1]:
            current += 1
            max_run = max(max_run, current)
        else:
            current = 1
    
    print(f"Longest run: {max_run}")
    
    if max_run > 10:
        print("WEAKNESS: Very long run detected - non-random pattern")
    
    # Check periodicity
    if len(bits) > 20:
        first_10 = bits[:10]
        next_10 = bits[10:20]
        if first_10 == next_10:
            print("WEAKNESS: Sequence repeats every 10 bits - very short period")
    
    # Overall assessment
    if max_run < 6 and 40 <= (ones/len(bits)*100) <= 60:
        print("Assessment: Appears relatively random")
    else:
        print("Assessment: WEAK - shows predictable patterns")

# Test different LFSR configurations
print("\nComparing weak vs strong LFSR configurations")

# Weak configuration: All zero seed (never changes)
print("\n--- WEAK CONFIGURATION 1: All zero seed ---")
lfsr_weak1 = LFSR(seed=[0,0,0], taps=[2,1])
bits_weak1 = lfsr_weak1.generate_sequence(30)
analyze_weakness(bits_weak1, "All zero seed")

# Weak configuration: Poor tap selection
print("\n--- WEAK CONFIGURATION 2: Poor tap selection (only 1 tap) ---")
lfsr_weak2 = LFSR(seed=[1,0,0], taps=[2])  # Only one tap
bits_weak2 = lfsr_weak2.generate_sequence(30)
analyze_weakness(bits_weak2, "Single tap only")

# Good configuration: Maximum period taps
print("\n--- GOOD CONFIGURATION: Maximum period taps ---")
lfsr_good = LFSR(seed=[1,0,0], taps=[2,1])
bits_good = lfsr_good.generate_sequence(30)
analyze_weakness(bits_good, "Maximum period taps (3-bit)")

print("\n" + "=" * 50)
print("WEAKNESS SUMMARY:")
print("1. All-zero seed never changes output")
print("2. Poor tap selection reduces period")
print("3. Short periods create repeating patterns")
print("4. LFSR alone is NOT cryptographically secure")
print("=" * 50)