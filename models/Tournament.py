"""Define the players"""

from tinydb import TinyDB


class Tournament:
    """Tournament class"""

    def __init__(self,
                 name=None,
                 place=None,
                 start_date=None,
                 end_date=None,
                 players=[],
                 time_control=None,
                 description=None):
        """Init the name, place, date, players, time_control, description"""
        self.id = -1
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_rounds = 4
        self.rounds = []
        self.players = players
        self.time_control = time_control
        self.description = description
        self.table = TinyDB('tournaments.json').table('tournaments')

    def __str__(self):
        return f"{self.id}: {self.name}"

    def insert(self):
        self.id = self.table.insert(self.serialize())
        self.update()

    def update(self):
        self.table.update(self.serialize(), doc_ids=[self.id])

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_rounds": self.number_rounds,
            "rounds": self.rounds,
            "players": self.players,
            "time_control": self.time_control,
            "description": self.description
        }

    def deserialize(self, tournament):
        self.id = tournament["id"]
        self.name = tournament["name"]
        self.place = tournament["place"]
        self.start_date = tournament["start_date"]
        self.end_date = tournament["end_date"]
        self.number_rounds = tournament["number_rounds"]
        self.rounds = tournament["rounds"]
        self.players = tournament["players"]
        self.time_control = tournament["time_control"]
        self.description = tournament["description"]
        return self

    def retrieve_all(self):
        tournaments = []
        for tournament in self.table.all():
            tournaments.append(Tournament().deserialize(tournament))
        return tournaments
