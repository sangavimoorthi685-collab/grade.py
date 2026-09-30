class Account:
    def deposit(self, amount):
        print("Amount deposited:", amount)
class Savings(Account):
    def deposit(self, amount):
        print("Savings account deposit:", amount)
class Current(Account):
    def deposit(self, amount):
        print("Current account deposit:", amount)
account = input("Enter account type (Savings/Current): ")
amount = int(input("Enter amount: "))
if account.lower() == "savings":
    s = Savings()
    s.deposit(amount)
elif account.lower() == "current":
    c = Current()
    c.deposit(amount)
else:
    print("Invalid account type")