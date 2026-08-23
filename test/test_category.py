from test.conftest import product_one


def test_category_count(category_one_1):
    assert category_one_1.category_count == 1


def test_product_count(category_one_1):
    assert category_one_1.product_count == 4


def test_category(category_one_1, product_two, product_three):
    assert category_one_1.name == "Смартфоны"
    assert (
        category_one_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )


def test_category_str(category_one_1):
    assert category_one_1.__str__() == f'Смартфоны, количество продуктов: 5'


def test_category_add_product(category_one_1, product_one):
    category_one_1.add_product(product_one)
    assert category_one_1.product_count == 11