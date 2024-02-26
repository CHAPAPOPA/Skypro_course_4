from src.product import Product, Smartphone, LawnGrass


class Category:
    name: str
    description: str
    __products: list

    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, __products):
        self.name = name
        self.description = description
        self.__products = __products
        Category.total_categories += 1
        Category.total_unique_products += len(set(self.__products))

    def add_products(self, product):
        """Метод добавления товаров в список-атрибут класса."""
        if isinstance(product, Product):
            if product.count_in_stock == 0:
                raise ValueError('Товар с нулевым количеством не может быть добавлен')
            self.__products.append(product)
            return self.__products
        raise TypeError('Можно добавить только экземпляры классов Product или его наследников')

    @property
    def get_products_list(self):
        """Метод-геттер, предназначенный для вывода товаров в определенном формате."""
        return (f'{i.name}, {i.price} руб. Остаток: {i.count_in_stock} шт.' for i in self.__products)

    def avg_price(self):
        try:
            avg = sum(i.price for i in self.__products) / len(self.__products)
            return avg
        except ZeroDivisionError:
            print('В категории нет товаров')
            return 0

    def __len__(self):
        """Метод возвращает общее количество товаров в категории."""
        total_stock = sum(i.count_in_stock for i in self.__products)
        return total_stock

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.__products})'


# ex_product_1 = Product('Молоко', 'Из цельного молока', 100, 45, 'Молочные', 'Белое')
# ex_product_2 = Product('Говядина', 'Отборная', 23, 44, 'Мясо', 'Красная')
# ex_product_3 = Product('Сыр', 'Тильзитер', 120, 67, 'Молочные', 'Жёлтый')
# ex_smartphone = Smartphone('iPhone 13', 'Смартфон Apple', 91_000, 10, 'Smartphone', 'чёрный', 8, '13', '256GB')
# ex_lawn_grass = LawnGrass('Bluegrass', 'Семена газонной травы', 5, 100, 'LawnGrass', 'зелёный', 'USA', 14)
# ex_1 = Category('Молочные', 'Из цельного молока', [])
# ex_2 = Category('Мясо', 'Говядина', [ex_product_2])
# ex_no = ('Мясо', 'Говядина')
#
#
# e = ex_1.add_products(ex_lawn_grass)
# # ex_1.add_products(ex_no)
# print(repr(ex_1))
# print(repr(ex_2))
# print(len(ex_1))
# print(len(ex_2))
# print(str(ex_smartphone))
# print(str(ex_2))
# print(ex_1.add_products(ex_product_2))
# print(ex_1.avg_price())
