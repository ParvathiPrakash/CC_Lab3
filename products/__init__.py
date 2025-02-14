from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data):
        """Factory method to create a Product instance from a dictionary."""
        return cls(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    """Fetches all products and converts them into Product objects."""
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """Fetches a single product by ID and converts it into a Product object."""
    return Product.load(dao.get_product(product_id))


def add_product(product: dict):
    """Adds a new product using the DAO."""
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """Updates the quantity of a product. Raises an error if quantity is negative."""
    if qty < 0:
        raise ValueError("Quantity cannot be negative")
    dao.update_qty(product_id, qty)
