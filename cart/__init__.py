import json
from products import get_product, Product
from cart import dao


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @classmethod
    def load(cls, data):
        """Factory method to create a Cart instance from a dictionary."""
        return cls(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list[Product]:
    """Fetches the cart details for a given username and returns a list of Product objects."""
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    items = []
    for cart_detail in cart_details:
        # Parse JSON string safely instead of using eval
        contents = json.loads(cart_detail['contents'])
        for product_id in contents:
            product = get_product(product_id)
            items.append(product)
    
    return items


def add_to_cart(username: str, product_id: int):
    """Adds a product to the user's cart."""
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    """Removes a product from the user's cart."""
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    """Deletes the user's cart."""
    dao.delete_cart(username)
