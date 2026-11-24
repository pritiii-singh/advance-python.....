"""
Project 125: Roman Numeral Converter
Concepts: greedy algorithms, ordered mappings, validation logic.
"""
ROMAN_TO_INT = {
    'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
    'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
    'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
}

INT_TO_ROMAN = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]

def to_roman(num):
    if not (1 <= num <= 3999):
        return "Error: Number must be between 1 and 3999"
    result = []
    for val, sym in INT_TO_ROMAN:
        while num >= val:
            result.append(sym)
            num -= val
    return "".join(result)

def from_roman(s):
    s = s.upper().strip()
    total = 0
    i = 0
    single_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    while i < len(s):
        if i + 1 < len(s) and single_map.get(s[i], 0) < single_map.get(s[i+1], 0):
            total += single_map.get(s[i+1], 0) - single_map.get(s[i], 0)
            i += 2
        else:
            total += single_map.get(s[i], 0)
            i += 1
    return total

def main():
    print("=== ROMAN NUMERAL CONVERTER ===")
    while True:
        print("\n1. Integer to Roman (1 - 3999)")
        print("2. Roman to Integer")
        print("3. Exit")
        c = input("Choice (1-3): ").strip()
        if c == "1":
            n = int(input("Enter integer: "))
            print(f"Roman Numeral: {to_roman(n)}")
        elif c == "2":
            r = input("Enter Roman numeral: ")
            print(f"Integer: {from_roman(r)}")
        elif c == "3":
            break

if __name__ == "__main__":
    main()
