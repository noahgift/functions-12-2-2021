from fastapi import FastAPI
import uvicorn
from logic import sentiment

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello DevOps"}

@app.get("/text/{word}/")
async def text(word: str):
    """detect sentiment"""

    result = sentiment(word)
    return {"emotion": result}


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')