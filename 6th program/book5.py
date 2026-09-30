class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog says Bow Bow")
class Cat(Animal):
    def sound(self):
        print("Cat says Meow")
animal = input("Enter animal (Dog/Cat): ")
if animal.lower() == "dog":
    d = Dog()
    d.sound()
elif animal.lower() == "cat":
    c = Cat()
    c.sound()
else:
    print("Invalid animal")