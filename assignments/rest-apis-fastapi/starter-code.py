"""
FastAPI REST API Starter Code
Build a REST API for managing items (books, todos, products, etc.)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Create FastAPI application
app = FastAPI(title="Item Management API", version="1.0.0")

# Define data model for items
class Item(BaseModel):
    """Item model with required and optional fields"""
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: Optional[float] = None


# In-memory storage for items (replace with database in production)
items_db: List[Item] = [
    Item(id=1, name="Example Item", description="This is an example", price=9.99)
]


# TODO: Implement GET endpoint to retrieve all items
# @app.get("/items")
# def get_all_items():
#     pass


# TODO: Implement GET endpoint to retrieve a specific item by ID
# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     pass


# TODO: Implement POST endpoint to create a new item
# @app.post("/items")
# def create_item(item: Item):
#     pass


# TODO: Implement PUT endpoint to update an item
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     pass


# TODO: Implement DELETE endpoint to remove an item
# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     pass


if __name__ == "__main__":
    import uvicorn
    # Run the server: python starter-code.py
    # Then visit http://localhost:8000/docs for interactive API documentation
    uvicorn.run(app, host="0.0.0.0", port=8000)
