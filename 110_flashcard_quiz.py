"""
Project 110: Interactive Flashcard Quiz Maker
Concepts: dictionaries, loop iteration, random sampling, score calculation.
"""
import random

DEFAULT_CARDS = [
    {"q": "What is the keyword to define a function in Python?", "a": "def"},
    {"q": "What data type is an ordered and immutable collection?", "a": "tuple"},
    {"q": "Which built-in function returns the length of an object?", "a": "len"},
    {"q": "What symbol starts a single-line comment in Python?", "a": "#"},
    {"q": "What method adds an element to the end of a list?", "a": "append"}
]

def main():
    deck = list(DEFAULT_CARDS)
    print("=== FLASHCARD QUIZ MAKER ===")
    while True:
        print("\n1. Start Quiz Session")
        print("2. Add Custom Card")
        print("3. View Deck")
        print("4. Exit")
        choice = input("Option (1-4): ").strip()

        if choice == "1":
            if not deck:
                print("Deck is empty!")
                continue
            random.shuffle(deck)
            score = 0
            for i, card in enumerate(deck, 1):
                print(f"\nCard {i}/{len(deck)}: {card['q']}")
                user_ans = input("Your answer: ").strip().lower()
                if user_ans == card["a"].lower():
                    print("[OK] Correct!")
                    score += 1
                else:
                    print(f"[X] Incorrect. The answer is: {card['a']}")
            print(f"\nQuiz complete! Final Score: {score}/{len(deck)} ({(score/len(deck))*100:.1f}%)")
        elif choice == "2":
            q = input("Question: ").strip()
            a = input("Answer: ").strip()
            if q and a:
                deck.append({"q": q, "a": a})
                print("Card added.")
        elif choice == "3":
            for i, c in enumerate(deck, 1):
                print(f"{i}. Q: {c['q']} | A: {c['a']}")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
