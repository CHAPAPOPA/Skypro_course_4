class Product:
    name: str
    description: str
    price: int or float
    count_in_stock: int

    def __init__(self, name, description, price, count_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.count_in_stock = count_in_stock
