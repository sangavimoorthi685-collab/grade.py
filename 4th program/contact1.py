contacts = {}
while True:
    print("\n1. Add  2. Search  3. Delete  4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        with open("contacts.txt", "w") as f:
            for n, p in contacts.items():
                f.write(n + "," + p + "\n")
        print("Contact added")
    elif choice == "2":
        name = input("Search name: ")
        print("Phone:", contacts.get(name, "Not found"))
    elif choice == "3":
        name = input("Delete name: ")
        contacts.pop(name, None)
        print("Contact deleted")
    elif choice == "4":
        break