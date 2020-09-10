"""

(2) Define a Person class with two attributes, "name" and "age".  It
    should only be possible to set "name" to be a string, and "age" to
    be an integer.

    Setting any other attribute name should cause an error.

    And setting these attributes with other types should cause an error, too.

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, attrname, value):
        if attrname == "name":
            if isinstance(value, str):
                object.__setattr__(self, "name", value)
            else:
                raise TypeError(f"Name must be a string")
        elif attrname == "age":
            if isinstance(value, int):
                object.__setattr__(self, "age", value)
            else:
                raise TypeError(f"Age must be an integer")
        else:
            raise AttributeError(f"{attrname} is unknown")


if __name__ == "__main__":
    p1 = Person("Mario", 42)
    print(p1.name)
    print(p1.age)
    p2 = Person("42", 42)
    print(p2.name)
    print(p2.age)
    print(p2.shoesize)

