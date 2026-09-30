n = int(input("Number of subjects: "))
total = 0
for i in range(n):
    total = total + int(input("Enter mark: "))
average = total / n
print("Total =", total)
print("Average =", average)
if average >= 50:
    print("Grade = Pass")
else:
    print("Grade = Fail")