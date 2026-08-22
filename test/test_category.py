def test_category_count(category_one):
    assert category_one.category_count == 1


def test_product_count(category_one):
    assert category_one.product_count == 4


def test_category(category_one, product_two, product_three):
    assert category_one.name == "Смартфоны"
    assert (
        category_one.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )


def test_category_str(category_one):
    assert category_one.__str__() == f'Смартфоны, количество продуктов: 5'
