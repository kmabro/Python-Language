import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "To_Do.txt")

def show_menu():
    print("|-----------------|")
    print("|--- TO DO APP ---|")
    print("|-----------------|")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")
    
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start = 1):
            print(f"{i}. {task}")
        
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append("[ ]" + task)
    print("Task added.")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        if "[x]" not in tasks[idx]:
            tasks[idx] = tasks[idx].replace("[ ]", "[x]",1)
            print("Task marked as done.")
        else:
            print("Task is already marked done.")
    except:
        print("Invalid input.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(idx)
        print(f"Deleted: {removed}")
    except:
        print("Invalid input.")
    
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
        save_tasks(tasks)

main()
