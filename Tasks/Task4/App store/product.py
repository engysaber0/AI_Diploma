class Product:
    """
    stands for one electronic item that the store is selling
    attributes:
    name (str): the name of the item
    price (float): the price of one unit of the item
    stock (int): how many of the item are left
    """
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def take_from_stock(self, amount):
        """
        takes a certain amount out of the stock once it gets bought
        args:
        amount (int): how much to take out of the stock
        """
        self.stock -= amount