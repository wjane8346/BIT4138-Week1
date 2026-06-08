seed = int(input("Enter seed: "))
a, c, m = 1664525, 1013904223, 2**32
state = seed
values = []
for i in range(25):
    state = (a * state + c) % m
    values.append(state)
print(f"Generated values: {values}")
print(f"Period: Up to {m} values before repetition")
print(f"Randomness: Values appear uniformly distributed but are fully deterministic")