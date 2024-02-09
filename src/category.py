from src.product import Product


class Category:
    name: str
    description: str
    products: list

    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1
        Category.total_unique_products += len(set(self.__products))

    def add_products(self, product):
        self.__products.append(product)
        return self.__products

    def get_products_list(self):
        formatted = []
        for i in self.__products:
            formatted.append(f'{i.name}, {i.price} руб. Остаток: {i.count_in_stock} шт.')
        return formatted

    def __repr__(self):
        return f'{self.name} {self.description} {self.__products}'



