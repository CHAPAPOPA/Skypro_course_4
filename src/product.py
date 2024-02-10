class Product:
    name: str
    description: str
    price: int or float
    count_in_stock: int

    def __init__(self, name, description, price, count_in_stock):
        self.name = name
        self.description = description
        self._price = price
        self.count_in_stock = count_in_stock

    @classmethod
    def create_product(cls, name, description, price, count_in_stock):
        """Метод для создания экземпляров класса Product"""
        return cls(name, description, price, count_in_stock)

    @property
    def price(self):
        """Геттер для атрибута цены"""
        return self._price

    @price.setter
    def price(self, new_price):
        """Сеттер для атрибута цены"""
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self._price = new_price

    def __repr__(self):
        return f'{self.name} {self.price} {self.count_in_stock}'


# ex_1 = Product('Молоко', 'Из цельного молока', 100, 45)
# print(ex_1)
# print(ex_1.create_product('Говядина', 'Отборная', 23, 44))
# print(ex_1.get_price)
# ex_1.get_price = -1
# ex_1.get_price = 0
