# Demonstration 1: Generate LFSR sequences
# BIT4138 Week 4 - Stream Cipher Cryptanalysis

print("=" * 50)
print("DEMO 1: Generate LFSR Sequences")
print("=" * 50)

class LFSR:
    def __init__(self, seed, taps):
        """
        Linear Feedback Shift Register
        seed: initial state (list of bits)
        taps: positions that affect feedback (list of indices)
        """
        self.state = list(seed)
        self.taps = taps
        self.initial_state = list(seed)
    
    def next_bit(self):
        """Generate next bit using XOR of tap positions"""
        # Calculate feedback bit (XOR of tap positions)
        feedback = 0
        for tap in self.taps:
            feedback ^= self.state[tap]
        
        # Shift right and insert feedback at beginning
        output_bit = self.state[-1]  # Output the rightmost bit
        self.state = [feedback] + self.state[:-1]
        
        return output_bit
    
    def generate_sequence(self, length):
        """Generate sequence of bits"""
        bits = []
        for i in range(length):
            bits.append(self.next_bit())
        return bits
    
    def reset(self):
        """Reset to initial state"""
        self.state = list(self.initial_state)

# Example 1: LFSR with taps at positions 2 and 1 (Fibonacci LFSR)
print("\n--- LFSR Example 1: Taps at positions 2 and 1 ---")
print("Formula: s_n = s_{n-1} XOR s_{n-3}")
print("(Using 3-bit LFSR with seed [1,0,0])")

lfsr1 = LFSR(seed=[1,0,0], taps=[2,1])  # positions 2 and 1
bits = lfsr1.generate_sequence(20)
print(f"Generated bits: {bits}")

# Example 2: LFSR with different taps
print("\n--- LFSR Example 2: Different taps ---")
print("Formula: s_n = s_{n-1} XOR s_{n-2}")
print("(Using 3-bit LFSR with seed [1,1,0])")

lfsr2 = LFSR(seed=[1,1,0], taps=[2,0])
bits = lfsr2.generate_sequence(20)
print(f"Generated bits: {bits}")

# Visual representation
visual = ''.join(str(b) for b in bits)
print(f"Visual: {visual}")