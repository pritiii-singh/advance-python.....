"""
Project 116: Daily Habit Streak Tracker
Concepts: datetime module, JSON serialization, streak logic, daily tracking.
"""
import json
import os
from datetime import date, timedelta

HABIT_FILE = "habits.json"

def load_habits():
    if os.path.exists(HABIT_FILE):
        try:
            with open(HABIT_FILE, "r") as f: return json.load(f)
        except Exception: return {}
    return {}

def save_habits(data):
    with open(HABIT_FILE, "w") as f: json.dump(data, f, indent=2)

def calculate_streak(completed_dates):
    if not completed_dates: return 0
    date_set = set(completed_dates)
    today = date.today()
    check_day = today if today.isoformat() in date_set else today - timedelta(days=1)
    
    streak = 0
    while check_day.isoformat() in date_set:
        streak += 1
        check_day -= timedelta(days=1)
    return streak

def main():
    habits = load_habits()
    today_str = date.today().isoformat()

    while True:
        print(f"\n=== HABIT TRACKER ({today_str}) ===")
        print("1. View Habits & Streaks")
        print("2. Check-in Today's Habit")
        print("3. Add New Habit")
        print("4. Exit")
        c = input("Option (1-4): ").strip()

        if c == "1":
            if not habits:
                print("No habits tracked yet.")
            else:
                print(f"{'Habit':<20} | {'Today?':<8} | {'Current Streak'}")
                print("-" * 45)
                for name, dates in habits.items():
                    is_done = "[OK]" if today_str in dates else "[X]"
                    streak = calculate_streak(dates)
                    print(f"{name:<20} | {is_done:<8} | {streak} days")
        elif c == "2":
            name = input("Enter habit name to check-in: ").strip()
            if name in habits:
                if today_str not in habits[name]:
                    habits[name].append(today_str)
                    save_habits(habits)
                    print(f"[SUCCESS] Checked in for '{name}' today!")
                else:
                    print("Already checked in today!")
            else:
                print("Habit not found.")
        elif c == "3":
            name = input("Enter new habit name: ").strip()
            if name and name not in habits:
                habits[name] = []
                save_habits(habits)
                print(f"Habit '{name}' created!")
        elif c == "4":
            break

if __name__ == "__main__":
    main()
