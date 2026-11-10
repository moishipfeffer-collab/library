def check_num(num):
    try:
        return int(num) > 0
    except ValueError:
        return False

def check_empty(input:str):
    if input.strip():
        return True
    return False


def check_book_exists(books,book):
    for b in books:
        if b["name"] == book["name"] and b["author"] == book["author"]:
            return True
    return False

def check_availability(book):
    if book["available"]:
            return True
    return False