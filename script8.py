def add_book(collection, title, author, genre, isbn, tags):
    """Try to see if isbn is in or not"""
    isbn = any(book["isbn"] == isbn for book in collection)

    if isbn:
        print("")