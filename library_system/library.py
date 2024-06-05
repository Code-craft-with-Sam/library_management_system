import json
import os
from models import Book
from .user import User
from .exceptions import (
    BookNotFoundError, 
    BookNotAvailableError, 
    UserNotFoundError, 
    BookAlreadyBorrowedError,
    BookAlreadyExistsError
)

class Library:
    def __init__(self, db):
        self.db = db
        self.users = {}
        self.genres = set()
        self.borrowed_books = {}

    def add_book(self, book):
        # Check if a book with the same ISBN already exists
        existing_book = Book.query.filter_by(isbn=book.isbn).first()
        if existing_book:
            raise BookAlreadyExistsError(f"Book with ISBN {book.isbn} already exists.")
        
        self.db.session.add(book)
        self.db.session.commit()
        self.genres.add(book.genre)

    def remove_book(self, isbn):
        book_to_remove = Book.query.filter_by(isbn=isbn).first()
        if book_to_remove:
            self.db.session.delete(book_to_remove)
            self.db.session.commit()
            if book_to_remove.genre not in [b.genre for b in Book.query.all()]:
                self.genres.remove(book_to_remove.genre)
        else:
            raise BookNotFoundError()

    def borrow_book(self, isbn, username):
        book_to_borrow = Book.query.filter_by(isbn=isbn).first()
        if book_to_borrow and book_to_borrow.available:
            if username not in self.users:
                self.users[username] = User(username)
            user = self.users[username]
            user.borrow_book(isbn)
            book_to_borrow.available = False
            self.db.session.add(book_to_borrow)
            self.db.session.commit()
            self.borrowed_books[isbn] = username
        elif not book_to_borrow:
            raise BookNotFoundError()
        else:
            raise BookNotAvailableError()

    def return_book(self, isbn, username):
        book_to_return = Book.query.filter_by(isbn=isbn).first()
        if book_to_return and not book_to_return.available:
            if username in self.users:
                user = self.users[username]
                user.return_book(isbn)
                book_to_return.available = True
                self.db.session.add(book_to_return)
                self.db.session.commit()
                del self.borrowed_books[isbn]
            else:
                raise UserNotFoundError()
        elif not book_to_return:
            raise BookNotFoundError()
        else:
            raise BookAlreadyBorrowedError("Book was not borrowed")

    def view_books(self):
        return Book.query.all()

    def view_genres(self):
        return {book.genre for book in Book.query.all()}

    def save_to_file(self, filename):
        data = {
            "books": [book.to_dict() for book in Book.query.all()],
            "users": {username: user.borrowed_books for username, user in self.users.items()},
            "genres": list(self.genres),
            "borrowed_books": self.borrowed_books
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                for book_data in data["books"]:
                    book = Book.from_dict(book_data)
                    self.db.session.add(book)
                self.db.session.commit()
                self.users = {username: User(username) for username in data["users"].keys()}
                for username, borrowed_books in data["users"].items():
                    self.users[username].borrowed_books_isbns = [book['isbn'] for book in borrowed_books]
                self.genres = set(data["genres"])
                self.borrowed_books = data["borrowed_books"]
        else:
            print("File does not exist, starting with an empty library.")
