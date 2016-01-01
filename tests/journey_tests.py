import unittest
from mock import Mock
from app.journey import Journey

class TestJourney(unittest.TestCase):
    def setUp(self):
        self.journey = Journey()
        self.mock_station = Mock()

    def test_current_journey_should_have_no_entry_or_exit_before_start(self):
        self.assertEqual(self.journey.current_journey, {'entry_station': None, 'exit_station': None})

    def test_log_entry_logs_entry_station_to_current_journey(self):
        self.journey.log_entry(self.mock_station)
        self.assertEqual(self.journey.current_journey, {'entry_station': self.mock_station, 'exit_station': None})

    def test_log_exit_logs_exit_station_to_current_journey(self):
        self.journey.log_exit(self.mock_station)
        self.assertEqual(self.journey.current_journey, {'entry_station': None, 'exit_station': self.mock_station})

    def test_isin_journey_is_false_on_initialization(self):
        self.assertFalse(self.journey.isin_journey)

    def test_isin_journey_is_true_after_log_entry(self):
        self.journey.log_entry(self.mock_station)
        self.assertTrue(self.journey.isin_journey)

    def test_isin_journey_is_false_after_full_journey(self):
        self.journey.log_entry(self.mock_station)
        self.journey.log_exit(self.mock_station)
        self.assertFalse(self.journey.isin_journey)

    def test_fare_returns_1_if_journey_is_complete(self):
        self.journey.log_entry(self.mock_station)
        self.journey.log_exit(self.mock_station)
        self.assertEqual(self.journey.fare(), 1)

    def test_fare_returns_6_if_journey_is_incomplete(self):
        self.journey.log_entry(self.mock_station)
        self.assertEqual(self.journey.fare(), 6)
