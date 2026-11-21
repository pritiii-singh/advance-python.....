"""
Project 119: Console Hangman Game
Concepts: string indexing, set operations, ASCII art stages, game state loops.
"""
import random

STAGES = [
    r"""
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    r"""
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    r"""
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    r"""
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    r"""
       ------
       |    |
       O    |
      /|\   |
            |
            |
    =========
    """,
    r"""
       ------
       |    |
       O    |
      /|\   |
      /     |
            |
    =========
    """,
    r"""
       ------
       |    |
       O    |
      /|\   |
      / \   |
            |
    =========
    """
]

WORDS = ["PYTHON", "ALGORITHM", "VARIABLE", "FUNCTION", "ITERATOR", "DEVELOPER"]

def main():
    secret = random.choice(WORDS)
    guessed = set()
    errors = 0
    max_errors = len(STAGES) - 1

    print("=== WELCOME TO HANGMAN ===")

    while errors < max_errors:
        print(STAGES[errors])
        display = [ch if ch in guessed else "_" for ch in secret]
        print("Word: " + " ".join(display))
        print(f"Guessed: {', '.join(sorted(guessed))}")

        if "_" not in display:
            print("\n[SUCCESS] Congratulations! You guessed the word correctly!")
            return

        guess = input("Guess a letter: ").strip().upper()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed:
            print("You already guessed that letter!")
            continue

        guessed.add(guess)
        if guess not in secret:
            errors += 1
            print(f"[X] Miss! {max_errors - errors} lives remaining.")

    print(STAGES[errors])
    print(f"[GAME OVER] Game Over! The word was {secret}.")

if __name__ == "__main__":
    main()
