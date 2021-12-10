from typing import Optional
from fastapi import FastAPI
import json

app = FastAPI()
health_good = {"status": "healthy"}

@app.get("/health")
def health_check():
    return json.dumps(health_good)


@app.get("/items/{item_id}")
def item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
