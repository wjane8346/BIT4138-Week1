# Demonstration 3: Observe predictability in LFSR
# BIT4138 Week 4

print("=" * 50)
print("DEMO 3: Observe Predictability in LFSR")
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
    
    def peek_next_bit(self):
        """Predict next bit without changing state"""
        feedback = 0
        for tap in self.taps:
            feedback ^= self.state[tap]
        return feedback  # This will become the new first bit
    
    def reset(self):
        self.state = list(self.initial_state)

# Demonstrate predictability
print("\n--- If you know LFSR taps, you can predict future bits ---")

lfsr = LFSR(seed=[1,0,0], taps=[2,1])
lfsr.reset()

print(f"LFSR taps: {lfsr.taps}")
print(f"Initial state: {lfsr.state}")
print("\nGenerating bits and predicting next:")

for i in range(10):
    current_state = lfsr.state
    next_predicted = lfsr.peek_next_bit()
    actual_bit = lfsr.next_bit()
    
    print(f"Step {i+1}: State {current_state} → Output {actual_bit} (Predicted next: {next_predicted})")
    
    if i < 9:
        print(f"         Next state will be: [{next_predicted}] + {current_state[:-1]}")
    print()

print("=" * 50)
print("CRYPTANALYSIS INSIGHT:")
print("Once an attacker knows the LFSR taps and state,")
print("ALL future bits can be predicted.")
print("This is why LFSR alone is NOT secure for cryptography.")
print("=" * 50)