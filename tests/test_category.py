import pytest

from src.category import Category
from src.product import Product

product_1 = Product('Молоко', 'Из цельного молока', 140.67, 45)


@pytest.fixture()
def category_milk():
    return Category('Молочные', 'Из цельного молока')


@pytest.fixture()
def category_beef():
    return Category('Мясные', 'Из говядины')


def test_init_milk(category_milk):
    assert category_milk.name == 'Молочные'
    assert category_milk.description == 'Из цельного молока'
    assert Category.total_categories == 2


def test_init_beef(category_beef):
    assert category_beef.name == 'Мясные'
    assert category_beef.description == 'Из говядины'
    assert Category.total_categories == 3


def test_add_products(category_milk):
    assert category_milk.add_products(product_1) == [product_1]



