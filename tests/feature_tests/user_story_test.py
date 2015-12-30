import unittest
from app.oystercard import Oystercard

class TestUserStories(unittest.TestCase):
    def setUp(self):
        self.card = Oystercard()

    def test_card_should_track_balance(self):
        # In order to use public transport
        # As a customer
        # I want money on my card
        self.assertEqual(self.card.balance, 0)

    def test_user_should_be_able_to_top_up_card(self):
        # In order to keep using public transport
        # As a customer
        # I want to add money to my card
        self.card.top_up(5)
        self.assertEqual(self.card.balance, 5)
