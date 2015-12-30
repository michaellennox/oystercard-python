class Oystercard(object):

    def __init__(self):
        self.balance = 0

    def top_up(self, amount):
        self.balance += amount
