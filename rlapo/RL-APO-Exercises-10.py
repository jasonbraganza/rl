"""Create a Person class that can only be instantiated 5 times.  Any
attempt to create more instances than that will result in an exception.
"""


class TooManyPeopleError(Exception):
    pass


class Person(object):
    population = 0

    def __new__(cls, *args):
        if Person.population >= 2:
            raise TooManyPeopleError(
                f"There are too many people here. Only two allowed"
            )
        Person.population += 1
        return super().__new__(cls)

    def __init__(self, name):
        print("In Person.__init__")
        self.name = name

    def __repr__(self):
        return f"Person object, vars = {vars(self)}"


def main():
    p1 = Person("Jason")
    print(p1)
    p2 = Person("Mario")
    print(p2)
    p3 = Person("Jess")
    print(p3)


if __name__ == "__main__":
    main()
