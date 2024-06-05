class BookNotFoundError(Exception):
    def __init__(self, message="Book not found in the library"):
        self.message = message
        super().__init__(self.message)

class BookNotAvailableError(Exception):
    def __init__(self, message="Book is currently not available for borrowing"):
        self.message = message
        super().__init__(self.message)

class UserNotFoundError(Exception):
    def __init__(self, message="User not found"):
        self.message = message
        super().__init__(self.message)

class BookAlreadyBorrowedError(Exception):
    def __init__(self, message="Book has already been borrowed"):
        self.message = message
        super().__init__(self.message)

class BookAlreadyExistsError(Exception):
    """Raised when attempting to add a book that already exists in the library."""
    pass
