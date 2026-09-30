import string
password = input("Enter your password: ")
if (len(password) >= 8 and
    any(c.isupper() for c in password) and
    any(c.islower() for c in password) and
    any(c.isdigit() for c in password) and
    any(c in string.punctuation for c in password)):
    print("Password is strong")
    encrypted = ""
    for c in password:
        encrypted += chr(ord(c) + 3)
    print("Encrypted password:", encrypted)
    with open("password.txt", "w") as file:
        file.write(encrypted)
    print("Encrypted password saved successfully")
else:
    print("Password is weak")
    print("Use 8 characters with uppercase, lowercase, number and special character")