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

    def create_product(self):
        product = Product(self.name, self.description, self.price, self.count_in_stock)
        return product

    def get_price(self):
        return self.price

    def set_price(self, new_p):
        if new_p <= 0:
            print('Цена введена некорректная')
        else:
            self.price = new_p

    def __repr__(self):
        return f'{self.name} {self.price} {self.count_in_stock}'
