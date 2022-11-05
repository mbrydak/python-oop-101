import csv

# Define a class with a method that multiplies two parameters of the object


class Item:
    pay_rate = 0.8  # price after 20 percent discount
    # define a constructor
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        # validate the parameters
        assert price >= 0, f"Price {price}, must be greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity}, must be greater than or equal to 0"

        # assign the parameters to self
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

        # alert the user that the object has been created
        print(
            f"Item {self.name} has been created, there are {self.quantity} of them and each costs ${self.price}.")

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # count out floats that are point zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    @property
    def read_only_name(self):
      pass