# Demonstration 2: Implement an LCG generator
# BIT4138 Week 3

print("=" * 50)
print("DEMO 2: LCG Generator Implementation")
print("=" * 50)

class LCGGenerator:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m
    
    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state
    
    def generate(self, count):
        return [self.next() for i in range(count)]

# Test the generator
print("\nLCG Formula: X_{n+1} = (a * X_n + c) mod m")
print(f"Parameters: a=1664525, c=1013904223, m=2^32\n")

seed = 42
lcg = LCGGenerator(seed)

print(f"Seed: {seed}")
print("First 10 generated numbers:")
for i in range(10):
    value = lcg.next()
    print(f"  {i+1}: {value}")
