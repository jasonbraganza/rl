"""
(1) Create a class, Ticket, which represents a single ticket that you
    can get for your car.  There will be one attribute, "amount", an
    integer indicating how much the ticket is for.  Use name manging
    to ensure that no subclass accidentally reuses this attribute.

    Create a second class, Payable, which represents something you can
    pay.  It will have a single attribute, "paid", set to either True
    or False.

    Now create a third class, ParkingTicket, which inherits from both
    Ticket and Payable.  Given this class, you should be able to say:

pt = ParkingTicket(100)
print(pt.paid) # False
pt.pay(50)     # make a first payment
print(pt.paid) # False
pt.pay(50)     # make a second payment
print(pt.paid) # True

    The amount paid to date should be stored in the ParkingTicket class.

    You should also have a __str__ method that returns (in a string)
    whether the ticket was paid, and the amount:

print(pt)      # "Paid ParkingTicket for 100"

    If the ticket was partly paid, then write:

print(pt)      # "Unpaid ParkingTicket, paid 50"

Note that the number should be the final word in this string.  That'll make the next exercise easier.


"""


class Ticket(object):
    def __init__(self, amount):
        self.amount = amount


class Payable:
    def __init__(self):
        self.paid = False


class ParkingTicket(Ticket, Payable):
    def __init__(self, amount):
        Ticket.__init__(self, amount)
        Payable.__init__(self)
        self.total = 0

    def pay(self, payment):
        self.total += payment
        if self.total >= self.amount:
            self.paid = True

    def __str__(self):
        if self.paid:
            return f"Paid {type(self).__name__} for {self.amount}"
        else:
            return f"Unpaid {type(self).__name__}, paid {self.total}"


if __name__ == "__main__":
    pt = ParkingTicket(100)
    print(pt.paid)  # False
    print(pt)
    pt.pay(50)  # make a first payment
    print(pt.paid)  # False
    print(pt)
    pt.pay(50)  # make a second payment
    print(pt.paid)  # True
    print(pt)
