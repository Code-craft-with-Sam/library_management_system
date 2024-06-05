class Book:
    def __init__(self, title, author, isbn, genre, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Not Available'}"

