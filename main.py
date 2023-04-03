from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional, Literal
from uuid import uuid4
import json
import os
import random

app = FastAPI()


class Book(BaseModel):
    name: str
    price: float
    genre: Literal["fiction", "non-fiction"]
    book_id: Optional[str] = uuid4().hex


BOOKS_FILE = "books.json"
BOOKDB = []

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        BOOKDB = json.load(f)


@app.get("/")
async def home():
    return {"messsage": "Welcome to the best BookStore"}


@app.get("/list-books")
async def list_books():
    return {"books": BOOKDB}


@app.get("/book-index/{index}")
async def book_index(index: int):
    if index < 0 or index > len(BOOKDB):
        raise HTTPException(404, f"Index {index} out of range {len(BOOKDB)}.")
    else:
        return {"book": BOOKDB[index]}


@app.get("/get-random-book")
async def get_random_book():
    return {"book": random.choice(BOOKDB)}


@app.post("/add-book")
async def add_book(book: Book):
    book.book_id = uuid4().hex
    json_book = jsonable_encoder(book)
    BOOKDB.append(json_book)
    with open(BOOKS_FILE, "w") as f:
        json.dump(BOOKDB, f)
    return {"message": f"Added '{book}'", "id": book.book_id}


@app.get("/get-book")
async def get_book(book_id: str):
    for book in BOOKDB:
        if book["book_id"] == book_id:
            return book
        else:
            raise HTTPException(404, f"Book does not exsist '{book_id}'")
