#Seb Ellis 2/22/2025 Books
def add_book(collection, title, author, genre, isbn, tags):

    """Try to see if isbn is in or not"""
    isbn_conflict = any(book["isbn"]
                == isbn for book in collection)

    if isbn_conflict:
        print("ISBN already taken")
        return collection

#add dict to code
    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "isbn": isbn,
        "tags": set(tags)

}

    collection.append(book)
    return collection

def books_with_tags(collection, tags):
    books = []
    for book in collection:
        """subset"""
        if tags.issubset(book["tags"]):
            books.append(book)
    return books

def get_book(collection, isbn):
    for book in collection:
        if book["isbn"] == isbn:
            return book["title"], book["author"]
    return ()

#set of book info
library = []
add_book(library,  "The Way of Kings", "Brandon Sand", "Fantasy", "97807", {"epic", "long", "trauma"})

"""Test getbook"""
assert get_book(library, "97807") == ("The Way of Kings", "Brandon Sand"), "get_book failed"

#Books tag test
results = books_with_tags(library, {"epic", "trauma"})
assert len(results) == 1,"Tag search failed"
assert results[0]["title"] == "The Way of Kings"

library = []

library = add_book(library, "The Way of Kings", "Brandon Sand", "Fantasy","97807",{"epic", "long", "trauma"})
print("current library", library)

"""time to search for tags"""

search_tags ={"epic" , "trauma"}
matching_books = books_with_tags(library, search_tags)

print(f"\nBooks with tags {search_tags}:")
for book in matching_books:
    print(f"- {book['title']} by {book['author']}")


    #let's find a couple tags

isbn_to_find = "97807"
book_info = get_book(library, isbn_to_find)

if book_info:
    print(f"\nFound Book: {book_info[0]}(Author: {book_info[1]}")
else:
    print("\nBook not found.")
if issubclass:
    print("book is here")

