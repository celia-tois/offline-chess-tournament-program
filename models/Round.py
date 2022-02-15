from datetime import datetime


class Round:
    def __init__(self, tournament):
        self.number = 1
        self.name = "Round " + str(len(tournament) + 1)
        self.start_date = datetime.now().isoformat(timespec='minutes')
        self.end_date = None

    def serialize(self):
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
