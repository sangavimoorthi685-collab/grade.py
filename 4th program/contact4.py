items = []
while True:
    print("\n1. Add  2. View  3. Delete  4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        item = input("Enter item: ")
        items.append(item)
        print("Item added")
    elif choice == "2":
        print("Items:", items)
    elif choice == "3":
        item = input("Delete item: ")
        if item in items:
            items.remove(item)
            print("Item deleted")
        else:
            print("Item not found")
    elif choice == "4":
        break