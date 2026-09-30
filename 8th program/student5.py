import matplotlib.pyplot as plt

n = int(input("Enter number of months: "))

months = []
sales = []

for i in range(n):
    month = input("Enter month: ")
    sale = float(input("Enter sales: "))
    months.append(month)
    sales.append(sale)

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()