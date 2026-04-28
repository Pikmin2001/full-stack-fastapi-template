from app.models import ClothItem

fake_items = [

    ClothItem(id=1, name="Black Oversized Tee", category="top", gender="male", price=25, in_stock=True),
    ClothItem(id=2, name="Blue Straight Jeans", category="bottom", gender="male", price=50, in_stock=True),
    ClothItem(id=3, name="White Sneakers", category="shoes", gender="male", price=70, in_stock=True),
 
    ClothItem(id=4, name="Red Blouse", category="top", gender="female", price=30, in_stock=True),
    ClothItem(id=5, name="Black Skirt", category="bottom", gender="female", price=45, in_stock=True),
    ClothItem(id=6, name="Black Flats", category="shoes", gender="female", price=55, in_stock=True),

    ClothItem(id=7, name="Gray Hoodie", category="top", gender="male", price=35, in_stock=True),
    ClothItem(id=8, name="Chino Pants", category="bottom", gender="male", price=45, in_stock=True),
    ClothItem(id=9, name="Canvas Sneakers", category="shoes", gender="male", price=40, in_stock=True),
]