from fastapi import FastAPI, HTTPException
import json
import os
import random

app = FastAPI()

BOOKS_FILE = "books.json"
BOOKDB = [
    "The Great Gatsby",
    "Atomic Habits",
    "Norwegian Wood",
]

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
async def add_book(book: str):
    BOOKDB.append(book)
    with open(BOOKS_FILE, "w") as f:
        json.dump(BOOKDB, f)
    return {"message": f"Added '{book}'"}
