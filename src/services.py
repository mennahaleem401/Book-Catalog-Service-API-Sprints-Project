from app.repository import books_db

def add_book(book):
    books_db.append(book.dict())
    return {"message": "Book added successfully"}

def get_books():
    return books_db