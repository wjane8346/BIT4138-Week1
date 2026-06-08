#!/usr/bin/env python3
"""
BIT4138 Week 4 - Assignment 1
LFSR Generator with Period Detection

Requirements:
- Develop LFSR generator
- Detect repeated states
- Estimate sequence period
- Display weaknesses

Student Name: [Your Name]
Student ID: [Your ID]
Date: [Current Date]
"""

class LFSR:
    def __init__(self, seed, taps):
        """
        Initialize LFSR
        
        seed: list of bits (e.g., [1,0,0,0])
        taps: list of tap positions (e.g., [3,2] for 4-bit LFSR)
        """
        self.state = list(seed)
        self.taps = taps
        self.initial_state = list(seed)
        self.n = len(seed)  # Number of bits
    
    def next_bit(self):
        """Generate next output bit and shift register"""
        # Calculate feedback (XOR of tap positions)
        feedback = 0
        for tap in self.taps:
            feedback ^= self.state[tap]
        
        # Output is the rightmost bit
        output_bit = self.state[-1]
        
        # Shift register: insert feedback at front, drop last bit
        self.state = [feedback] + self.state[:-1]
        
        return output_bit
    
    def generate_bits(self, count):
        """Generate specified number of bits"""
        bits = []
        for i in range(count):
            bits.append(self.next_bit())
        return bits
    
    def get_state(self):
        """Return current state as tuple (for hashing)"""
        return tuple(self.state)
    
    def reset(self):
        """Reset to initial state"""
        self.state = list(self.initial_state)
    
    def detect_period(self, max_steps=2000):
        """
        Detect period by finding repeated states
        Returns: (period, steps_before_repeat)
        """
        self.reset()
        seen_states = {}
        
        for step in range(max_steps):
            current_state = self.get_state()
            
            if current_state in seen_states:
                period = step - seen_states[current_state]
                return period, step
            
            seen_states[current_state] = step
            self.next_bit()  # Advance to next state
        
        return None, None  # Period not found
    
    def analyze_weaknesses(self):
        """Identify weaknesses in LFSR configuration"""
        weaknesses = []
        
        # Check 1: All-zero seed
        if all(bit == 0 for bit in self.initial_state):
            weaknesses.append("CRITICAL: All-zero seed - LFSR will never generate output")
        
        # Check 2: All-one seed (fine, just note)
        if all(bit == 1 for bit in self.initial_state):
            weaknesses.append("Note: All-one seed is acceptable")
        
        # Check 3: Check if taps are valid
        for tap in self.taps:
            if tap >= self.n or tap < 0:
                weaknesses.append(f"ERROR: Invalid tap position {tap} for {self.n}-bit LFSR")
        
        # Check 4: Only one tap
        if len(self.taps) == 1:
            weaknesses.append("WEAK: Only one tap - reduces randomness quality")
        
        # Check 5: Even number of taps (fine, no issue)
        
        return weaknesses
    
    def get_max_period(self):
        """Calculate maximum possible period for n-bit LFSR"""
        return (2 ** self.n) - 1


def main():
    print("=" * 60)
    print("LFSR GENERATOR WITH PERIOD DETECTION")
    print("=" * 60)
    
    # Get user input for LFSR configuration
    print("\n--- Configure LFSR ---")
    
    # Method 1: Use preset configurations
    print("\nChoose a preset configuration:")
    print("1. 3-bit LFSR (taps [2,1]) - Max period 7")
    print("2. 4-bit LFSR (taps [3,2]) - Max period 15")
    print("3. Custom configuration")
    
    choice = input("\nEnter choice (1/2/3): ")
    
    if choice == '1':
        seed = [1,0,0]
        taps = [2,1]
        name = "3-bit LFSR"
    elif choice == '2':
        seed = [1,0,0,0]
        taps = [3,2]
        name = "4-bit LFSR"
    else:
        # Custom configuration
        n = int(input("Enter number of bits (e.g., 4): "))
        seed_input = input(f"Enter {n} bits as 0s and 1s (e.g., 1000): ")
        seed = [int(b) for b in seed_input[:n]]
        taps_input = input("Enter tap positions (e.g., 3,2): ")
        taps = [int(t) for t in taps_input.split(',')]
        name = f"{n}-bit custom LFSR"
    
    # Create LFSR
    lfsr = LFSR(seed, taps)
    
    # Display configuration
    print("\n" + "=" * 60)
    print(f"LFSR CONFIGURATION: {name}")
    print("=" * 60)
    print(f"Seed: {seed}")
    print(f"Taps: {taps}")
    print(f"Number of bits: {lfsr.n}")
    print(f"Maximum possible period: {lfsr.get_max_period()}")
    
    # Check weaknesses
    weaknesses = lfsr.analyze_weaknesses()
    if weaknesses:
        print("\n--- WEAKNESSES DETECTED ---")
        for w in weaknesses:
            print(f"⚠ {w}")
    else:
        print("\n✓ No obvious weaknesses in configuration")
    
    # Generate and display sequence
    print("\n--- GENERATING SEQUENCE ---")
    num_bits = int(input("How many bits to generate? (default 50): ") or "50")
    lfsr.reset()
    bits = lfsr.generate_bits(num_bits)
    
    print(f"\nGenerated {len(bits)} bits:")
    print(f"Bits: {bits}")
    
    # Visual representation
    visual = ''.join(['█' if b==1 else '░' for b in bits[:60]])
    print(f"Visual: {visual}...")
    
    # Period detection
    print("\n--- PERIOD DETECTION ---")
    period, step = lfsr.detect_period(max_steps=2000)
    
    if period:
        print(f"✓ Period detected: {period} bits")
        print(f"  Sequence repeats every {period} bits")
        print(f"  Maximum possible: {lfsr.get_max_period()}")
        
        if period == lfsr.get_max_period():
            print("  ✓ Maximum period achieved - optimal configuration")
        else:
            print("  ⚠ Not maximum period - consider different tap positions")
    else:
        print("  Period not detected within 2000 steps")
        print("  (Period may be longer than 2000 bits)")
    
    # Statistical analysis
    print("\n--- STATISTICAL ANALYSIS ---")
    ones = sum(bits)
    zeros = len(bits) - ones
    print(f"Ones: {ones} ({ones/len(bits)*100:.1f}%)")
    print(f"Zeros: {zeros} ({zeros/len(bits)*100:.1f}%)")
    
    # Run detection
    runs = []
    current = 1
    for i in range(1, len(bits)):
        if bits[i] == bits[i-1]:
            current += 1
        else:
            runs.append(current)
            current = 1
    runs.append(current)
    
    print(f"Number of runs: {len(runs)}")
    print(f"Longest run: {max(runs)}")
    
    # Overall assessment
    print("\n" + "=" * 60)
    print("OVERALL ASSESSMENT")
    print("=" * 60)
    
    if period and period == lfsr.get_max_period():
        print("✓ LFSR has maximum period")
    else:
        print("⚠ LFSR period is suboptimal")
    
    if max(runs) > 15:
        print("⚠ Very long runs detected - may indicate pattern")
    else:
        print("✓ Run lengths appear reasonable")
    
    print("\nCRYPTANALYSIS NOTE:")
    print("Even with maximum period, LFSR is cryptographically weak.")
    print("Berlekamp-Massey algorithm can reconstruct LFSR from 2n bits.")
    print("Do not use LFSR alone for encryption.")
    print("=" * 60)

if __name__ == "__main__":
    main()