import pytest

from src.category import Category


@pytest.fixture()
def category_milk():
    return Category('Молочные', 'Из цельного молока', ['Сгущёнка', 'Молоко', 'Сгущёнка', 'Сыр'])


@pytest.fixture()
def category_beef():
    return Category('Мясные', 'Из говядины', ['Шейка', 'Спинка', 'Лопаточная часть', 'Вырезка рибай'])


def test_init_milk(category_milk):
    assert category_milk.name == 'Молочные'
    assert category_milk.description == 'Из цельного молока'
    assert category_milk.products == ['Сгущёнка', 'Молоко', 'Сгущёнка', 'Сыр']
    assert Category.total_categories == 1
    assert Category.total_unique_products == 3


def test_init_beef(category_beef):
    assert category_beef.name == 'Мясные'
    assert category_beef.description == 'Из говядины'
    assert category_beef.products == ['Шейка', 'Спинка', 'Лопаточная часть', 'Вырезка рибай']
    assert Category.total_categories == 2
    assert Category.total_unique_products == 7


