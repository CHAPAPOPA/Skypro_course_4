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

    def __add__(self, other):
        return self.price * self.count_in_stock + other.price * other.count_in_stock

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.count_in_stock} шт.'

    def __repr__(self):
        return f'{self.name} {self.price} {self.count_in_stock}'


ex_1 = Product('Молоко', 'Из цельного молока', 100, 45)
ex_2 = Product('Говядина', 'Отборная', 23, 44)
ex_3 = Product('.', '.', 0, 0)


# ex_3_normal = ex_3.create_product('Сыр', 'Тильзитер', 120, 67)
# print(ex_3_normal)
# print(ex_1.price)
# ex_3.price = 0
# ex_3.price = 121
# print(ex_3.price)
# print(ex_1 + ex_3_normal)
# print(str(ex_1))
