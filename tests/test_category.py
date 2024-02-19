import pytest

from src.category import Category
from src.product import Product, Smartphone, LawnGrass


@pytest.fixture()
def category_milk():
    return Category('Молочные', 'Из цельного молока', [])


@pytest.fixture()
def product_milk():
    return Product('Молоко', 'Из цельного молока', 140.67, 45, 'Молочные', 'Белое')


@pytest.fixture()
def product_cheese():
    return Product('Сыр', 'Тильзитер', 120, 67, 'Молочные', 'Жёлтый')


@pytest.fixture()
def product_smartphone():
    return Smartphone('iPhone 13', 'Смартфон Apple', 91_000, 10, 'Smartphone', 'чёрный', 8, '13', '256GB')


@pytest.fixture()
def product_lawn_grass():
    return LawnGrass('Bluegrass', 'Семена газонной травы', 5, 100, 'LawnGrass', 'зелёный', 'USA', 14)


def test_init_milk(category_milk):
    assert category_milk.name == 'Молочные'
    assert category_milk.description == 'Из цельного молока'
    assert category_milk._Category__products == []
    assert Category.total_categories == 1


def test_add_products(category_milk, product_milk, product_cheese, product_smartphone, product_lawn_grass):
    ex_no = ('Мясо', 'Говядина')
    category_milk.add_products(product_milk)
    category_milk.add_products(product_cheese)
    category_milk.add_products(product_smartphone)
    category_milk.add_products(product_lawn_grass)

    assert len(category_milk._Category__products) == 4
    assert category_milk._Category__products[0] == product_milk
    assert category_milk._Category__products[1] == product_cheese
    assert category_milk._Category__products[2] == product_smartphone
    assert category_milk._Category__products[3] == product_lawn_grass
    with pytest.raises(TypeError):
        category_milk.add_products(ex_no)


def test_get_products_list(category_milk, product_milk, product_cheese):
    category_milk.add_products(product_milk)
    category_milk.add_products(product_cheese)
    products_list = list(category_milk.get_products_list)
    assert len(products_list) == 2
    assert products_list[0] == 'Молоко, 140.67 руб. Остаток: 45 шт.'
    assert products_list[1] == 'Сыр, 120 руб. Остаток: 67 шт.'


def test_len(category_milk, product_milk, product_cheese):
    category_milk.add_products(product_milk)
    category_milk.add_products(product_cheese)
    assert len(category_milk) == 112


def test_str(category_milk, product_milk):
    category_milk.add_products(product_milk)
    assert str(category_milk) == 'Молочные, количество продуктов: 45 шт.'


def test_repr(category_milk):
    assert repr(category_milk) == 'Category(Молочные, Из цельного молока, [])'
