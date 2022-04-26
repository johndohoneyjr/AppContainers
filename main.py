from typing import Optional
from fastapi import FastAPI
import json

app = FastAPI()
health_good = {"status": "healthy"}
my_greeting = {"message": "Hello"}

@app.get("/health")
def health_check():
    return json.dumps(health_good)

@app.get("/hello")
def greeting():
    return json.dumps(my_greeting)

@app.get("/items/{item_id}")
def item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
