"""

(2) Modify the Account class such that it handles "in" telling us if
    a particular transaction amount was ever handled.

100 in a   # yes, there was a +100 transaction -- True
-30 in a   # no, no -30 transaction -- False


"""


class Account(object):
    def __init__(self):
        self.transactions = []

    def __iadd__(self, deposit):
        self.transactions.append(deposit)
        return self

    def __isub__(self, withdrawal):
        self.transactions.append(-withdrawal)
        return self

    def __repr__(self):
        return f"Balance is {self.transactions}"

    def __float__(self):
        return float(sum(self.transactions))

    def __int__(self):
        return int(sum(self.transactions)) * 100

    def __contains__(self, item):
        return item in self.transactions


def main():
    a = Account()
    a += 100
    a -= 50
    a += 200.50
    print(100 in a)


if __name__ == "__main__":
    main()
