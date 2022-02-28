"""Define the players"""

from tinydb import TinyDB


class Player:
    """Player class"""

    def __init__(self,
                 last_name=None,
                 first_name=None,
                 date_of_birth=None,
                 gender=None,
                 ranking=None):
        """
        __init__()
        Init the id, last_name, first_name, date_of_birth, gender,
        ranking, score and table of a player.
        :arg: last_name, first_name, date_of_birth, gender, ranking
        """
        self.id = -1,
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.score = 0
        self.table = TinyDB("players.json").table('players')

    def __str__(self):
        """
        __str__()
        :rtype: str
        :return: id, first_name and last_name of the selected player
        """
        return f"{self.id}: {self.first_name} {self.last_name}"

    def insert(self):
        """
        insert()
        Give the player the right id and call the update() function.
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
        :return: player's info serialized
        """
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
        """
        deserialize()
        :arg: selected player
        :rtype: instance attribute
        :return: player's info deserialized
        """
        self.id = player["id"]
        self.last_name = player["last_name"]
        self.first_name = player["first_name"]
        self.date_of_birth = player["date_of_birth"]
        self.gender = player["gender"]
        self.ranking = player["ranking"]
        self.score = player["score"]
        return self

    def retrieve_all(self):
        """
        retrieve_all()
        :rtype: list
        :return: list of deserialized players
        """
        return [Player().deserialize(player) for player in self.table.all()]
