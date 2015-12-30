class Oystercard(object):
    """A simulated oystercard

    Attributes:
        balance = current working balance of card
        isin_journey = boolean representing whether the card is currently in journey
    """

    MAXIMUM_BALANCE = 90
    MINIMUM_BALANCE = 1

    def __init__(self):
        self.balance = 0
        self.isin_journey = False

    def top_up(self, amount):
        """Adds amount passed as argument to balance, fails if that would take balance over 90"""
        if self.balance + amount > self.MAXIMUM_BALANCE:
            raise RuntimeError('Maximum Balance is 90')
        self.balance += amount

    def deduct(self, amount):
        """Subtracts amount passed as argument from balance."""
        self.balance -= amount

    def touch_in(self):
        """Changes the value of isin_journey to True, fails if current balance is below 1"""
        if self.balance < self.MINIMUM_BALANCE:
            raise RuntimeError('Minimum Balance to travel is 1')
        self.isin_journey = True

    def touch_out(self):
        """Changes the value of isin_journey to False"""
        self.deduct(1)
        self.isin_journey = False
