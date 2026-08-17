class Product:
    name: str
    description: str
    __price: float
    quantity: int
    __products = []

    def __init__(self, name: str, description: str, price: float = 0, quantity: int = 0):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.__products.append({
            'name' : name,
            'description' : description,
            'price' : price,
            'quantity' : quantity
        })

    @classmethod
    def new_product(cls, params: dict):
        for product in Product.__products:
            if params['name'] == product['name']:
                params['quantity'] += product['quantity']

        return cls(params['name'], params['description'], params['price'], params['quantity'])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            if new_price < self.__price:
                confirm = input('Вы уверены, что хотите изменить цену?\n'
                                'Y - да, N - нет\n')
                if confirm.lower() == 'y':
                    self.__price = new_price
