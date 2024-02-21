import pytest

from src.product import Product, Smartphone, LawnGrass


@pytest.fixture()
def milk():
    return Product('Молоко', 'Из цельного молока', 140.67, 45, 'Молочные', 'Белое')


@pytest.fixture()
def smartphone():
    return Smartphone('iPhone 13', 'Смартфон Apple', 91_000, 10, 'Smartphone', 'чёрный', 8, '13', '256GB')


@pytest.fixture()
def lawn_grass():
    return LawnGrass('Bluegrass', 'Семена газонной травы', 5, 100, 'LawnGrass', 'зелёный', 'USA', 14)


def test_init_1(milk):
    assert milk.name == 'Молоко'
    assert milk.description == 'Из цельного молока'
    assert milk.price == 140.67
    assert milk.count_in_stock == 45
    assert milk.category == 'Молочные'
    assert milk.color == 'Белое'


def test_init_2(smartphone):
    assert smartphone.name == 'iPhone 13'
    assert smartphone.description == 'Смартфон Apple'
    assert smartphone.price == 91000
    assert smartphone.count_in_stock == 10
    assert smartphone.category == 'Smartphone'
    assert smartphone.color == 'чёрный'
    assert smartphone.efficiency == 8
    assert smartphone.model == '13'
    assert smartphone.amount_memory == '256GB'


def test_init_3(lawn_grass):
    assert lawn_grass.name == 'Bluegrass'
    assert lawn_grass.description == 'Семена газонной травы'
    assert lawn_grass.price == 5
    assert lawn_grass.count_in_stock == 100
    assert lawn_grass.category == 'LawnGrass'
    assert lawn_grass.color == 'зелёный'
    assert lawn_grass.origin_country == 'USA'
    assert lawn_grass.germination_period == 14


def test_create_product():
    new_product = Product.create_product('Говядина', 'Отборная', 23, 44, 'Мясо', 'Красная')
    assert isinstance(new_product, Product)
    assert new_product.name == 'Говядина'
    assert new_product.description == 'Отборная'
    assert new_product.price == 23
    assert new_product.count_in_stock == 44
    assert new_product.category == 'Мясо'
    assert new_product.color == 'Красная'


def test_get_price(milk):
    assert milk.price == 140.67


def test_set_price(milk):
    milk.price = 45
    assert milk.price == 45


def test_set_price_negative(milk, capsys):
    milk.price = -100
    captured = capsys.readouterr()
    assert 'Цена введена некорректная' in captured.out


def test_set_price_zero(milk, capsys):
    milk.price = 0
    captured = capsys.readouterr()
    assert 'Цена введена некорректная' in captured.out


def test_addition(milk, smartphone, lawn_grass):
    cheese = Product('Сыр', 'Тильзитер', 120, 67, 'Молочные', 'Жёлтый')
    total_cost = milk + cheese
    assert total_cost == 140.67 * 45 + 120 * 67
    with pytest.raises(TypeError):
        milk + 5
    with pytest.raises(TypeError):
        smartphone + 5
    with pytest.raises(TypeError):
        lawn_grass + 5
    with pytest.raises(TypeError):
        lawn_grass + smartphone


def test_len(milk):
    assert len(milk) == 45


def test_str(milk):
    assert str(milk) == 'Молоко, 140.67 руб. Остаток: 45 шт.'


def test_repr(milk):
    assert repr(milk) == ("Создан объект: Product - {'name': 'Молоко', 'description': 'Из цельного "
                          "молока', '_price': 140.67, 'count_in_stock': 45, 'category': 'Молочные', "
                          "'color': 'Белое'}")
