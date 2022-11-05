# Inheritance, python
from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to 0"
        self.broken_phones = broken_phones
