

class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name:str, description:str, price:float=0, quantity:int=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
