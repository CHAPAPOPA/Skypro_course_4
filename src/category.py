from src.product import Product


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
        self.__products.append(product)
        return self.__products

    @property
    def get_products_list(self):
        """Метод-геттер, предназначенный для вывода товаров в определенном формате."""
        return (f'{i.name}, {i.price} руб. Остаток: {i.count_in_stock} шт.' for i in self.__products)

    def __len__(self):
        """Метод возвращает общее количество товаров в категории."""
        total_stock = sum(product.count_in_stock for product in self.__products)
        return total_stock

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.__products})'


# ex_product_1 = Product('Молоко', 'Из цельного молока', 45, 100)
# ex_product_2 = Product('Мясо', 'Говядина', 456, 23)
# ex_product_3 = Product('Сыр', 'Тильзитер', 120, 67)
# ex_1 = Category('Молочные', 'Из цельного молока', [ex_product_1])
# ex_2 = Category('Мясо', 'Говядина', [ex_product_2])
# ex_1.add_products(ex_product_3)
#
#
# print(repr(ex_1))
# print(repr(ex_2))
# print(len(ex_1))
# print(len(ex_2))
# print(str(ex_1))
# print(str(ex_2))
