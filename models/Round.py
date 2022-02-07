from datetime import datetime
from models.Tournament import Tournament


class Round:
    def __init__(self, tournament):
        self.number = 1
        self.name = "Round " + str(len(tournament) + 1)
        self.start_date = datetime.now().isoformat(timespec='minutes')

    def serialize(self):
        return {
            "name": self.name,
            "start_date": self.start_date
        }
