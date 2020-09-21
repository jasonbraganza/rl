class Product(object):
    def __init__(self, name):
        self.name = name
        self._prices = []

    @property
    def price(self):
        return self._prices[-1]

    @price.setter
    def price(self, new_price):
        self._prices.append(new_price)

    def price_history(self):
        return self._prices


def main():
    p = Product("book")
    p.price = 30
    p.price = 35
    print(p.price)
    p.price = 29
    print(p.price)
    print(p.price_history())


if __name__ == "__main__":
    main()
