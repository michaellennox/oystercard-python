import unittest
from mock import Mock
from app.oystercard import Oystercard

class TestOystercard(unittest.TestCase):

    def setUp(self):
        self.card = Oystercard()
        self.mock_station = Mock()

    def test_balance_should_be_card_current_balance(self):
        self.assertEqual(self.card.balance, 0)

    def test_isin_journey_should_be_false_before_card_is_used(self):
        self.assertFalse(self.card.isin_journey)

    def test_entry_station_should_be_None_at_initialization(self):
        self.assertIsNone(self.card.entry_station)

    def test_top_up_should_increase_current_balance(self):
        self.card.top_up(10)
        self.assertEqual(self.card.balance, 10)

    def test_top_up_should_not_allow_balance_higher_than_MAXIMUM_BALANCE(self):
        self.card.top_up(Oystercard.MAXIMUM_BALANCE)
        with self.assertRaisesRegexp(RuntimeError, 'Maximum Balance is 90'):
            self.card.top_up(1)

    def test_deduct_should_reduce_balance_by_amount_passed_as_argument(self):
        self.card.top_up(10)
        self.card._deduct(5)
        self.assertEqual(self.card.balance, 5)

    def test_touch_in_should_change_isin_journey_to_true(self):
        self.card.top_up(5)
        self.card.touch_in(self.mock_station)
        self.assertTrue(self.card.isin_journey)

    def test_touch_in_should_fail_if_balance_is_below_1(self):
        with self.assertRaisesRegexp(RuntimeError, 'Minimum Balance to travel is 1'):
            self.card.touch_in(self.mock_station)

    def test_touch_in_should_set_the_station_passed_as_entry_station(self):
        self.card.top_up(5)
        self.card.touch_in(self.mock_station)

    def test_touch_out_should_change_isin_journey_to_false(self):
        self.card.top_up(5)
        self.card.touch_in(self.mock_station)
        self.card.touch_out()
        self.assertFalse(self.card.isin_journey)

    def test_touch_out_should_reduce_balance(self):
        self.card.top_up(10)
        self.card.touch_in(self.mock_station)
        self.card.touch_out()
        self.assertEqual(self.card.balance, 10 - Oystercard.MINIMUM_FARE)
