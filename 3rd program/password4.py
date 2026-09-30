name = input("Enter your name: ")
message = input("Enter your message: ")
with open("message.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Message: " + message)
print("Message saved successfully")