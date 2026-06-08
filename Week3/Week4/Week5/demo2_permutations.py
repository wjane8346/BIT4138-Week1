# Demonstration 2: Apply permutations
# BIT4138 Week 5

print("=" * 50)
print("DEMO 2: Apply Permutations")
print("=" * 50)

def apply_permutation(data, permutation):
    """
    Rearrange data according to permutation mapping
    permutation: list of indices showing new order
    """
    result = [data[i] for i in permutation]
    return result

def inverse_permutation(permutation):
    """Find inverse of a permutation"""
    inverse = [0] * len(permutation)
    for i, pos in enumerate(permutation):
        inverse[pos] = i
    return inverse

# Example 1: Simple permutation of bits
print("\n--- Example 1: Permuting Bits ---")
bits = [1, 0, 1, 1, 0, 0, 1, 0]
print(f"Original bits: {bits}")

# Permutation that rearranges positions
# Position 0 goes to position 3, position 1 goes to 0, etc.
permutation = [3, 0, 5, 1, 7, 2, 6, 4]
permuted = apply_permutation(bits, permutation)
print(f"Permutation:  {permutation}")
print(f"Permuted bits: {permuted}")

# Reverse the permutation
inv_perm = inverse_permutation(permutation)
reversed_bits = apply_permutation(permuted, inv_perm)
print(f"\nInverse permutation: {inv_perm}")
print(f"Reversed bits: {reversed_bits}")
print(f"Recovered original: {bits == reversed_bits} ✓")

# Example 2: Permuting characters in a block
print("\n--- Example 2: Permuting Characters in Block ---")
block = "HELLOWORLD"
print(f"Original block: {block}")

# Character permutation
char_perm = [4, 0, 7, 2, 8, 1, 5, 9, 3, 6]
char_list = list(block)
permuted_chars = apply_permutation(char_list, char_perm)
permuted_block = ''.join(permuted_chars)
print(f"Permutation: {char_perm}")
print(f"Permuted block: {permuted_block}")

# Example 3: Effect of permutation on diffusion
print("\n--- Example 3: Permutation Spreads Changes ---")
original = list("ABCDEFGH")
print(f"Original: {original}")

# Change one character in original
modified = list("ABCDEFGH")
modified[0] = 'Z'
print(f"Modified: {modified}")

# Apply same permutation to both
p = [2, 5, 0, 7, 1, 4, 6, 3]
perm_original = apply_permutation(original, p)
perm_modified = apply_permutation(modified, p)

print(f"Permutation: {p}")
print(f"Permuted original: {perm_original}")
print(f"Permuted modified: {perm_modified}")

# Find differences
diff_count = sum(1 for i in range(8) if perm_original[i] != perm_modified[i])
print(f"\nOne change in original caused {diff_count} changes in permuted output")
print("This is DIFFUSION - spreading plaintext changes throughout ciphertext")