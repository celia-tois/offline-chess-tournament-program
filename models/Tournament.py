"""Define the players"""

from tinydb import TinyDB
from models.Player import Player
from models.Round import Round


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
        """
        __init__()
        Init the id, name, place, start_date, end_date, number_rounds,
        rounds, players, time_control, description and table of a player.
        :arg: name, place, start_date, end_date, players, time_control, description
        """
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
        """
        __str__()
        :rtype: str
        :return: id and name of the selected tournament
        """
        return f"{self.id}: {self.name}"

    def insert(self):
        """
        insert()
        Give the tournament the right id and call the update() function.
        """
        self.id = self.table.insert(self.serialize())
        self.update()

    def update(self):
        """
        update()
        Update the table.
        """
        self.table.update(self.serialize(), doc_ids=[self.id])

    def serialize(self):
        """
        serialize()
        :rtype: dict
        :return: tournament's info serialized
        """
        return {
            "id": self.id,
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_rounds": self.number_rounds,
            "rounds": [round.serialize() for round in self.rounds],
            "players": [player.serialize() for player in self.players],
            "time_control": self.time_control,
            "description": self.description
        }

    def deserialize(self, tournament):
        """
        deserialize()
        :arg: selected tournament
        :rtype: instance attribute
        :return: tournament's info deserialized
        """
        self.id = tournament["id"]
        self.name = tournament["name"]
        self.place = tournament["place"]
        self.start_date = tournament["start_date"]
        self.end_date = tournament["end_date"]
        self.number_rounds = tournament["number_rounds"]
        self.rounds = [Round(tournament).deserialize(round) for round in tournament["rounds"]]
        self.players = [Player().deserialize(player) for player in tournament["players"]]
        self.time_control = tournament["time_control"]
        self.description = tournament["description"]
        return self

    def retrieve_all(self):
        """
        retrieve_all()
        :rtype: list
        :return: list of deserialized tournaments
        """
        return [Tournament().deserialize(tournament) for tournament in self.table.all()]
