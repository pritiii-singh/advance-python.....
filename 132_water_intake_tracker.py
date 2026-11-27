"""
Project 132: Daily Water Intake Tracker
Concepts: numerical limits, terminal progress bar, simple logs, health goals.
"""
import datetime

def main():
    target_glasses = 8
    consumed = 0
    log = []

    print("=== DAILY WATER INTAKE TRACKER ===")
    print(f"Daily recommended goal: {target_glasses} glasses (approx 2 Liters)\n")

    while True:
        pct = min(100, int((consumed / target_glasses) * 100))
        bar = "█" * (pct // 5) + "-" * (20 - (pct // 5))
        print(f"Progress: [{bar}] {consumed}/{target_glasses} glasses ({pct}%)")

        print("\nOptions: (1) Drink 1 glass (2) Drink custom glasses (3) View Log (4) Exit")
        c = input("Action: ").strip()
        if c == "1":
            consumed += 1
            log.append(f"{datetime.datetime.now().strftime('%H:%M')} - 1 glass")
            print("💧 Great! Stay hydrated!")
        elif c == "2":
            amt = int(input("How many glasses: ") or 1)
            consumed += amt
            log.append(f"{datetime.datetime.now().strftime('%H:%M')} - {amt} glasses")
        elif c == "3":
            print("\n--- Intake Log ---")
            for entry in log: print(f" • {entry}")
            print("------------------")
        elif c == "4":
            break

if __name__ == "__main__":
    main()
