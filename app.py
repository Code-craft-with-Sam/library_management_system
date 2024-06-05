from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, User, Book
from werkzeug.security import generate_password_hash, check_password_hash
from library_system import Library, BookNotFoundError, BookNotAvailableError, UserNotFoundError, BookAlreadyBorrowedError

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

initialized = False

with app.app_context():
    db.create_all()

class LibrarySystem:
    def __init__(self, db):
        self.library = Library(db)

library_system = LibrarySystem(db)

@app.before_request
def create_tables():
    global initialized
    if not initialized:
        db.create_all()
        print("Tables created")
        if not User.query.filter_by(is_admin=True).first():
            print("Creating admin users")
            for i in range(1, 6):
                username = f'admin{i}'
                password = 'adminpassword'
                admin = User(username=username, is_admin=True)
                admin.set_password(password)
                db.session.add(admin)
            db.session.commit()
            print("Admin users created")
        initialized = True

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('register'))
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['is_admin'] = user.is_admin
            flash('Login successful.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('welcome'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if not session.get('is_admin'):
        flash('Only admins can add books.', 'danger')
        return redirect(url_for('index'))
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        genre = request.form['genre']
        book = Book(title=title, author=author, isbn=isbn, genre=genre)
        library_system.library.add_book(book)
        flash(f"Book '{title}' added to the library.", 'success')
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/view_books')
def view_books():
    books = Book.query.all()
    return render_template('view_books.html', books=books)

@app.route('/borrow_book', methods=['GET', 'POST'])
def borrow_book():
    if request.method == 'POST':
        isbn = request.form['isbn']
        username = request.form['username']
        try:
            library_system.library.borrow_book(isbn, username)
            flash("Book borrowed successfully.", 'success')
        except (BookNotFoundError, BookNotAvailableError, BookAlreadyBorrowedError) as e:
            flash(str(e), 'danger')
        return redirect(url_for('index'))
    return render_template('borrow_book.html')

@app.route('/return_book', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        isbn = request.form['isbn']
        username = request.form['username']
        try:
            library_system.library.return_book(isbn, username)
            flash("Book returned successfully.", 'success')
        except (BookNotFoundError, UserNotFoundError, BookAlreadyBorrowedError) as e:
            flash(str(e), 'danger')
        return redirect(url_for('index'))
    return render_template('return_book.html')

@app.route('/view_genres')
def view_genres():
    genres = library_system.library.view_genres()
    return render_template('view_genres.html', genres=genres)

@app.route('/save')
def save():
    if not session.get('is_admin'):
        flash('Only admins can save library data.', 'danger')
        return redirect(url_for('index'))
    library_system.library.save_to_file('library_data.json')
    flash("Library data saved.", 'success')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
