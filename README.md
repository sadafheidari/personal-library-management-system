# Personal Library Management System

A beginner-friendly command-line application built with Python for managing a personal book collection.

The program allows users to add, view, search, remove, borrow, and return books. Book information is stored in a JSON file so the data remains available after the program is closed.

## Features

- Add new books
- View all books
- Search for a book by title
- Remove books
- Borrow available books
- Return borrowed books
- Save book data to a JSON file
- Load saved books automatically when the program starts
- Validate menu selections

## Technologies Used

- Python
- JSON
- Git
- GitHub
- PyCharm

## Project Structure

```text
personal-library-management-system/
├── personal-library-management-system.py
├── books.json
├── .gitignore
├── README.md
└── images/
    └── program-demo.png
```

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/sadafheidari/personal-library-management-system.git
```

2. Open the project folder:

```bash
cd personal-library-management-system
```

3. Run the Python program:

```bash
python personal-library-management-system.py
```

## Example Book Data

```json
{
    "title": "atomic habits",
    "author": "james clear",
    "year": "2018",
    "price": "20",
    "status": "Available"
}
```

## Program Screenshot

![Personal Library Management System Demo](images/program-demo.png)

## What I Learned

Through this project, I practiced:

- Python variables and data structures
- Lists and dictionaries
- Loops and conditional statements
- User input handling
- File handling
- Reading and writing JSON data
- Error handling with `try` and `except`
- Building a menu-driven command-line application
- Version control using Git and GitHub

## Future Improvements

- Add input validation for year and price
- Prevent duplicate book titles
- Save changes immediately instead of only when exiting
- Organize the program using functions
- Add book IDs
- Add sorting and filtering options

## Author

**Sadaf Heidari**

GitHub: [sadafheidari](https://github.com/sadafheidari)
