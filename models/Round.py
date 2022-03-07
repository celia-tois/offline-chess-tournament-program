from datetime import datetime
from models.Player import Player


class Round:
    """Round class"""

    def __init__(self, tournament):
        """
        __init__()
        Init the name, start_date, end_date and matches of a tournament.
        :arg: selected tournament
        """
        self.name = "Round " + str(len(tournament) + 1)
        self.start_date = datetime.now().isoformat(timespec='minutes')
        self.end_date = None
        self.matches = []

    def serialize(self):
        """
        serialize()
        :rtype: dict
        :return: tournament's info serialized
        """
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matches": [([match[0][0].serialize(), match[0][1]],
                         [match[1][0].serialize(), match[1][1]])
                        for match in self.matches]
        }

    def deserialize(self, round):
        """
        deserialize()
        :arg: selected round
        :rtype: instance attribute
        :return: tournament's info deserialized
        """
        self.name = round["name"]
        self.start_date = round["start_date"]
        self.end_date = round["end_date"]
        self.matches = [([Player().deserialize(match[0][0]), match[0][1]],
                         [Player().deserialize(match[1][0]), match[1][1]])
                        for match in round["matches"]]
        return self
