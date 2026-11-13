"""
Project 105: Dice Rolling Simulator & Statistics Tracker
Concepts: random module, collections.Counter, loops, text-based bar charts.
"""
import random
from collections import Counter

def roll_dice(sides, count, modifier=0):
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls) + modifier
    return rolls, total

def run_simulation(sides, num_rolls):
    print(f"\nSimulating {num_rolls} rolls of a D{sides}...")
    results = [random.randint(1, sides) for _ in range(num_rolls)]
    counts = Counter(results)
    max_count = max(counts.values()) if counts else 1
    
    print("\nFrequency Distribution:")
    for face in range(1, sides + 1):
        freq = counts[face]
        pct = (freq / num_rolls) * 100
        bar_len = int((freq / max_count) * 30)
        bar = "█" * bar_len
        print(f"Face {face:>3}: {freq:>5} ({pct:>5.1f}%) | {bar}")

def main():
    print("=" * 45)
    print("      ADVANCED DICE SIMULATOR & STATS      ")
    print("=" * 45)
    while True:
        print("\n1. Roll Custom Dice (e.g., 2d6 + 3)")
        print("2. Run Monte Carlo Dice Distribution")
        print("3. Exit")
        choice = input("Select option (1-3): ").strip()
        
        if choice == "1":
            dice_type = input("Choose die sides (4, 6, 8, 10, 12, 20, 100): ").strip()
            count_str = input("How many dice to roll: ").strip()
            mod_str = input("Modifier (+/- value, default 0): ").strip()
            
            try:
                sides = int(dice_type)
                count = int(count_str)
                mod = int(mod_str) if mod_str else 0
                if sides < 2 or count < 1:
                    print("Sides must be >= 2 and count >= 1.")
                    continue
                rolls, total = roll_dice(sides, count, mod)
                print(f"\n[DICE] Rolls: {rolls}")
                if mod != 0:
                    print(f"Modifier: {mod:+d}")
                print(f"-> Total: {total}")
            except ValueError:
                print("Invalid integer entered.")
        elif choice == "2":
            sides_str = input("Enter die sides (e.g., 6, 20): ").strip()
            rolls_str = input("Number of rolls (e.g., 1000, 10000): ").strip()
            try:
                sides = int(sides_str)
                num_rolls = int(rolls_str)
                run_simulation(sides, num_rolls)
            except ValueError:
                print("Invalid numbers.")
        elif choice == "3":
            print("May the rolls be ever in your favor!")
            break

if __name__ == "__main__":
    main()
