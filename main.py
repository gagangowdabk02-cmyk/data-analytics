from database import create_table
import book
import issue

def menu():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        # Add Book
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            book.add_book(title, author)

        # View Books
        elif choice == "2":
            books = book.view_books()

            print("\n--- Book List ---")

            if not books:
                print("No books found")
            else:
                for b in books:
                    print(f"ID: {b[0]} | Title: {b[1]} | Author: {b[2]}")

        # Issue Book
        elif choice == "3":
            book_id = input("Enter book ID: ")
            student = input("Enter student name: ")
            issue.issue_book(book_id, student)

        # Return Book
        elif choice == "4":
            book_id = input("Enter book ID to return: ")
            issue.return_book(book_id)

        # Exit
        elif choice == "5":
            print("Thank you for using Library System!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    create_table()
    menu()