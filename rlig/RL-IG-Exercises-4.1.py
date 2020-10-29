"""
Create a Warehouse class containing products. Each product will be
represented by a three-element tuple containing:

    - product name
    - product price
    - product ID number

The Warehouse should be iterable, returning one tuple with each
iteration. By default, the items should be sorted by ID number.

(You don't need to enforce uniqueness, since more than one
item of each type is likely stored in the warehouse.)

You can add a new item to the warehouse with the "add_item" method,
which takes three arguments.

You can remove an item from the warehouse with the "remove_item" method,
which takes one argument (an ID number).  Only the first item matching
the ID number will be removed.

If the warehouse changes during the iteration, it should return an
error.

Add two methods, by_price and by_name, to the Warehouse class.  Each of
these returns a list (which is iterable by definition) of the tuples,
sorted by price or name, respectively.

"""

import operator


class WarehouseIterator:
    def __init__(self, items):
        self.items = sorted(items, key=operator.itemgetter(2))
        self.original_items = items
        self.index = 0

    def __next__(self):
        if len(self.items) != len(self.original_items):
            raise RuntimeError
        if self.index >= len(self.items):
            raise StopIteration
        value = self.items[self.index]
        self.index += 1
        return value


class Warehouse:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, id_number):
        self.items.append((name, price, id_number))

    def remove_item(self, id_number):
        for index, one_item in enumerate(self.items):
            if one_item[2] == id_number:
                self.items.pop(index)
                break

    def by_price(self):
        return sorted(self.items, key=operator.itemgetter(1))

    def by_name(self):
        return sorted(self.items, key=operator.itemgetter(0))

    def __iter__(self):
        return WarehouseIterator(self.items)


if __name__ == "__main__":
    wh = Warehouse()
    wh.add_item("book", 50, 10)
    wh.add_item("pasta", 10, 15)
    wh.add_item("pasta sauce", 5, 20)
    wh.add_item("newspaper", 2, 5)
    for one_item in wh:
        print(one_item)
    wh.remove_item(5)
    for one_item in wh:
        print(one_item)
    print("by name")
    for one_item in wh.by_name():
        print(one_item)
    print("by price")
    for one_item in wh.by_price():
        print(one_item)
