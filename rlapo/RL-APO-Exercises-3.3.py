"""

(3) Further modify it such that if the person has no money or is in
    overdraft, it returns False in a boolean context.

if a:
    print("Hello, Mr. Moneybags!")
else:
    print("Hello, Ms. Poverty!")


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

    def __bool__(self):
        return sum(self.transactions) > 0


def main():
    a = Account()
    a += 100
    a -= 50
    a += 200.50
    a -= 5000
    if a:
        print("You have money")
    else:
        print("You have no money")


if __name__ == "__main__":
    main()
