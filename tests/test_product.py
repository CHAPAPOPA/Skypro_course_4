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
