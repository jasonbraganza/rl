"""(2) Create an Account class, to which you can deposit with "+=" and
    withdraw with "-=".

a = Account()
a += 100
print(a)  # prints 100
a += 1000
print(a)  # prints 1100
a -= 500
print(a)  # prints 600"""


class Account(object):
    def __init__(self):
        self.balance = 0

    def __iadd__(self, deposit):
        self.balance += deposit
        return self

    def __isub__(self, withdrawal):
        self.balance -= withdrawal
        return self

    def __repr__(self):
        return f"Balance is {self.balance}"


if __name__ == "__main__":
    a = Account()
    a += 100
    print(a)  # prints 100
    a += 1000
    print(a)  # prints 1100
    a -= 500
    print(a)  # prints 60
