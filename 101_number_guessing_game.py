"""
Project 101: Number Guessing Game
Concepts: random module, while loops, conditional branching (if/elif/else), input validation.
"""
import random

def get_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy (1 to 50, 10 attempts)")
    print("2. Medium (1 to 100, 7 attempts)")
    print("3. Hard (1 to 500, 8 attempts)")
    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 500, 8
        print("Invalid choice. Please enter 1, 2, or 3.")

def play_round():
    max_num, attempts_left = get_difficulty()
    secret_number = random.randint(1, max_num)
    print(f"\nI have chosen a number between 1 and {max_num}. Can you guess it?")
    
    attempts_used = 0
    while attempts_left > 0:
        print(f"\nAttempts remaining: {attempts_left}")
        guess_str = input("Your guess: ").strip()
        if not guess_str.isdigit():
            print("Please enter a valid positive number.")
            continue
        
        guess = int(guess_str)
        attempts_used += 1
        attempts_left -= 1
        
        if guess == secret_number:
            print(f"[SUCCESS] Correct! You guessed {secret_number} in {attempts_used} attempts!")
            return True
        elif guess < secret_number:
            diff = secret_number - guess
            hint = "Very close!" if diff <= 5 else "Too low!"
            print(f"[LOW] {hint}")
        else:
            diff = guess - secret_number
            hint = "Very close!" if diff <= 5 else "Too high!"
            print(f"[HIGH] {hint}")
            
    print(f"\n[BOOM] Game Over! The secret number was {secret_number}.")
    return False

def main():
    print("=" * 45)
    print("      WELCOME TO NUMBER GUESSING GAME      ")
    print("=" * 45)
    wins = 0
    games = 0
    
    while True:
        games += 1
        if play_round():
            wins += 1
        print(f"\nScore: {wins} wins / {games} games played.")
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
