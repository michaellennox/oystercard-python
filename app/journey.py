class Journey(object):
    """This class handles managing individual journeys for the oystercard

    Attributes:
        current_journey = A dict with the entry and exit station for the current journey
        isin_journey = boolean representing whether the card is currently in journey
    """

    def __init__(self):
        self.current_journey = {'entry_station': None, 'exit_station': None}
        self.isin_journey = False

    def log_entry(self, station):
        self.current_journey['entry_station'] = station
        self.isin_journey = True

    def log_exit(self, station):
        self.current_journey['exit_station'] = station
        self.isin_journey = False

    def fare(self):
        return 6 if self.isin_journey else 1
