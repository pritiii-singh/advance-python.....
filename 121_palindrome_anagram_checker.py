"""
Project 121: Palindrome & Anagram Verifier
Concepts: string slicing, regex text normalization, collections.Counter.
"""
import re
from collections import Counter

def is_palindrome(text):
    clean = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return clean == clean[::-1], clean

def are_anagrams(s1, s2):
    c1 = Counter(re.sub(r"[^a-zA-Z0-9]", "", s1).lower())
    c2 = Counter(re.sub(r"[^a-zA-Z0-9]", "", s2).lower())
    return c1 == c2

def main():
    print("=== PALINDROME & ANAGRAM ANALYZER ===")
    while True:
        print("\n1. Check Palindrome (e.g. 'A man a plan a canal Panama')")
        print("2. Check Anagram Pair (e.g. 'listen' and 'silent')")
        print("3. Exit")
        c = input("Choice (1-3): ").strip()

        if c == "1":
            phrase = input("Enter text: ")
            pal, clean = is_palindrome(phrase)
            if pal:
                print(f"[OK] It IS a palindrome! Normalized: '{clean}'")
            else:
                print(f"[X] Not a palindrome. Forward: '{clean}', Reverse: '{clean[::-1]}'")
        elif c == "2":
            w1 = input("Enter first word/phrase: ")
            w2 = input("Enter second word/phrase: ")
            if are_anagrams(w1, w2):
                print(f"[OK] Yes! '{w1}' and '{w2}' are anagrams!")
            else:
                print(f"[X] No, they are not anagrams.")
        elif c == "3":
            break

if __name__ == "__main__":
    main()
