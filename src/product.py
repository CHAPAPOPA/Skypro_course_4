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
        if type(self) is not type(other):
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


class LawnGrass(Product, ReprMixin):
    origin_country: str
    germination_period: int or float

    def __init__(self, name, description, price, count_in_stock, category, color, origin_country, germination_period):
        super().__init__(name, description, price, count_in_stock, category, color)
        self.origin_country = origin_country
        self.germination_period = germination_period
