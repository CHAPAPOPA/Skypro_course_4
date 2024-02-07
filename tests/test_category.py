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
    assert category_milk.total_categories == 1


def test_init_beef(category_beef):
    assert category_beef.name == 'Мясные'
    assert category_beef.description == 'Из говядины'
    assert category_beef.products == ['Шейка', 'Спинка', 'Лопаточная часть', 'Вырезка рибай']
    assert category_beef.total_categories == 1


def test_count_products():
    Category('Мясные', 'Из говядины', ['Шейка', 'Спинка', 'Лопаточная часть', 'Вырезка рибай'])
    Category('Молочные', 'Из цельного молока', ['Сгущёнка', 'Молоко', 'Сгущёнка', 'Сыр'])
    assert Category.total_categories == 2


def test_unique_1():
    category = Category('Мясные', 'Из говядины', ['Шейка', 'Спинка', 'Лопаточная часть', 'Вырезка рибай'])
    assert category.unique_products() == 4


def test_unique_2():
    category = Category('Молочные', 'Из цельного молока', ['Сгущёнка', 'Молоко', 'Сгущёнка', 'Сыр'])
    assert category.unique_products() == 3
