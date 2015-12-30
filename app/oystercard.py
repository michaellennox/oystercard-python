class Oystercard(object):
    """A simulated oystercard

    Attributes:
        balance = current working balance of card
    """

    MAXIMUM_BALANCE = 90

    def __init__(self):
        self.balance = 0

    def top_up(self, amount):
        """Adds amount passed as argument to balance.

        Fails if that would take balance over 90"""
        if self.balance + amount > self.MAXIMUM_BALANCE:
            raise Exception('Maximum Balance is 90')
        self.balance += amount

    def deduct(self, amount):
        self.balance -= amount
