tasks = []

while True:
    print("\n1. Create Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("\nTask Created!")
        
    elif choice == '2':
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == '3':
        if not tasks:
            print("Task Not Created.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                num = int(input("Enter task number to update: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1] = input("Enter updated task: ")
                    print("Task updated!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Exit")
        break