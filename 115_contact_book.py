"""
Project 115: Contact Book Manager
Concepts: JSON database, dictionary searching, CRUD operations, format strings.
"""
import json
import os

DB_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as f: return json.load(f)
        except Exception: return []
    return []

def save_contacts(contacts):
    with open(DB_FILE, "w") as f: json.dump(contacts, f, indent=2)

def main():
    contacts = load_contacts()
    while True:
        print("\n=== CONTACT BOOK ===")
        print("1. List All Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            if not contacts:
                print("No contacts available.")
            else:
                print(f"\n{'Name':<20} | {'Phone':<15} | {'Email'}")
                print("-" * 55)
                for c in contacts:
                    print(f"{c['name']:<20} | {c['phone']:<15} | {c.get('email', '-')}")
        elif choice == "2":
            name = input("Full Name: ").strip()
            phone = input("Phone Number: ").strip()
            email = input("Email: ").strip()
            contacts.append({"name": name, "phone": phone, "email": email})
            save_contacts(contacts)
            print("Contact saved.")
        elif choice == "3":
            q = input("Search term (name or phone): ").strip().lower()
            results = [c for c in contacts if q in c['name'].lower() or q in c['phone']]
            print(f"Found {len(results)} matches:")
            for r in results:
                print(f" • {r['name']} | {r['phone']} | {r.get('email')}")
        elif choice == "4":
            name = input("Exact name of contact to delete: ").strip().lower()
            before = len(contacts)
            contacts = [c for c in contacts if c['name'].lower() != name]
            if len(contacts) < before:
                save_contacts(contacts)
                print("Contact deleted.")
            else:
                print("No matching contact found.")
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
