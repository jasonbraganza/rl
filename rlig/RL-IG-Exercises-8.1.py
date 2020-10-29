"""
Write a generator function, "myrange", that can take 1, 2, or 3 arguments, just
like "range".

Moreover, it should be possible to have a descending "myrange", not just
ascending.


for one_item in myrange(5):
    print(one_item, end=' ')

0 1 2 3 4

for one_item in myrange(5, 10):
    print(one_item, end=' ')

5 6 7 8 9 10

for one_item in myrange(5, 10, 2):
    print(one_item, end=' ')

5 7 9

for one_item in myrange(10, 5, -2):
    print(one_item, end=' ')

10 8 6
"""


def myrange(first, second=None, step=1):
    if second is None:
        current = 0
        stop = first
    else:
        current = first
        stop = second
    while True:
        if step > 0:
            if current > stop:
                break
        else:
            if current < stop:
                break
        yield current
        current += step


if __name__ == "__main__":
    for one_item in myrange(5):
        print(one_item, end=" ")

    for one_item in myrange(5, 10):
        print(one_item, end=" ")

    for one_item in myrange(5, 10, 2):
        print(one_item, end=" ")
    for one_item in myrange(10, 5, -2):
        print(one_item, end=" ")
