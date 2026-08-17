class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0
    __products = []

    def __init__(self, name: str, description: str, products):
        if len(products) < 1:
            products = []
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @classmethod
    def add_product(cls, product):
        cls.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return [f'{product.name}, {product.price} руб. Остаток: {product.quantity}' for product in self.__products]
