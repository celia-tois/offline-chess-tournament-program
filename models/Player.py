"""Define the players"""

from tinydb import TinyDB


class Player:
    """Player class"""

    def __init__(self, last_name=None, first_name=None, date_of_birth=None, gender=None, ranking=None):
        """Init the last_name, first_name, date_of_birth, gender and the rank"""

        self.id = -1,
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.score = 0
        self.table = TinyDB("players.json").table('players')

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"

    def insert(self):
        self.id = self.table.insert(self.serialize())
        self.update()

    def update(self):
        self.table.update(self.serialize(), doc_ids=[self.id])

    def serialize(self):
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "ranking": self.ranking,
            "score": self.score
        }

    def deserialize(self, player):
        self.id = player["id"]
        self.last_name = player["last_name"]
        self.first_name = player["first_name"]
        self.date_of_birth = player["date_of_birth"]
        self.gender = player["gender"]
        self.ranking = player["ranking"]
        self.score = player["score"]
        return self

    def retrieve_all(self):
        players = []
        for player in self.table.all():
            players.append(Player().deserialize(player))
        return players

