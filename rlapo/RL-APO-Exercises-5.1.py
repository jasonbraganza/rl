"""

(1) Create an Account class, in which we have a single attribute, "balance".

    When you create an Account instance, you can set the
    balance. After that, while you can set "balance", you'll provide
    "deposit" and "withdraw" methods to add or subtract from the
    balance.

a = Account(1000)
a.deposit(100)
a.withdraw(50)
a.balance # should return # 1050

"""

class Account(object):
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

# should return # 1050


if __name__ == "__main__":
    a = Account(1000)
    a.deposit(100)
    a.withdraw(50)
    print(a.balance)