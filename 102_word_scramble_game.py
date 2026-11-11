"""
Project 102: Word Scramble Game
Concepts: strings, lists, random.shuffle, dictionaries, scoring systems.
"""
import random

WORD_BANK = {
    "Programming": ["python", "variable", "function", "algorithm", "compiler", "database"],
    "Animals": ["elephant", "kangaroo", "dolphin", "chameleon", "cheetah", "penguin"],
    "Science": ["gravity", "molecule", "electron", "telescope", "ecosystem", "quantum"],
    "Countries": ["canada", "brazil", "germany", "japan", "australia", "egypt"]
}

def scramble_word(word):
    letters = list(word)
    if len(letters) <= 1:
        return word
    while True:
        random.shuffle(letters)
        scrambled = "".join(letters)
        if scrambled != word:
            return scrambled

def main():
    print("=" * 45)
    print("        WELCOME TO WORD SCRAMBLE           ")
    print("=" * 45)
    
    score = 0
    streak = 0
    
    categories = list(WORD_BANK.keys())
    for idx, cat in enumerate(categories, 1):
        print(f"{idx}. {cat}")
    
    cat_choice = input("\nPick a category (1-4) or press Enter for All: ").strip()
    if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
        selected_cat = categories[int(cat_choice) - 1]
        words_pool = [(selected_cat, w) for w in WORD_BANK[selected_cat]]
    else:
        words_pool = [(cat, w) for cat, lst in WORD_BANK.items() for w in lst]
        
    random.shuffle(words_pool)
    
    for cat, original in words_pool:
        scrambled = scramble_word(original)
        print(f"\n[Category: {cat}] Scrambled Word: {scrambled.upper()}")
        print("Type 'hint' for a clue, or 'skip' to move to next.")
        
        hint_used = False
        while True:
            user_input = input("Your answer: ").strip().lower()
            if user_input == "skip":
                print(f"Skipped! The word was: {original.upper()}")
                streak = 0
                break
            elif user_input == "hint":
                if not hint_used:
                    print(f"[HINT] Clue: Starts with '{original[0].upper()}' and ends with '{original[-1].upper()}'. Length: {len(original)}")
                    hint_used = True
                else:
                    print("No more hints available for this word!")
            elif user_input == original:
                points = 5 if hint_used else 10
                score += points
                streak += 1
                print(f"[OK] Correct! +{points} pts (Streak: {streak})")
                break
            else:
                print("[X] Not quite. Try again!")
                
    print(f"\nGame Finished! Final Score: {score}")

if __name__ == "__main__":
    main()
