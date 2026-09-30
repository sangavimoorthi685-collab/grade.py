balance = 5000
print("1. Balance")
print("2. Deposit")
print("3. Withdraw")
choice = int(input("Enter choice: "))
if choice == 1:
    print("Balance =", balance)
elif choice == 2:
    amount = int(input("Enter amount: "))
    balance = balance + amount
    print("Balance =", balance)
elif choice == 3:
    amount = int(input("Enter amount: "))
    if amount <= balance:
        balance = balance - amount
        print("Balance =", balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid choice")