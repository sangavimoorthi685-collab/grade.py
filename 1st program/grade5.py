n = int(input("Enter number of subjects: "))
total = 0
for i in range(1, n + 1):
    mark = float(input(f"Enter marks for subject {i}: "))
    total += mark
average = total / n
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"
print("\n---Result---")
print("Total Marks =", total)
print("Average =", average)
print("Grade =", grade)