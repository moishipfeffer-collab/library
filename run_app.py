from inputs import get_book_name,get_year,get_author,get_book_id
from books import add_book,boroow_book,return_book,get_books_by_author
from books import search_book_by_name
def show_menu():
    print("=============================")
    print("     LIBRARY MANAGEMENT")
    print("=============================")
    while True:
        chise = input("1. Display all books\n2. Search book by name\n" \
        "3. Add new book\n4. Borrow a book\n5. Return a book\n" \
        "6. Display available books\n7. Display books by author\n" \
        "8. Exit\n\nChoose an option: ")
        if chise in ["1","2","3","4","5","6","7","8"]:
            return chise
        print("not valid chise\n")

# option 1 show all books

def display_all_books(books):
    for book in books:
        print(book)

# option 2 search by name 

def search_book_by_name_flow(books):
    name = get_book_name()
    book = search_book_by_name(books,name)
    if book:
        return book
    return "the book is not found in the library"

# option 3 add book

def add_book_flow(books):
    name = get_book_name()
    author = get_author()
    year = get_year()
    if add_book(books,name,author,year):
        print("book added successully")
    

# option 4 borrow book

def boroow_book_flow(books):
    book_id = get_book_id()
    if not boroow_book(books,book_id):
        print("the book is not available")
    else:
        print("the book borrowd successfully")

# option 5 return book 

def return_book_flow(books):
    book_id = get_book_id()
    if not return_book(books,book_id):
        print("the book is already available")
    else:
        print("the book is returnd successfully")

# option 6 get available books

def get_available_books(books):
    available_books = []
    for book in books:
        if book["available"] == True:
            available_books.append(book)
    return available_books

# option 7 get book by author 

def get_books_by_author_flow(books):
    author = get_author()
    auther_books = get_books_by_author(books,author)
    if auther_books:
        return auther_books
    return "no books found"
