"""
Project 104: Command-Line To-Do List
Concepts: file I/O, json serialization, lists of dictionaries, CRUD operations.
"""
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty! [SUCCESS]")
        return
    print("\n" + "-" * 55)
    print(f"{'#':<3} | {'Status':<10} | {'Priority':<8} | {'Task Description'}")
    print("-" * 55)
    for i, t in enumerate(tasks, 1):
        status = "[x] Done" if t.get("done") else "[ ] Pending"
        prio = t.get("priority", "Medium")
        print(f"{i:<3} | {status:<10} | {prio:<8} | {t.get('title')}")
    print("-" * 55)

def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO LIST MANAGER ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter option (1-5): ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ").strip()
            if not title:
                print("Task cannot be empty.")
                continue
            prio = input("Priority (Low / Medium / High) [Medium]: ").strip().capitalize()
            if prio not in ["Low", "Medium", "High"]:
                prio = "Medium"
            tasks.append({"title": title, "priority": prio, "done": False})
            save_tasks(tasks)
            print("Task added successfully.")
        elif choice == "3":
            show_tasks(tasks)
            idx_str = input("Enter task # to mark complete: ").strip()
            if idx_str.isdigit() and 1 <= int(idx_str) <= len(tasks):
                tasks[int(idx_str) - 1]["done"] = True
                save_tasks(tasks)
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        elif choice == "4":
            show_tasks(tasks)
            idx_str = input("Enter task # to delete: ").strip()
            if idx_str.isdigit() and 1 <= int(idx_str) <= len(tasks):
                removed = tasks.pop(int(idx_str) - 1)
                save_tasks(tasks)
                print(f"Removed: {removed['title']}")
            else:
                print("Invalid task number.")
        elif choice == "5":
            print("Saved tasks. Have a productive day!")
            break

if __name__ == "__main__":
    main()
