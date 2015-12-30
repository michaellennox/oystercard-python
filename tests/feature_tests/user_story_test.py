import unittest
from app.oystercard import Oystercard
from app.station import Station

class TestUserStories(unittest.TestCase):
    def setUp(self):
        self.card = Oystercard()
        self.moorgate = Station('Moorgate', 1)
        self.liverpool_st = Station('Liverpool St.', 1)

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
        self.card._deduct(5)
        self.assertEqual(self.card.balance, 5)

    def test_card_should_track_whether_in_journey(self):
        # In order to get through the barriers.
        # As a customer
        # I need to touch in and out.
        self.card.top_up(10)
        self.assertFalse(self.card.isin_journey)
        self.card.touch_in(self.moorgate)
        self.assertTrue(self.card.isin_journey)
        self.card.touch_out(self.liverpool_st)
        self.assertFalse(self.card.isin_journey)

    def test_should_not_be_able_to_touch_in_if_balance_is_below_1(self):
        # In order to pay for my journey
        # As a customer
        # I need to have the minimum amount (1) for a single journey.
        with self.assertRaisesRegexp(RuntimeError, 'Minimum Balance to travel is 1'):
            self.card.touch_in(self.moorgate)

    def test_should_deduct_from_balance_on_touch_out(self):
        # In order to pay for my journey
        # As a customer
        # When my journey is complete, I need the correct amount deducted from my card
        self.card.top_up(10)
        self.card.touch_in(self.moorgate)
        self.card.touch_out(self.liverpool_st)
        self.assertEqual(self.card.balance, 9)

    def test_card_should_track_where_it_was_touched_in(self):
        # In order to pay for my journey
        # As a customer
        # I need to know where I've travelled from
        self.card.top_up(10)
        self.card.touch_in(self.moorgate)
        self.assertEqual(self.card.entry_station, self.moorgate)

    def test_card_should_track_journey_history(self):
        # In order to know where I have been
        # As a customer
        # I want to see to all my previous trips
        self.card.top_up(10)
        self.card.touch_in(self.moorgate)
        self.card.touch_out(self.liverpool_st)
        journey_dict = {'entry_station': self.moorgate, 'exit_station': self.liverpool_st}
        self.assertIn(journey_dict, self.card.journey_history)

    def test_station_should_save_zone(self):
        # In order to know how far I have travelled
        # As a customer
        # I want to know what zone a station is in
        self.assertEqual(self.moorgate.zone, 1)
