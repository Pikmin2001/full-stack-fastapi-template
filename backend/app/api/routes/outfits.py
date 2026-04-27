from fastapi import APIRouter
import random
from typing import Optional

from app.models import ClothItem

router = APIRouter(prefix="/outfits", tags=["outfits"])


items = [
    ClothItem(id=1, name="Blue Shirt", category="top", gender="male", price=25.0, in_stock=True),
    ClothItem(id=2, name="Black Jeans", category="bottom", gender="male", price=40.0, in_stock=True),
    ClothItem(id=3, name="White Sneakers", category="shoes", gender="male", price=60.0, in_stock=True),
    ClothItem(id=4, name="Red Shirt", category="top", gender="female", price=30.0, in_stock=True),
    ClothItem(id=5, name="Skirt", category="bottom", gender="female", price=45.0, in_stock=True),
]


@router.post("/generate")
def generate_outfit(
    gender: Optional[str] = None,
    max_price: Optional[float] = None,
):
    filtered_items = [
        item for item in items
        if item.in_stock
        and (gender is None or item.gender == gender)
        and (max_price is None or item.price <= max_price)
    ]

    tops = [i for i in filtered_items if i.category == "top"]
    bottoms = [i for i in filtered_items if i.category == "bottom"]
    shoes = [i for i in filtered_items if i.category == "shoes"]

    top = random.choice(tops) if tops else None
    bottom = random.choice(bottoms) if bottoms else None
    shoe = random.choice(shoes) if shoes else None

    total_price = sum([i.price for i in [top, bottom, shoe] if i])

    return {
        "top": top,
        "bottom": bottom,
        "shoes": shoe,
        "total_price": total_price
    }

@router.post("/swap")
def swap_item(
    current_outfit: dict,
    item_type: str
):
    # Get current item
    current_item = current_outfit.get(item_type)

    if not current_item:
        return {"error": "No item to swap"}

    # Normalize current item
    if isinstance(current_item, dict):
        current_id = current_item.get("id")
        current_price = current_item.get("price")
        current_gender = current_item.get("gender")
    else:
        current_id = current_item.id
        current_price = current_item.price
        current_gender = current_item.gender

    # Step 1: same category + in stock
    candidates = [
        item for item in items
        if item.category == item_type and item.in_stock
    ]

    # Step 2: remove current item FIRST
    candidates = [i for i in candidates if i.id != current_id]

    if not candidates:
        return {"error": "No items available to swap"}

    # Step 3: try same gender
    same_gender = [i for i in candidates if i.gender == current_gender]
    if same_gender:
        candidates = same_gender

    # Step 4: try similar price (but don’t force it)
    similar_price = [
        i for i in candidates
        if abs(i.price - current_price) <= 20
    ]
    if similar_price:
        candidates = similar_price

    # Step 5: pick closest price
    best_item = min(candidates, key=lambda x: abs(x.price - current_price))

    # Replace with dict
    current_outfit[item_type] = best_item.dict()

    # Recalculate total price
    total_price = sum([
        item["price"]
        for key, item in current_outfit.items()
        if key != "total_price" and item
    ])

    current_outfit["total_price"] = total_price

    return current_outfit