""" 

(2) Create a Box class, which will have three attributes: Height, width,
    and length.  Create comparison methods, such that we're comparing
    the volume of a box.

"""
from functools import total_ordering


@total_ordering
class Box(object):
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length

    def __repr__(self):
        return f"Box with {vars(self)}"

    def volume(self):
        return self.height * self.width * self.length

    def __eq__(self, other):
        return self.volume() == other.volume()

    def __lt__(self, other):
        return self.volume() < other.volume()


def main():
    b1 = Box(4, 2, 2)
    b2 = Box(2, 4, 2)
    b3 = Box(3, 2, 2)
    b4 = Box(5, 3, 8)
    print(b1)
    print(b1 == b2)
    print(b3 == b4)
    print(b4 > b2)
    print(b3 >= b1)


if __name__ == "__main__":
    main()

