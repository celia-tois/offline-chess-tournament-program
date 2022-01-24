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

    def serialize(self):
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "ranking": self.ranking
        }

    def insert(self):
        database = TinyDB('players.json')
        player_table = database.table('players')
        player_table.insert(self.serialize())

    def update(self):
        self.id = id


