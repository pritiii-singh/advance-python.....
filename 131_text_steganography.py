"""
Project 131: Zero-Width Text Steganography
Concepts: bit manipulation, unicode characters, binary encoding/decoding.
"""
# Using zero-width space and zero-width non-joiner
ZW_ZERO = '\u200b'
ZW_ONE = '\u200c'

def encode_hidden_message(cover_text, secret_text):
    # Convert secret text into binary string
    binary = "".join(f"{ord(c):08b}" for c in secret_text)
    hidden_payload = "".join(ZW_ONE if bit == '1' else ZW_ZERO for bit in binary)
    # Inject hidden payload after first character of cover text
    return cover_text[:1] + hidden_payload + cover_text[1:]

def decode_hidden_message(stego_text):
    bits = []
    for ch in stego_text:
        if ch == ZW_ZERO:
            bits.append('0')
        elif ch == ZW_ONE:
            bits.append('1')
    bit_str = "".join(bits)
    if not bit_str or len(bit_str) % 8 != 0:
        return "No valid secret message found."
    
    chars = [chr(int(bit_str[i:i+8], 2)) for i in range(0, len(bit_str), 8)]
    return "".join(chars)

def main():
    print("=== ZERO-WIDTH STEGANOGRAPHY ===")
    while True:
        print("\n1. Hide secret text in cover message")
        print("2. Extract secret text from stego message")
        print("3. Exit")
        c = input("Choice (1-3): ").strip()
        if c == "1":
            cover = input("Enter innocent cover sentence: ")
            secret = input("Enter secret message to hide: ")
            stego = encode_hidden_message(cover, secret)
            print(f"\nStego message (looks completely normal):\n{stego}")
            print(f"Length visibly looks like: {len(cover)} chars (actual: {len(stego)} chars)")
        elif c == "2":
            stego = input("Paste stego text: ")
            extracted = decode_hidden_message(stego)
            print(f"[SECRET] Extracted Secret: {extracted}")
        elif c == "3":
            break

if __name__ == "__main__":
    main()
