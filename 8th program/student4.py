import matplotlib.pyplot as plt

n = int(input("Enter number of subjects: "))

subjects = []
marks = []

for i in range(n):
    subject = input("Enter subject name: ")
    mark = float(input("Enter mark: "))
    subjects.append(subject)
    marks.append(mark)

plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Subject Marks Distribution")

plt.show()