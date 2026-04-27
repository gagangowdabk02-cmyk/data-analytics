import sqlite3

def connect():
    return sqlite3.connect("library.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    # Books table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT
        )
    """)

    # Issued books table (THIS WAS MISSING OR NOT CREATED PROPERLY)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS issued_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            student TEXT
        )
    """)

    conn.commit()
    conn.close()
    