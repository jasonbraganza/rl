"""

(1) Define a class, EasyDict, which is initialized with a dictionary.
    Make it possible to retrieve values from the dictionary not only
    with [], but also as an attribute.  For example:

    ed = EasyDict({'a':1, 'b':2, 'c':3})
    print(ed['a'])  # prints 1
    print(ed.a)     # also prints 1

    It's OK to raise a KeyError if the key doesn't exist.

"""


class EasyDict:
    def __init__(self, d):
        self.d = d

    def __getitem__(self, key):
        return self.d[key]

    def __getattr__(self, key):
        return self.d[key]


if __name__ == "__main__":
    ed = EasyDict({"a": 1, "b": 2, "c": 3})
    print(ed["b"])
    print(ed.a)
