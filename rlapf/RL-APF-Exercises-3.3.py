"""
(3) Write a function (remember) that takes a function as an
    argument, and returns a function.  The inner function can take any
    arguments, which it passes along to the input function.

    When the (returned) inner function is invoked, it returns a tuple:
    The first element is the original function's output. The second is
    a list of all previous outputs from this function.

    For example:

    def add(a, b):
        return a + b

    f = remember(add)
    f(10, 3)  # returns (13, [13])
    f(20, 5)  # returns (25, [13, 25])
    f('abc', 'defg')  # returns ('abcdefg', [13, 25, 'abcdefg'])
"""


def remember(some_func):
    history = []

    def inner(*args, **kwargs):
        value = some_func(*args, **kwargs)
        history.append(value)
        return value, history

    return inner


def add(a, b):
    return a + b


f = remember(add)


def main():
    print(f(10, 3))
    print(f("mario", "jason"))


if __name__ == "__main__":
    main()
