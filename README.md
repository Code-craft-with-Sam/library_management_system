# 📚 Library Management System

A comprehensive and user-friendly Library Management System built using Flask and SQLAlchemy. This application allows users to borrow and return books, manage their library inventory, and much more.

## 📖 Table of Contents

1. [✨ Features](#-features)
2. [📂 Folder Structure](#-folder-structure)
3. [⚙️ Working of Application](#️-working-of-application)
4. [🚀 How to Run](#-how-to-run)
5. [🛠️ Usage](#-usage)
6. [📚 Topics Covered](#-topics-covered)
7. [🤝 Contributing](#-contributing)
8. [📜 License](#-license)

## ✨ Features

- 👤 User authentication (login/logout)
- 📖 Borrow books
- 🔄 Return books
- 📚 View available and borrowed books
- 🛠️ Manage library inventory
- 💕 Responsive design with Bootstrap.
- 🚫 Error handling for various user actions

## 📂 Folder Structure

```
library_management_system/
│
├── app.py                  # Main application file
├── config.py               # Configuration file
├── requirements.txt        # Python dependencies
├── Dockerfile              # for containerization
│
├── library_system/     
│   ├── __init__.py         # Package initializer
│   ├── book.py             # Book model
│   ├── user.py             # User model
│   ├── library.py          # Library logic
│   └── exceptions.py       # Custom exceptions
│
├── static/             
│   └── css/                # CSS files
│       └── styles.css      # Main stylesheet
│
└── templates/              # HTML templates
    ├── base.html           # Base template
    ├── index.html          # Homepage template
    ├── login.html          # Login page template
    ├── borrow_book.html    # Borrow book template
    └── return_book.html    # Return book template
```

## ⚙️ Working of Application

1. **🔒 User Authentication**: Users need to log in to borrow or return books.
2. **📖 Borrow Book**: Users can borrow books by providing the ISBN and their username. The system checks if the book is available and assigns it to the user.
3. **🔄 Return Book**: Users can return books by providing the ISBN and their username. The system verifies the user and updates the book's status to available.
4. **🛠️ Manage Inventory**: Admin can manage the inventory by adding or removing books from the database.

## 🚀 How to Run

### 🐍 Using Python Virtual Environment

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Liquizar/library_management_system.git
    cd library_management_system
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    flask run
    ```

5. **Open your browser and navigate to** `http://127.0.0.1:5000`

### 🐳 Using Docker

1. **Build the Docker image**:
   ```sh
   docker build -t library_management_system .
   ```

2. **Run the Docker container**:
   ```sh
   docker run -d -p 5000:5000 --name library_management_system_container library_management_system
   ```

3. **Open your browser** and go to `http://localhost:5000`.


## 🛠️ Usage

1. **🔒 Login**: Use the login form to authenticate.
2. **📖 Borrow Book**: Navigate to the "Borrow Book" page, enter the ISBN of the book and your username, then submit.
3. **🔄 Return Book**: Navigate to the "Return Book" page, enter the ISBN of the book and your username, then submit.
4. **📚 View Inventory**: The home page displays the list of available and borrowed books.

## 📚 Topics Covered

This project covers the following Python topics:

- **Flask Framework**
  - Setting up routes
  - Handling GET and POST requests
  - Using Flask templates
  - Flash messages for user feedback
  - User session management

- **SQLAlchemy**
  - ORM (Object-Relational Mapping)
  - Creating and managing database models
  - Database sessions and transactions

- **HTML & CSS**
  - Structuring web pages with HTML
  - Styling web pages with CSS
  - Bootstrap for responsive design

- **Python Basics**
  - Classes and objects
  - Error handling with try-except blocks
  - List comprehensions
  - Dictionary operations

- **Docker for containerization**

- **Git for version control**

## 🤝 Contributing

We welcome contributions to improve this Library Management System. To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request with a detailed description of your changes.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

