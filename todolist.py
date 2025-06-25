import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!\n")
    else:
        print("Empty task not added.\n")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed task: '{removed}'\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    print("=== TO-DO LIST APPLICATION ===")
    tasks = load_tasks()

    while True:
        print("Options:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
