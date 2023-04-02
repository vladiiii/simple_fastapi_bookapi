from fastapi import FastAPI, HTTPException

app = FastAPI()

BOOKDB = [
    "The Great Gatsby",
    "Atomic Habits",
    "Norwegian Wood",
]


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
