"""

(2) Create a LoggedAccount class, which inherits from Account.  When
    you create an LoggedAccount instance, you provide both a starting
    balance and a filename to which all operations will be logged.
    When you deposit or withdraw, that information is logged to a
    file, with the current timestamp.  Add a most_recent method, which
    takes an integer argument (n) and returns a list of integers
    indicating the n most recent transactions.

la = LoggedAccount(1000, 'accountlog.txt')
la.deposit(100)
la.withdraw(50)
la.balance  # will still return 1050
la.most_recent(2)  # will return a list of [100, -50]

"""
import time


class Account(object):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class LoggedAccount(Account):
    def __init__(self, balance, filename):
        super().__init__(balance)
        self.filename = filename

    def deposit(self, amount):
        super().deposit(amount)
        with open(self.filename, "a") as f:
            f.write(f"{time.time()}\t{amount}\n")

    def withdraw(self, amount):
        super().withdraw(amount)
        with open(self.filename, "a") as f:
            f.write(f"{time.time()}\t{-amount}\n")

    def most_recent(self, n):
        return [int(one_line.split("\t")[-1]) for one_line in open(self.filename)][-n:]


if __name__ == "__main__":
    a = Account(1000)
    a.deposit(100)
    a.withdraw(50)
    print(a.balance)

    la = LoggedAccount(1000, "accountlog.txt")
    la.deposit(100)
    la.withdraw(80)
    print(la.balance)
    print(la.most_recent(1))
