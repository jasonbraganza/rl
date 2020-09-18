"""

(2) Create DollarMixin and EuroMixin

    Right now, the amounts are printed as just numbers. We might want to put some
    numeric symbols there. Create two mixins, DollarMixin and EuroMixin, that
    modify the __str__ printout to include that symbol.
"""


class Ticket(object):
    def __init__(self, amount):
        self.amount = amount


class Payable:
    def __init__(self):
        self.paid = False


class RupeeMixin(object):
    def __str__(self):
        if self.paid:
            return f"Paid {type(self).__name__} for INR {self.amount}"
        else:
            return f"Unpaid {type(self).__name__}, paid INR {self.total}"


class EuroMixin(object):
    def __str__(self):
        if self.paid:
            return f"Paid {type(self).__name__} for EUR {self.amount}"
        else:
            return f"Unpaid {type(self).__name__}, paid EUR {self.total}"


class ParkingTicket(EuroMixin, Ticket, Payable):
    def __init__(self, amount):
        Ticket.__init__(self, amount)
        Payable.__init__(self)
        self.total = 0

    def pay(self, payment):
        self.total += payment
        if self.total >= self.amount:
            self.paid = True


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
