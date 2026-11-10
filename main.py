from books_list import BOOKS as books
from run_app import show_menu,display_all_books,search_book_by_name_flow,add_book_flow
from run_app import boroow_book_flow,return_book_flow,get_available_books
from run_app import get_books_by_author_flow

def main():
    while True:
        choise = show_menu()
        if choise == "1":
            display_all_books(books)
        elif choise == "2":
            print(search_book_by_name_flow(books))
        elif choise == "3":
            add_book_flow(books)
        elif choise == "4":
            boroow_book_flow(books)
        elif choise == "5":
            return_book_flow(books)
        elif choise == "6":
            print(get_available_books(books))
        elif choise == "7":
            print(get_books_by_author_flow(books))
        elif choise == "8":
            break

main()



