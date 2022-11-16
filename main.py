import random
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return str(random.randint(1, 6))
