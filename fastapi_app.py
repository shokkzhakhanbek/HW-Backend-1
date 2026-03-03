from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, nfactorial!"}


@app.post("/meaning-of-life")
def meaning():
    return {"meaning": "42"}


def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


@app.get("/{num}")
def nfactorial(num: int):
    if num < 0:
        raise HTTPException(status_code=400, detail="num must be >= 0")
    return {"nfactorial": factorial(num)}




