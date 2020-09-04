"""

(2) Write a function ("getitems") that takes any number of arguments.
    It returns a function that takes a sequence as an argument.  That
    inner function then returns a tuple containing elements of its
    sequence at those indexes.

    For example:

    f = getitems(2, 4, 3)
    f('abcdefg')   # returns ('c', 'e', 'd')
    f('uvwxyz')   # returns ('w', 'y', 'x')

    f([10, 20, 30, 40, 50, 60, 70])  # returns (30, 50, 40)

    And yes, this is very similar to operator.itemgetter.


"""


def getitems(*args):
    def inner(s):
        output = []
        for one_index in args:
            output.append(s[one_index])
        return tuple(output)

    return inner


f = getitems(0, 4, 3)


def main():
    print(f("abcdefg"))
    print(f("uvwxyz"))
    print(f([10, 20, 30, 40, 50, 60, 70]))


if __name__ == "__main__":
    main()
