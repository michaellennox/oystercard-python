import unittest
from app.station import Station

class TestStation(unittest.TestCase):
    def setUp(self):
        self.station = Station('Moorgate', 1)

    def test_station_should_have_a_name(self):
        self.assertEqual(self.station.name, 'Moorgate')

    def test_station_should_have_a_zone(self):
        self.assertEqual(self.station.zone, 1)
