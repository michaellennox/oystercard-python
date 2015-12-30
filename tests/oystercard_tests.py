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

    def test_top_up_should_not_allow_balance_higher_than_MAXIMUM_BALANCE(self):
        self.card.top_up(Oystercard.MAXIMUM_BALANCE)
        with self.assertRaisesRegexp(Exception, 'Maximum Balance is 90'):
            self.card.top_up(1)

    def test_deduct_should_reduce_balance_by_amount_passed_as_argument(self):
        self.card.top_up(10)
        self.card.deduct(5)
        self.assertEqual(self.card.balance, 5)

    def test_isin_journey_should_be_false_before_card_is_used(self):
        self.assertFalse(self.card.isin_journey)

    def test_touch_in_should_change_isin_journey_to_true(self):
        self.card.touch_in()
        self.assertTrue(self.card.isin_journey)

    def test_touch_out_should_change_isin_journey_to_false(self):
        self.card.touch_in()
        self.card.touch_out()
        self.assertFalse(self.card.isin_journey)
