#!/usr/bin/env python3
"""
Linear Congruential Generator (LCG) Implementation
For BIT4138 Week 2 - Stream Ciphers and PRNGs
"""

class LCG:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        """
        Initialize LCG with parameters
        
        Standard parameters (Numerical Recipes):
        a = 1664525 (multiplier)
        c = 1013904223 (increment)
        m = 2^32 (modulus)
        """
        self.state = seed
        self.a = a
        self.c = c
        self.m = m
        self.initial_seed = seed
        
    def next(self):
        """Generate next pseudorandom number"""
        self.state = (self.a * self.state + self.c) % self.m
        return self.state
    
    def generate_sequence(self, count):
        """Generate sequence of 'count' numbers"""
        sequence = []
        for i in range(count):
            sequence.append(self.next())
        return sequence
    
    def reset(self):
        """Reset generator to initial seed"""
        self.state = self.initial_seed


def main():
    print("=" * 60)
    print("LINEAR CONGRUENTIAL GENERATOR (LCG) DEMONSTRATION")
    print("=" * 60)
    
    # Test different seeds
    seeds = [42, 123, 9999]
    
    for seed in seeds:
        print(f"\n--- Seed: {seed} ---")
        lcg = LCG(seed)
        
        print(f"First 10 generated numbers:")
        for i in range(10):
            value = lcg.next()
            print(f"  {i+1}: {value}")
        
        # Generate and show period detection
        print(f"\nDetecting period with seed {seed}...")
        lcg.reset()
        seen = {}
        period = 0
        for i in range(5000):  # Check first 5000 values
            val = lcg.next()
            if val in seen:
                period = i - seen[val]
                print(f"  First repetition found at position {i}")
                print(f"  Value {val} first appeared at position {seen[val]}")
                print(f"  Detected period length: {period}")
                break
            seen[val] = i
        if period == 0:
            print("  No repetition detected within 5000 values (period > 5000)")
    
    # Demonstrate effect of changing parameters
    print("\n" + "=" * 60)
    print("EFFECT OF CHANGING LCG PARAMETERS")
    print("=" * 60)
    
    print("\n--- Default parameters (a=1664525, c=1013904223, m=2^32) ---")
    lcg1 = LCG(1)
    print(f"First 5 values: {lcg1.generate_sequence(5)}")
    
    print("\n--- Poor parameters (a=1, c=1, m=10) ---")
    class LCG_Poor:
        def __init__(self, seed):
            self.state = seed
            self.a = 1
            self.c = 1
            self.m = 10
        def next(self):
            self.state = (self.a * self.state + self.c) % self.m
            return self.state
        def generate_sequence(self, count):
            seq = []
            for i in range(count):
                seq.append(self.next())
            return seq
    
    lcg2 = LCG_Poor(1)
    print(f"First 20 values: {lcg2.generate_sequence(20)}")
    print(">> OBSERVATION: Very short period and predictable pattern!")
    
    print("\n--- Cryptographic parameters (a=1103515245, c=12345, m=2^31) ---")
    class LCG_Crypto:
        def __init__(self, seed):
            self.state = seed
            self.a = 1103515245
            self.c = 12345
            self.m = 2**31
        def next(self):
            self.state = (self.a * self.state + self.c) % self.m
            return self.state
        def generate_sequence(self, count):
            seq = []
            for i in range(count):
                seq.append(self.next())
            return seq
    
    lcg3 = LCG_Crypto(1)
    print(f"First 10 values: {lcg3.generate_sequence(10)}")
    print(">> OBSERVATION: Better quality but still cryptographically weak")
    
    print("\n" + "=" * 60)
    print("LCG FORMULA: X_{n+1} = (a * X_n + c) mod m")
    print("=" * 60)

if __name__ == "__main__":
    main()