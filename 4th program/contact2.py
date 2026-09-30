students = {}
while True:
    print("\n1. Add  2. Search  3. Delete  4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Student name: ")
        mark = input("Mark: ")
        students[name] = mark
        print("Student added")
    elif choice == "2":
        name = input("Search name: ")
        print("Mark:", students.get(name, "Not found"))
    elif choice == "3":
        name = input("Delete name: ")
        students.pop(name, None)
        print("Student deleted")
    elif choice == "4":
        break