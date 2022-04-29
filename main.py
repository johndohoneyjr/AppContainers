from typing import Optional
from fastapi import FastAPI
import json
import logging
import time

app = FastAPI()
health_good = {"status": "healthy"}
my_greeting = {"message": "Hello"}


@app.get("/health")
def health_check():
    myData = "Time is: " + time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)') + " " + str(health_good)
    return json.dumps(myData)

@app.get("/hello")
def greeting():
    myData = "Time is: " + time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)') + " " + str(my_greeting)
    return json.dumps(myData)

@app.get("/items/{item_id}")
def item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
