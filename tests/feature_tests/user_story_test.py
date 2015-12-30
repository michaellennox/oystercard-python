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

    def test_card_should_not_top_up_beyond_90(self):
        # In order to protect my money from theft or loss
        # As a customer
        # I want a maximum limit (of 90) on my card
        self.card.top_up(90)
        with self.assertRaisesRegexp(Exception, 'Maximum Balance is 90'):
            self.card.top_up(1)

    def test_card_should_be_able_to_be_charged_with_deduct(self):
        # In order to pay for my journey
        # As a customer
        # I need my fare deducted from my card
        self.card.top_up(10)
        self.card.deduct(5)
        self.assertEqual(self.card.balance, 5)
