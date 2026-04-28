import random
from typing import Optional

def generate_outfit(items, gender: Optional[str] = None, max_price: Optional[float] = None):
    filtered_items = [
        item for item in items
        if item.in_stock
        and (gender is None or item.gender == gender)
        and (max_price is None or item.price <= max_price)
    ]

    tops = [i for i in filtered_items if i.category == "top"]
    bottoms = [i for i in filtered_items if i.category == "bottom"]
    shoes = [i for i in filtered_items if i.category == "shoes"]

    if not tops or not bottoms or not shoes:
        return None

    top = random.choice(tops)
    bottom = random.choice(bottoms)
    shoe = random.choice(shoes)

    total_price = top.price + bottom.price + shoe.price

    return {
    "top": top.model_dump(),
    "bottom": bottom.model_dump(),
    "shoes": shoe.model_dump(),
    "total_price": total_price
}