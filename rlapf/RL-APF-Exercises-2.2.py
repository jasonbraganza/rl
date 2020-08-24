"""
(2) The "globals" function returns a dictionary containing all global
    variables in Python.  Assuming that you have the string

    'x={x}, y={y}'

    already defined in Python, and that both "x" and "y" are defined
    global variables, how can you get the string to display the values
    of both "x" and "y"?

"""
x = 2
y = 3


my_ = globals()

print(f"{x=}, {y=}")
