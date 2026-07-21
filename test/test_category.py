def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации,"
                                    " но и получения дополнительных функций для удобства жизни")
    assert category.products == []


def test_category_count(category):
    assert category.category_count == 2
    assert category.product_count == 0
