import unittest
from mock import Mock
from app.oystercard import Oystercard

class TestOystercard(unittest.TestCase):

    def setUp(self):
        self.card = Oystercard()
        self.mock_station = Mock()

    def test_balance_should_be_card_current_balance(self):
        self.assertEqual(self.card.balance, 0)

    def test_journey_history_should_start_empty(self):
        self.assertEqual(self.card.journey_history, [])

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

    def test_touch_in_should_fail_if_balance_is_below_1(self):
        with self.assertRaisesRegexp(RuntimeError, 'Minimum Balance to travel is 1'):
            self.card.touch_in(self.mock_station)

    def test_touch_out_should_reduce_balance(self):
        self.card.top_up(10)
        self.card.touch_in(self.mock_station)
        self.card.touch_out(self.mock_station)
        self.assertEqual(self.card.balance, 10 - Oystercard.MINIMUM_FARE)

    def test_touch_out_should_add_entry_and_exit_stations_to_journey_history(self):
        self.card.top_up(10)
        self.card.touch_in(self.mock_station)
        self.card.touch_out(self.mock_station)
        journey_dict = {'entry_station': self.mock_station, 'exit_station': self.mock_station}
        self.assertIn(journey_dict, self.card.journey_history)
