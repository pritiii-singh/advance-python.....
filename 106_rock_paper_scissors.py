"""
Project 106: Rock Paper Scissors Game
Concepts: random choices, conditional logic, match score tracking.
"""
import random

OPTIONS = ["rock", "paper", "scissors"]
WIN_MAP = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def main():
    print("=== ROCK, PAPER, SCISSORS ===")
    rounds = int(input("How many rounds to play for victory? (e.g., 3): ") or 3)
    user_score = 0
    cpu_score = 0
    ties = 0

    while user_score < rounds and cpu_score < rounds:
        print(f"\nScore: You {user_score} - {cpu_score} Computer (Ties: {ties})")
        user_choice = input("Enter rock, paper, or scissors (or 'quit'): ").strip().lower()
        if user_choice == "quit":
            break
        if user_choice not in OPTIONS:
            print("Invalid move. Try again.")
            continue

        cpu_choice = random.choice(OPTIONS)
        print(f"Computer chose: {cpu_choice}")

        if user_choice == cpu_choice:
            print("[DRAW] It's a tie!")
            ties += 1
        elif WIN_MAP[user_choice] == cpu_choice:
            print(f"[SUCCESS] You win this round! {user_choice.capitalize()} beats {cpu_choice}.")
            user_score += 1
        else:
            print(f"💻 Computer wins this round! {cpu_choice.capitalize()} beats {user_choice}.")
            cpu_score += 1

    print("\n=== MATCH FINISHED ===")
    if user_score > cpu_score:
        print("[WINNER] Congratulations! You won the match!")
    elif cpu_score > user_score:
        print("[AI] Computer wins the match! Better luck next time!")
    else:
        print("Match ended early.")

if __name__ == "__main__":
    main()
