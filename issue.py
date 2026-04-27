from database import connect

def issue_book(book_id, student):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO issued_books (book_id, student) VALUES (?, ?)",
        (book_id, student)
    )

    conn.commit()
    conn.close()

    print("Book issued successfully!")


def return_book(book_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM issued_books WHERE book_id = ?",
        (book_id,)
    )

    conn.commit()
    conn.close()

    print("Book returned successfully!")