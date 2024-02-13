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


def test_create_product():
    new_product = Product.create_product('Говядина', 'Отборная', 23, 44)
    assert isinstance(new_product, Product)
    assert new_product.name == 'Говядина'
    assert new_product.description == 'Отборная'
    assert new_product.price == 23
    assert new_product.count_in_stock == 44


def test_get_price(milk):
    assert milk.price == 140.67


def test_set_price(milk):
    milk.price = 45
    assert milk.price == 45


def test_set_price_negative(milk, capsys):
    milk.price = -100
    captured = capsys.readouterr()
    assert "Цена введена некорректная" in captured.out


def test_set_price_zero(milk, capsys):
    milk.price = 0
    captured = capsys.readouterr()
    assert "Цена введена некорректная" in captured.out


def test_addition(milk):
    cheese = Product('Сыр', 'Тильзитер', 120, 67)
    total_cost = milk + cheese
    assert total_cost == 140.67 * 45 + 120 * 67


def test_str(milk):
    assert str(milk) == 'Молоко, 140.67 руб. Остаток: 45 шт.'


def test_repr(milk):
    assert repr(milk) == "Молоко 140.67 45"



