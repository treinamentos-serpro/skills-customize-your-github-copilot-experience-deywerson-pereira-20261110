from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Classroom Inventory API")


class Item(BaseModel):
    id: int
    name: str
    quantity: int = Field(ge=0)


items: dict[int, Item] = {}


@app.get("/")
def read_root():
    return {"message": "Classroom Inventory API"}


@app.get("/items")
def list_items():
    # Return all items stored in memory.
    pass


# Add POST /items and GET /items/{item_id}.
# Add PUT /items/{item_id} and DELETE /items/{item_id}.