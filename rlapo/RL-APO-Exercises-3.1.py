"""

(1) Modify our Account class, such that it doesn't add to the balance
with each deposit or withdrawal, but rather adds that item to
a list.  Running float() on an "Account" object will return the current
balance, while running int() will return the current balance as an integer,
in cents.

a = Account()
a += 100
a -= 50
a += 200.50

# [100, -50, 200.50]

float(a)  # should return the total as a float -- 250.5
int(a)    # should return the total as a int -- 25050


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


if __name__ == "__main__":
    a = Account()
    a += 100
    a -= 50
    a += 200.50

    # [100, -50, 200.50]
    print(a)
    print(float(a))  # should return the total as a float -- 250.5
    print(int(a))  # should return the total as a int -- 25050
