from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"messsage": "Hello", "var": 1234}
