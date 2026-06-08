import random

print("=== Python Random Number Generator ===")
print("Five random integers between 1 and 100:")
for i in range(5):
    print(f"Number {i+1}: {random.randint(1, 100)}")

print("\nFive random floats between 0 and 1:")
for i in range(5):
    print(f"Float {i+1}: {random.random()}")