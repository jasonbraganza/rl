"""


(2) Write an iterator, MyRange, that takes one, two, or three
    arguments.  It should function like the built-in "range"
    function:

for one_item in MyRange(5):
    print(one_item, end=' ')

0 1 2 3 4

for one_item in MyRange(5, 10):
    print(one_item, end=' ')

5 6 7 8 9

for one_item in MyRange(5, 20, 3):
    print(one_item, end=' ')

5 8 11 14 17
"""


class MyRange(object):
    def __init__(self, first, second=None, step=1):
        if second == None:
            self.current = 0
            self.end = first
        else:
            self.current = first
            self.end = second
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step >= 0:
            if self.current >= self.end:
                raise StopIteration
        else:
            if self.current <= self.end:
                raise StopIteration
        value = self.current
        self.current += self.step

        return value


if __name__ == "__main__":
    # for one_item in MyRange(5):
    #     print(one_item, end=" ")
    # for one_item in MyRange(5, 10):
    #     print(one_item, end=" ")
    # for one_item in MyRange(5, 20, 3):
    #     print(one_item, end=" ")
    for one_item in MyRange(20, 5, -2):
        print(one_item, end=" ")
