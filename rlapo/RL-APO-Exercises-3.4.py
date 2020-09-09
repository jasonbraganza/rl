"""

(4) Finally, define __format__ such that by default, an account displays the current
    (floating-point) balance. But if we pass a format string of "detail", we'll get
    a string containing newlines showing all of the transactions.  Moreover, passing
    "detailn" where n is an integer will show the n most recent transactions.

print(f'Your account is: {a}')  # display the current balance, 250.5
print(f'Your account is: {a:detail}')  # display all transactions
print(f'Your account is: {a:detail3}')  # display last 3 transactions

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

    def __format__(self, formatstring):
        if formatstring == "detail":
            return "\n".join(
                str(one_transaction) for one_transaction in self.transactions
            )
        elif formatstring.startswith("detail"):
            number_of_transactions = int(formatstring[-1])
            return "\n".join(
                str(one_transaction)
                for one_transaction in self.transactions[-number_of_transactions:]
            )
        else:
            return str(sum(self.transactions))


def main():
    a = Account()
    a += 100
    a -= 50
    a += 200.50
    a += 100
    print(f"Your account is: {a}")  # display the current balance, 250.5
    print(f"Your account is: {a:detail}")  # display all transactions
    print(f"Your account is: {a:detail1}")  # display last 3 transactions


if __name__ == "__main__":
    main()

