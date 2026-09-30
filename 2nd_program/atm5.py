balance = 1000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Your Balance is:", balance)
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Please collect your cash")
        else:
            print("Insufficient balance")
    elif choice == 4:
        print("Thank you for using ATM")
        break
    else:
        print("Invalid choice. Try again")