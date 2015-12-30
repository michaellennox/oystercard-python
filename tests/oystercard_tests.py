import unittest
from app.oystercard import Oystercard

class TestOystercard(unittest.TestCase):

    def setUp(self):
        self.card = Oystercard()

    def test_balance_should_initialize_as_0(self):
        self.assertEqual(self.card.balance, 0)

    def test_top_up_should_increase_current_balance(self):
        self.card.top_up(10)
        self.assertEqual(self.card.balance, 10)
