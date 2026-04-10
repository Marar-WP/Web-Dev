from models import TaskManager
from storage import load_tasks, save_tasks
FILENAME = "data.json"
def show_menu():
    print("\n=== Task Manager ===")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")
def show_tasks(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour tasks:")
        for task in tasks:
            print(task)
def add_task(manager):
    title = input("Enter task title: ")
    manager.add_task(title)
    print("Task added.")
def complete_task(manager):
    try:
        task_id = int(input("Enter task ID to complete: "))
        if manager.complete_task(task_id):
            print("Task completed.")
        else:
            print("Task not found.")
    except:
        print("Invalid input.")
def delete_task(manager):
    try:
        task_id = int(input("Enter task ID to delete: "))
        if manager.delete_task(task_id):
            print("Task deleted.")
        else:
            print("Task not found.")
    except:
        print("Invalid input.")
def main():
    tasks = load_tasks(FILENAME)
    manager = TaskManager(tasks)

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(manager)
        elif choice == "2":
            add_task(manager)
        elif choice == "3":
            complete_task(manager)
        elif choice == "4":
            delete_task(manager)
        elif choice == "5":
            save_tasks(FILENAME, manager.tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()