class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def start(self):
        print("Car started")
class Bike(Vehicle):
    def start(self):
        print("Bike started")
vehicle = input("Enter vehicle (Car/Bike): ")
if vehicle.lower() == "car":
    c = Car()
    c.start()
elif vehicle.lower() == "bike":
    b = Bike()
    b.start()
else:
    print("Invalid vehicle")