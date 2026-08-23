class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float = 0, quantity: int = 0):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, prod_1):
        total = prod_1.quantity * prod_1.price + self.quantity * self.price
        return total

    @classmethod
    def new_product(cls, params):
        return cls(params['name'], params['description'], params['price'], params['quantity'])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        if new_price < self.__price:
            answer = input('Вы уверены, что хотите изменить цену?\n'
                           'Y - да, N - нет.\n')
            if answer.lower() == 'y':
                self.__price = new_price
        else:
            self.__price = new_price
