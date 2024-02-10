from src.product import Product


class Category:
    name: str
    description: str
    __products: list

    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1
        Category.total_unique_products += len(set(self.__products))

    def add_products(self, product):
        """Метод добавления товаров в список-атрибут класса."""
        self.__products.append(product)
        return self.__products

    @property
    def get_products_list(self):
        """Метод-геттер, предназначенный для вывода товаров в определенном формате."""
        formatted = []
        for i in self.__products:
            formatted.append(f'{i.name}, {i.price} руб. Остаток: {i.count_in_stock} шт.')
        return formatted

    def __repr__(self):
        return f'{self.name} {self.description} {self.__products}'


# ex_1 = Category('Молоко', 'Из цельного молока')
# print(ex_1)
# list_1 = Product('Молоко', 'Описание', 100, 45)
# print(ex_1.add_products(list_1))
# print(ex_1.get_products_list)
