from typing import Optional
from fastapi import FastAPI
import json
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
import time

app = FastAPI()
health_good = {"status": "healthy"}
my_greeting = {"message": "Hello"}

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=a0a31278-af1a-4825-8e3d-226fbe8bcabe')
)
logger.setLevel(logging.INFO)


@app.get("/health")
def health_check():
    myData = "Time is: " + time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)') + " " + str(health_good)
    logger.info(myData)
    return json.dumps(myData)

@app.get("/hello")
def greeting():
    myData = "Time is: " + time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)') + " " + str(my_greeting)
    logger.info(myData)
    return json.dumps(myData)

@app.get("/items/{item_id}")
def item(item_id: int, q: Optional[str] = None):
    logger.info("item_id=" + item_id + " q=" + q)
    return {"item_id": item_id, "q": q}
