import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print(f"✅ Added: {task}")
        elif choice == "3":
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to remove: "))
                removed = tasks.pop(index - 1)
                save_tasks(tasks)
                print(f"🗑️ Removed: {removed}")
            except (ValueError, IndexError):
                print("❌ Invalid number.")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()