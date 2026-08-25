import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_no_price(product_two):
    assert product_two.price == 0
    assert product_two.quantity == 0


def test_product_change_price(product_one):
    product_one.price = 200000
    assert product_one.price == 200000


def test_product_str(product):
    assert product.__str__() == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'


def test_product_add(product_one, product_two):
    assert Product.__add__(product_two, product_one) == 900000.0


def test_add_wrong_type(product_one, product_four):
    with pytest.raises(TypeError):
        product_four + product_one


def test_product_mixin(capsys):
    prod = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    captured = capsys.readouterr()
    assert captured.out == 'Product, Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5\n'