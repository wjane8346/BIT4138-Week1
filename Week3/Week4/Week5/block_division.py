# Demonstration 1: Divide plaintext into blocks
# BIT4138 Week 5 - Block Ciphers and Feistel Structures

print("=" * 50)
print("DEMO 1: Divide Plaintext into Blocks")
print("=" * 50)

def divide_into_blocks(plaintext, block_size=8):
    """Divide plaintext into fixed-size blocks"""
    blocks = []
    
    # Convert to uppercase and remove spaces for simplicity
    text = plaintext.upper().replace(" ", "")
    
    # Split into blocks
    for i in range(0, len(text), block_size):
        block = text[i:i+block_size]
        # Pad last block if needed
        if len(block) < block_size:
            block = block + "X" * (block_size - len(block))
        blocks.append(block)
    
    return blocks

# Test the function
plaintext = "HELLO WORLD THIS IS BLOCK CIPHER DEMONSTRATION"
print(f"\nOriginal text: {plaintext}")
print(f"Text length: {len(plaintext)} characters")

block_size = 8
blocks = divide_into_blocks(plaintext, block_size)

print(f"\nBlock size: {block_size} characters")
print(f"Number of blocks: {len(blocks)}")
print("\nBlocks:")
for i, block in enumerate(blocks):
    print(f"  Block {i+1}: {block}")

# Show with different block sizes
print("\n" + "-" * 40)
print("Different Block Sizes:")
for size in [4, 6, 8]:
    blocks = divide_into_blocks(plaintext, size)
    print(f"\nBlock size {size}: {len(blocks)} blocks")
    print(f"First 3 blocks: {blocks[:3]}")