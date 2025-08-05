# todo.py

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!\n")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        print("To-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks, filename)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks, filename)
        elif choice == '4':
            save_tasks(tasks, filename)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again!\n")

if __name__ == '__main__':
    main()
