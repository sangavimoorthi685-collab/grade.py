employees = {}
while True:
    print("\n1. Add  2. Search  3. Delete  4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Employee name: ")
        salary = input("Salary: ")
        employees[name] = salary
        print("Employee added")
    elif choice == "2":
        name = input("Search name: ")
        print("Salary:", employees.get(name, "Not found"))
    elif choice == "3":
        name = input("Delete name: ")
        employees.pop(name, None)
        print("Employee deleted")

    elif choice == "4":
        break