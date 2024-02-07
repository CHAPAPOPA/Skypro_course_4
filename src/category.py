class Category:
    name: str
    description: str
    products: list

    total_categories = 0
    total_unique_products = set()

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1

    def unique_products(self):
        Category.total_unique_products.update(self.products)
        return len(Category.total_unique_products)



