import unittest
from app.oystercard import Oystercard

class TestOystercard(unittest.TestCase):

    def setUp(self):
        self.card = Oystercard()

    def test_balance_should_initialize_as_0(self):
        self.assertEqual(self.card.balance, 0)
