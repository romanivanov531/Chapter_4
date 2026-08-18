import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category():
    return Category(name="Смартфоны",
                    description="Смартфоны, как средство не только коммуникации, "
                                "но и получения дополнительных функций для "
                                "удобства жизни",
                    products=[])


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def product_one():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def product_two():
    return Product("Iphone 15", "512GB, Gray space")


@pytest.fixture()
def product_three():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture()
def category_one(product_one, product_two):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
        "удобства жизни",
        products=[product_one, product_two],
    )
