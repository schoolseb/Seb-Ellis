## Create initial and individual variables
Book1 = {"Title": "Comedy show", "Tags": ["Comedy"]}
Book2 = {"Title": "Horror show", "Tags": ["horror"]}

## Put your variables together in the same object (using a list or tuple)
Collection = [Book1, Book2]

# Be sure that you can access the properties of your Dictionary objects
print(Book1["Tags"])
print(Book2["Tags"])
print(Collection[0])

## Create a Tag set that you want to evaluate (using sets for efficient comparison)
Tags_horror_books = {"horror", "Gore", "Mystery", "Dark"}
Tags_comedy_books = {"comedy", "jokes", "funny"}

## Try to get a True or False output
# Note: Added .lower() to handle case sensitivity
print(set(tag.lower() for tag in Book1["Tags"]).issubset(Tags_horror_books))
print(set(tag.lower() for tag in Book1["Tags"]).issubset(Tags_comedy_books))

## Apply this in a Conditional Statement
if set(tag.lower() for tag in Book1["Tags"]).issubset(Tags_horror_books):
    print("Yes, this is a horror movie")
else:
    print("No, this is NOT a horror movie")

## Apply this in a Conditional Statement
if set(tag.lower() for tag in Book1["Tags"]).issubset(Tags_comedy_books):
    print("Yes, this is a comedy movie")
else:
    print("No, this is NOT a comedy movie")

## Now implement this with a for loop that goes in each element of the Collection
print("\n--- Looping through Collection ---")
for book in Collection:
    # Normalize tags to lowercase for comparison
    book_tags = set(tag.lower() for tag in book["Tags"])

    if book_tags.issubset(Tags_horror_books):
        print(f"'{book['Title']}' is a horror movie")
    elif book_tags.issubset(Tags_comedy_books):
        print(f"'{book['Title']}' is a comedy movie")
    else:
        print(f"I do not know what '{book['Title']}' is about")

# Create a function that does all you evaluate above
def Check_Movie_Genre(Collection):
    print("\n--- Function Output ---")
    for book in Collection:
        book_tags = set(tag.lower() for tag in book["Tags"])

        if book_tags.issubset(Tags_horror_books):
            print(f"'{book['Title']}' is a horror movie")
        elif book_tags.issubset(Tags_comedy_books):
            print(f"'{book['Title']}' is a comedy movie")
        else:
            print(f"I do not know what '{book['Title']}' is about")

# Apply this function to your initial variables
Check_Movie_Genre(Collection)
