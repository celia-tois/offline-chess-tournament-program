"""Define the players"""

from models.player import Player
from tinydb import TinyDB, Query, where


class Tournament:
    """Tournament class"""

    def __init__(self, name=None, place=None, date=None, time_control=None, description=None):
        """Init the name, place, date, players, time_control, description"""

        self.name = name
        self.place = place
        self.date = date
        self.number_rounds = 4
        self.rounds = "liste des instances de rondes"
        self.players = []
        self.time_control = time_control
        self.description = description

    def serialize(self):
        return {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "number_rounds": self.number_rounds,
            "rounds": self.rounds,
            "players": self.players,
            "time_control": self.time_control,
            "description": self.description
        }

    def insert(self):
        database = TinyDB('tournament.json')
        tournament_table = database.table('tournament')
        tournament_table.insert(self.serialize())





