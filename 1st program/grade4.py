n = int(input("Enter number of subjects: "))
total = 0
for i in range(n):
    mark = float(input("Enter mark: "))
    total += mark
    if mark >= 90:
        print("Grade: A")
    elif mark >= 80:
        print("Grade: B")
    elif mark >= 70:
        print("Grade: C")
    elif mark >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
average = total / n
print("Total:", total)
print("Average:", average)