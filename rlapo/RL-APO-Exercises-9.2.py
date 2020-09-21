"""

(2) Create a HexNumber descriptor, which stores integers but
    returns strings formatted as hexadecimal numbers (using the
    builtin "hex" function).

    By default, the descriptor will return '0x00', hex for 0.

    You can set it with an integer, in which case it'll be turned into
    a hex string.  Or you can set it with a hex string, in which case
    it'll be kept as is.

"""

from collections import defaultdict


class HexNumber(object):
    def __init__(self):
        self.number = defaultdict(int)

    def __get__(self, host_instance, host_class):
        return hex(self.number[host_instance])

    def __set__(self, host_instance, new_value):
        if isinstance(new_value, int):
            self.number[host_instance] = new_value
        elif isinstance(new_value, str):
            self.number[host_instance] = int(new_value, 16)
        else:
            raise TypeError("Please enter a numeber in decimal or hex")


class HexContainer(object):
    hn = HexNumber()


def main():
    hc = HexContainer()
    print(hc.hn)
    hc.hn = 255
    print(hc.hn)
    hc.hn = 0xA45
    print(hc.hn)


if __name__ == "__main__":
    main()
