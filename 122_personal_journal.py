"""
Project 122: Personal Journal with Timestamps
Concepts: file append mode, datetime formatting, file reading, text search.
"""
import datetime
import os

JOURNAL_FILE = "my_journal.txt"

def add_entry():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\nWrite your journal entry below (Press ENTER when done):")
    entry = input("> ").strip()
    if entry:
        with open(JOURNAL_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{now}]\n{entry}\n{'-'*40}\n")
        print("Entry saved successfully.")

def view_entries():
    if not os.path.exists(JOURNAL_FILE):
        print("Journal is empty.")
        return
    with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
        print("\n" + f.read())

def search_journal():
    if not os.path.exists(JOURNAL_FILE):
        print("Journal is empty.")
        return
    term = input("Search keyword: ").strip().lower()
    with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    entries = content.split("-" * 40)
    matches = [e.strip() for e in entries if term in e.lower() and e.strip()]
    print(f"\nFound {len(matches)} matching entries:")
    for m in matches:
        print(m + "\n" + "-" * 40)

def main():
    while True:
        print("\n=== PERSONAL JOURNAL ===")
        print("1. New Entry")
        print("2. Read All Entries")
        print("3. Search Entries")
        print("4. Exit")
        c = input("Option (1-4): ").strip()
        if c == "1": add_entry()
        elif c == "2": view_entries()
        elif c == "3": search_journal()
        elif c == "4": break

if __name__ == "__main__":
    main()
