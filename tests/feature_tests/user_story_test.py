import unittest
from app.oystercard import Oystercard

class TestUserStories(unittest.TestCase):
    def setUp(self):
        self.card = Oystercard()

    def test_user_has_money_on_card(self):
        # In order to use public transport
        # As a customer
        # I want money on my card
        self.assertEqual(self.card.balance, 0)
