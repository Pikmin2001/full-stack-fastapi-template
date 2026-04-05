from fastapi import APIRouter
from random import sample
from app.models import ClothItem

router = APIRouter()

# Mock inventory
mock_cloth_items = [
    ClothItem(id=1, name="Blue Shirt", category="shirt", gender="male", price=25.0, in_stock=True),
    ClothItem(id=2, name="Black Jeans", category="pants", gender="male", price=40.0, in_stock=True),
    ClothItem(id=3, name="Red Dress", category="dress", gender="female", price=60.0, in_stock=True),
    ClothItem(id=4, name="White Sneakers", category="shoes", gender="unisex", price=50.0, in_stock=True),
    ClothItem(id=5, name="Green Hoodie", category="hoodie", gender="unisex", price=35.0, in_stock=True),
]

@router.get("/generate-outfit")
def generate_outfit(gender: str = "male"):
    available_items = [
        item for item in mock_cloth_items
        if item.gender in [gender, "unisex"] and item.in_stock > 0
    ]
    if not available_items:
        return {"outfit": [], "message": "No items available for this gender"}
    
    outfit_items = sample(available_items, min(3, len(available_items)))
    return {"outfit": outfit_items}