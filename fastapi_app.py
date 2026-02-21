from fastapi import FastAPI, HTTPException

app = FastAPI()

# 1 GET /
@app.get("/")
def hello():
    return {"message": "Hello, nfactorial!"}


# 2 POST /meaning-of-life
@app.post("/meaning-of-life")
def meaning():
    return {"meaning": "42"}


# 3 GET /{num}
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




