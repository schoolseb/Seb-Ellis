class Book:
    def __init__(self, tags):
        self.tags = tags

    def __str__(self):
        return f"{self.tags}"


Romeo = Book("Romeo")
print(Romeo)
collection = []
book1 = {
    "tile": "The way of Kings.",
    "author": "Brandon",
    "genre": "Fantasy",
    "isbn": "2854",
    "tags": ["tragedy", "long", "horror"]
}
book2 = {
    "tile": "Romeo and Juliette.",
    "author": "William",
    "genre": "Romance",
    "isbn": "1234",
    "tags": ["tragedy", "romance", "play"]
}
collection.append(book1)
collection.append(book2)
print(book1["tags"])
input("pick")
tags_horror = {"horror", "play"}


#print(book1["tags"].issubset(tags_horror))
# other_book = ["the way of kings",
#               "Brandon Sanderson",
#               "Fantasy",
#               "2854",
#               ["tragedy", "long", "horror"]]
# other_isbn = "2853"
# print(other_book[3] == other_isbn)

def get_book(books, isbn):
    for book in books:
        if book["isbn"] == isbn:
            return book
    return None


#isbn_confict take prameter already in then return true or false
def add_book(collection, title, author, genre, isbn, tags):
    if get_book(collection, isbn):
        print("can't add book")
        return
    book = {
        "tile": title,
        "author": author,
        "genre": genre,
        "isbn": isbn,
        "tags": tags
    }
    collection.append(book)


if get_book(collection, "1234"):
    print("ISBN already taken")
else:
    print("ISBN is free")

# add set for books
set1 = ["tragedy", "long", "horror"]
set2 = ["tragedy", "romance", "horror"]
set3 = ["tragedy"]


def books_with_tags(collection, tags, book_with_tags=None):
    books = []
    for books in collection:
        if set(books["tags"]).issubset(tags_horror):
            print("books are visible")
    else:
        print("books are not visible")

    if book_with_tags:
        books.append(books)

    return tags


#print  books_with_tags()

def add(book, tags):
    return book + tags



assert add(4, 5) == book2, "add() failed"

try:

    assert add(4,5) == book1, "add() failed"
except AssertionError as e:

    print(f"Caught an error: {e}")
    print("program moves with running")
    print("program good")
