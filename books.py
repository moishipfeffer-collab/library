from validations import check_book_exists,check_availability

def get_next_book_id(books):
    return len(books) + 1

def  add_book(books:list,name,author,year):
    book_id = get_next_book_id(books)
    new_book = {"id":book_id, "name":name,"author":author,
    "year":year,"available": True}
    if not check_book_exists(books,new_book):
        books.append(new_book)
        return True
    print("book already exists")

def boroow_book(books,book_id):
    for book in books:
        if book["id"] == book_id:
            if check_availability(book):
                book["available"] = False
                return True
    return False

def return_book(books,book_id):
    for book in books:
        if book_id == book["id"]:
            if check_availability(book):
                return False
            book["available"] = True
    return True

def get_books_by_author(books, author):
    books_by_author = []
    for book in books:
        if book["author"] == author:
            books_by_author.append(book)
    return books_by_author

def search_book_by_name(books,name):
    books_found = []
    for book in books:
        if name in book["name"]:
            books_found.append(book)
    if books_found:
        return books_found
    return None

