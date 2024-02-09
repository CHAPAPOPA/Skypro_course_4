import pytest

from src.product import Product


@pytest.fixture()
def milk():
    return Product('Молоко', 'Из цельного молока', 140.67, 45)


def test_init(milk):
    assert milk.name == 'Молоко'
    assert milk.description == 'Из цельного молока'
    assert milk.price == 140.67
    assert milk.count_in_stock == 45


def test_create_product(milk):
    new_milk = milk.create_product()
    assert new_milk.name == milk.name
    assert new_milk.description == milk.description
    assert new_milk.price == milk.price
    assert new_milk.count_in_stock == milk.count_in_stock


def test_get_price(milk):
    assert milk.get_price() == 140.67


def test_set_price_positive():
    product = Product("Молоко", "Описание", 100, 45)
    product.set_price(140.67)
    assert product.price == 140.67


def test_set_price_zero():
    product = Product("Молоко", "Описание", 100, 45)
    product.set_price(0)
    assert product.price == 100


def test_set_price_negative():
    product = Product("Молоко", "Описание", 100, 45)
    product.set_price(-50)
    assert product.price == 100
