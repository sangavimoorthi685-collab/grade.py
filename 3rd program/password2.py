password = input("Enter your password: ")
if len(password) >= 8:
    print("Password length is valid")
else:
    print("Password is too short")
if any(c.isupper() for c in password):
    print("Uppercase letter found")
else:
    print("Use at least one uppercase letter")
if any(c.isdigit() for c in password):
    print("Number found")
else:
    print("Use at least one number")