#from .exceptions import BookAlreadyBorrowedError, BookNotFoundError

#class User:
#    def __init__(self, username):
#        self.username = username
#        self.borrowed_books = []

#    def borrow_book(self, book):
#        if book.isbn not in [b.isbn for b in self.borrowed_books]:
#            self.borrowed_books.append(book)
#        else:
#            raise BookAlreadyBorrowedError()

#    def return_book(self, isbn):
#        book_to_return = next((book for book in self.borrowed_books if book.isbn == isbn), None)
#        if book_to_return:
#            self.borrowed_books.remove(book_to_return)
#        else:
#            raise BookNotFoundError("Book not found in user's borrowed books")

from .exceptions import BookAlreadyBorrowedError, BookNotFoundError

class User:
    def __init__(self, username):
        self.username = username
        self.borrowed_books_isbns = []  # Store ISBNs instead of Book instances

    def borrow_book(self, isbn):
        if isbn not in self.borrowed_books_isbns:
            self.borrowed_books_isbns.append(isbn)
        else:
            raise BookAlreadyBorrowedError()

    def return_book(self, isbn):
        if isbn in self.borrowed_books_isbns:
            self.borrowed_books_isbns.remove(isbn)
        else:
            raise BookNotFoundError("Book not found in user's borrowed books")
