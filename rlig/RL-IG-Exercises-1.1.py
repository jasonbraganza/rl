"""
Write an iterator ("Circle") that takes two arguments, an iterable and
an integer. The integer indicates how many elements you'll get back
from the iterator.  The elements will be taken from the iterable.  If
the iterable is too short, then the iterator will return to the start.

So if we say:

    c = Circle('abcd', 7)

We can then say:

    for one_item in c:
        print(one_item)

And we'll get:

a
b
c
d
a
b
c
"""


class Circle(object):
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value


if __name__ == "__main__":
    c = Circle("abc", 5)
    for one_item in c:
        print(one_item)
