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
