from validations import check_num,check_empty

def get_book_name():
    while True:
        book_name = input("enter book name: ")
        if check_empty(book_name):
            return book_name
        print("the book name can not be empty")

def get_year():
    while True:
        year = input("enter year: ")
        if not check_empty(year):
            print("year can not be empty")
        elif not check_num(year):
            print("year must be a positive number")
        else:
            return year

def get_author():
    while True:
        author = input("enter author: ")
        if check_empty(author):
            return author
        print("must enter the author name")

def get_book_id():
    while True:
        book_id = input("enter book id: ")
        if not check_empty(book_id):
            print("must enter the book id")
        elif not check_num(book_id):
            print("id must be a positive number")
        else:
            return int(book_id)
