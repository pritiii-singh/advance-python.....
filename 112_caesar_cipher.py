"""
Project 112: Caesar Cipher Encryptor & Decryptor
Concepts: ASCII code manipulation (ord, chr), modular arithmetic, brute-force search.
"""
def caesar(text, shift, mode="encrypt"):
    if mode == "decrypt":
        shift = -shift
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shifted = (ord(ch) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(ch)
    return "".join(result)

def brute_force(ciphertext):
    print("\n=== BRUTE FORCE ALL 25 SHIFTS ===")
    for s in range(1, 26):
        print(f"Shift {s:2d}: {caesar(ciphertext, s, mode='decrypt')}")

def main():
    print("=== CAESAR CIPHER TOOL ===")
    while True:
        print("\n1. Encrypt text")
        print("2. Decrypt text with known key")
        print("3. Brute-force decrypt (test all shifts)")
        print("4. Exit")
        opt = input("Option (1-4): ").strip()
        if opt == "1":
            t = input("Enter plain text: ")
            s = int(input("Enter shift key (1-25): "))
            print(f"Encrypted: {caesar(t, s, 'encrypt')}")
        elif opt == "2":
            t = input("Enter encrypted text: ")
            s = int(input("Enter shift key (1-25): "))
            print(f"Decrypted: {caesar(t, s, 'decrypt')}")
        elif opt == "3":
            t = input("Enter ciphertext to crack: ")
            brute_force(t)
        elif opt == "4":
            break

if __name__ == "__main__":
    main()
