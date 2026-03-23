from fastapi import FastAPI
from app.models import Book
from app.services import add_book, get_books

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Book Catalog API"}

@app.get("/books")
def list_books():
    return get_books()

@app.post("/books")
def create_book(book: Book):
    return add_book(book)