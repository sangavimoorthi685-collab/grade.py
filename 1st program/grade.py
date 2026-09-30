marks = []
n = int(input("Enter number of subjects: "))
for i in range(n):
    mark = float(input("Enter mark: "))
    marks.append(mark)
total = sum(marks)
average = total / n
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
print("Total:", total)
print("Average:", average)
print("Grade:", grade)