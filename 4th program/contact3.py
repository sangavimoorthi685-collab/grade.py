tasks = []
while True:
    print("\n1. Add  2. View  3. Delete  4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")
    elif choice == "2":
        print("Tasks:", tasks)
    elif choice == "3":
        task = input("Enter task to delete: ")
        if task in tasks:
            tasks.remove(task)
            print("Task deleted")
        else:
            print("Task not found")
    elif choice == "4":
        break