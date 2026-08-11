from test.conftest import category


def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации,"
                                    " но и получения дополнительных функций для удобства жизни")
    assert category.products == []


def test_category_count(category):
    assert category.category_count == 2


def test_product_count(category_1):
    assert category_1.product_count == 2