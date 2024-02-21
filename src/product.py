from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class ReprMixin:
    def __repr__(self, *args, **kwargs):
        return f"Создан объект: {self.__class__.__name__} - {self.__dict__}"


class Product(ReprMixin, Item):
    name: str
    description: str
    price: int or float
    count_in_stock: int
    category: str
    color: str

    def __init__(self, name, description, price, count_in_stock, category, color):
        super().__init__()
        self.name = name
        self.description = description
        self._price = price
        self.count_in_stock = count_in_stock
        self.category = category
        self.color = color

    @classmethod
    def create_product(cls, name, description, price, count_in_stock, category, color):
        """Метод для создания экземпляров класса Product"""
        return cls(name, description, price, count_in_stock, category, color)

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
        # if type(self) != type(other):
        if not isinstance(other, Product):
            raise TypeError('Нельзя складывать продукты разных типов')
        return self.price * self.count_in_stock + other.price * other.count_in_stock

    def __len__(self):
        """Метод возвращает количество товаров на складе."""
        return self.count_in_stock

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {len(self)} шт.'


class Smartphone(Product, ReprMixin):
    efficiency: int or float
    model: str
    amount_memory: str

    def __init__(self, name, description, price, count_in_stock, category, color, efficiency, model, amount_memory):
        super().__init__(name, description, price, count_in_stock, category, color)
        self.efficiency = efficiency
        self.model = model
        self.amount_memory = amount_memory

    def __add__(self, other):
        if not isinstance(other, Smartphone):
            raise TypeError('Нельзя складывать продукты разных типов')
        return self.price * self.count_in_stock + other.price * other.count_in_stock


class LawnGrass(Product, ReprMixin):
    origin_country: str
    germination_period: int or float

    def __init__(self, name, description, price, count_in_stock, category, color, origin_country, germination_period):
        super().__init__(name, description, price, count_in_stock, category, color)
        self.origin_country = origin_country
        self.germination_period = germination_period

    def __add__(self, other):
        if not isinstance(other, LawnGrass):
            raise TypeError('Нельзя складывать продукты разных типов')
        return self.price * self.count_in_stock + other.price * other.count_in_stock


# ex_1 = Product('Молоко', 'Из цельного молока', 100, 45, 'Молочные', 'Белое')
# ex_2 = Product('Говядина', 'Отборная', 23, 44, 'Мясо', 'Красная')
# ex_3 = Product('.', '.', 0, 0, '', '')
# ex_4 = Smartphone('iPhone 13', 'Смартфон Apple', 91_000, 10, 'Smartphone', 'чёрный', 8, '13', '256GB')
# ex_5 = LawnGrass('Bluegrass', 'Семена газонной травы', 5, 100, 'LawnGrass', 'зелёный', 'USA', 14)
#
# ex_3_normal = ex_3.create_product('Сыр', 'Тильзитер', 120, 67, 'Молочные', 'Жёлтый')
# print(ex_3_normal)
# print(ex_1.price)
# ex_3.price = 0
# ex_3.price = 121
# print(ex_3.price)
# print(ex_1 + ex_3_normal)
# print(str(ex_1))
# print(repr(ex_5))
# # print(ex_1 + ex_5)
