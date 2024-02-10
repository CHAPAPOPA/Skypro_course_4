import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def category_milk():
    return Category('Молочные', 'Из цельного молока')


@pytest.fixture()
def category_product():
    return Product('Молоко', 'Из цельного молока', 140.67, 45)


def test_init_milk(category_milk):
    assert category_milk.name == 'Молочные'
    assert category_milk.description == 'Из цельного молока'
    assert Category.total_categories == 1


def test_get_products_list(category_milk, category_product):
    category_milk.add_products(category_product)
    products_list = category_milk.get_products_list
    assert len(products_list) == 1
    assert products_list[0] == 'Молоко, 140.67 руб. Остаток: 45 шт.'


def test_repr(category_milk):
    assert repr(category_milk) == 'Молочные Из цельного молока []'
