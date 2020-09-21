"""
(1) Write an iterator, EvenlyDivisible, that takes two arguments:
    A list of integers, and an integer.  Only return those list
    elements that are evenly divisible by the integer.  For example:

e = EvenlyDivisible([2,3,4,5,6,7,8,9], 2)

for one_item in e:
    print(one_item)

2
4
6
8

"""


class EvenlyDivisible(object):
    def __init__(self, data, divisor):
        self.data = data
        self.index = 0
        self.divisor = divisor

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            value = self.data[self.index]
            self.index += 1
            if value % self.divisor == 0:
                break
        return value


if __name__ == "__main__":
    e = EvenlyDivisible([2, 3, 4, 5, 6, 7, 8, 9], 3)

    for one_item in e:
        print(one_item)
