text = input("Enter your message: ")
encrypted = ""
for c in text:
    encrypted += chr(ord(c) + 3)
print("Original message:", text)
print("Encrypted message:", encrypted)