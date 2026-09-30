balance = 10000
while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Your balance is", balance)
    elif choice == "2":
        deposit = int(input("Enter amount: "))
        balance += deposit
        print("New balance =", balance)
    elif choice == "3":
        withdraw = int(input("Enter amount: "))
        if withdraw <= balance:
            balance -= withdraw
            print("New balance =", balance)
        else:
            print("Insufficient balance")
    elif choice == "4":
        print("Thank you for using ATM")
        break
    else:
        print("Invalid choice")