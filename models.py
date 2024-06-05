from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(150), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')>"
    
    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'available': self.available
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            isbn=data['isbn'],
            title=data['title'],
            author=data['author'],
            genre=data['genre'],
            available=data['available']
        )

