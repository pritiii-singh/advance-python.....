"""
Project 109: Expense Tracker
Concepts: data analysis, file handling, dictionaries, lambda sorting.
"""
import json
import os

EXPENSES_FILE = "expenses.json"

def load_data():
    if os.path.exists(EXPENSES_FILE):
        try:
            with open(EXPENSES_FILE, "r") as f: return json.load(f)
        except Exception: return []
    return []

def save_data(data):
    with open(EXPENSES_FILE, "w") as f: json.dump(data, f, indent=2)

def main():
    expenses = load_data()
    while True:
        print("\n=== PERSONAL EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category Summary & Total")
        print("4. Clear All Expenses")
        print("5. Exit")
        choice = input("Select option (1-5): ").strip()

        if choice == "1":
            title = input("Description: ").strip()
            amt = float(input("Amount ($): ").strip())
            cat = input("Category (Food, Rent, Bills, Leisure, Other): ").strip().capitalize()
            expenses.append({"title": title, "amount": amt, "category": cat or "Other"})
            save_data(expenses)
            print("Expense recorded!")
        elif choice == "2":
            if not expenses:
                print("No expenses logged.")
            else:
                print(f"\n{'#':<3} | {'Description':<20} | {'Category':<12} | {'Amount':>8}")
                print("-" * 50)
                for i, e in enumerate(expenses, 1):
                    print(f"{i:<3} | {e['title']:<20} | {e['category']:<12} | ${e['amount']:>7.2f}")
        elif choice == "3":
            if not expenses:
                print("No expenses logged.")
                continue
            cat_totals = {}
            total = 0.0
            for e in expenses:
                cat_totals[e["category"]] = cat_totals.get(e["category"], 0.0) + e["amount"]
                total += e["amount"]
            print(f"\nTotal Spent: ${total:.2f}")
            print("Breakdown by category:")
            for c, amt in sorted(cat_totals.items(), key=lambda x: x[1], reverse=True):
                pct = (amt / total) * 100
                print(f" - {c:<12}: ${amt:>7.2f} ({pct:5.1f}%)")
        elif choice == "4":
            if input("Confirm clear all? (y/n): ").lower() == 'y':
                expenses = []
                save_data(expenses)
                print("All records cleared.")
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
