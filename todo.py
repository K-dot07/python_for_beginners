# Simple To-Do List App

tasks = []  # Empty list to store tasks

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        print("\nYour Tasks:")
        for i, t in enumerate(tasks,1):
            print(f"{i}. {t}")
    elif choice == '3':
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task removed!")
        else:
            print("Invalid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
