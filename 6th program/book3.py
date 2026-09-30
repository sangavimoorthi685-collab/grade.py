class Employee:
    def salary(self, amount):
        print("Employee salary:", amount)
class Manager(Employee):
    def salary(self, amount):
        print("Manager salary:", amount)
class Developer(Employee):
    def salary(self, amount):
        print("Developer salary:", amount)
job = input("Enter job (Manager/Developer): ")
amount = int(input("Enter salary: "))
if job.lower() == "manager":
    m = Manager()
    m.salary(amount)
elif job.lower() == "developer":
    d = Developer()
    d.salary(amount)
else:
    print("Invalid job")