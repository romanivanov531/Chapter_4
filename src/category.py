class Category:

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products):

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self):
        result = ' \n'.join([f'{product.name}, {product.price} руб. '
                             f'Остаток: {product.quantity} шт.' for product in self.__products])
        return result
