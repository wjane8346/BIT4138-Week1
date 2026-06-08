def menu():
    while True:
        print("\n1. Encrypt\n2. Decrypt\n3. Exit")
        choice = input("Choice: ")
        if choice == '1':
            text = input("Text: ")
            key = input("Key: ")
            result = ''.join(chr(ord(t) ^ ord(key[i % len(key)])) for i,t in enumerate(text))
            print(f"Encrypted (hex): {result.encode().hex()}")
        elif choice == '2':
            hex_input = input("Hex ciphertext: ")
            key = input("Key: ")
            bytes_data = bytes.fromhex(hex_input)
            result = ''.join(chr(b ^ ord(key[i % len(key)])) for i,b in enumerate(bytes_data))
            print(f"Decrypted: {result}")
        elif choice == '3':
            break
menu()