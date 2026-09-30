import matplotlib.pyplot as plt
n = int(input("Enter number of students: "))
students = []
marks = []
for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter mark: "))
    students.append(name)
    marks.append(mark)
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()