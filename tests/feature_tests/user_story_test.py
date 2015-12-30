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
        with self.assertRaisesRegexp(RuntimeError, 'Maximum Balance is 90'):
            self.card.top_up(1)

    def test_card_should_be_able_to_be_charged_with_deduct(self):
        # In order to pay for my journey
        # As a customer
        # I need my fare deducted from my card
        self.card.top_up(10)
        self.card.deduct(5)
        self.assertEqual(self.card.balance, 5)

    def test_card_should_track_whether_in_journey(self):
        # In order to get through the barriers.
        # As a customer
        # I need to touch in and out.
        self.card.top_up(10)
        self.assertFalse(self.card.isin_journey)
        self.card.touch_in()
        self.assertTrue(self.card.isin_journey)
        self.card.touch_out()
        self.assertFalse(self.card.isin_journey)

    def test_should_not_be_able_to_touch_in_if_balance_is_below_1(self):
        # In order to pay for my journey
        # As a customer
        # I need to have the minimum amount (1) for a single journey.
        with self.assertRaisesRegexp(RuntimeError, 'Minimum Balance to travel is 1'):
            self.card.touch_in()

    def test_should_deduct_from_balance_on_touch_out(self):
        # In order to pay for my journey
        # As a customer
        # When my journey is complete, I need the correct amount deducted from my card
        self.card.top_up(10)
        self.card.touch_in()
        self.card.touch_out()
        self.assertEqual(self.card.balance, 9)
