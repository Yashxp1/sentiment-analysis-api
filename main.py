from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a data model for request validation
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Endpoint with path and query parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}

# Endpoint accepting a JSON request body
@app.post("/items/")
def create_item(item: Item):
    return {"status": "created", "item": item}
