"""
Project 111: Morse Code Translator
Concepts: two-way dictionary mapping, string join/split, character validation.
"""
MORSE_MAP = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

REVERSE_MAP = {v: k for k, v in MORSE_MAP.items()}

def text_to_morse(text):
    result = []
    for char in text.upper():
        if char in MORSE_MAP:
            result.append(MORSE_MAP[char])
    return " ".join(result)

def morse_to_text(morse):
    tokens = morse.strip().split()
    result = []
    for token in tokens:
        if token in REVERSE_MAP:
            result.append(REVERSE_MAP[token])
        else:
            result.append("?")
    return "".join(result)

def main():
    print("=== MORSE CODE TRANSLATOR ===")
    while True:
        print("\n1. Text -> Morse Code")
        print("2. Morse Code -> Text")
        print("3. Exit")
        c = input("Choice (1-3): ").strip()
        if c == "1":
            msg = input("Enter text: ")
            print(f"Morse: {text_to_morse(msg)}")
        elif c == "2":
            morse = input("Enter Morse code (space separated, '/' for word space): ")
            print(f"Decoded Text: {morse_to_text(morse)}")
        elif c == "3":
            break

if __name__ == "__main__":
    main()
