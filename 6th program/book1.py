class User:
    def issue(self, book):
        print("Book issued:", book)
class Student(User):
    def issue(self, book):
        print("Student issued:", book)
class Faculty(User):
    def issue(self, book):
        print("Faculty issued:", book)
class Book:
    status = False
    def return_book(self, book):
        if Book.status:
            print(book, "returned successfully")
            Book.status = False
        else:
            print("No book to return")


book = Book()

while True:
    print("\n1. Issue Book")
    print("2. Return Book")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        user = input("Enter user type (Student/Faculty): ")
        book_name = input("Enter book name: ")

        if not Book.status:
            Book.status = True

            if user.lower() == "student":
                s = Student()
                s.issue(book_name)

            elif user.lower() == "faculty":
                f = Faculty()
                f.issue(book_name)

            else:
                print("Invalid user type")
        else:
            print("Book is already issued")
    elif choice == 2:
        book_name = input("Enter book name: ")
        book.return_book(book_name)
    elif choice == 3:
        break

    else:
        print("Invalid choice")