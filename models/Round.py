from datetime import datetime


class Round:
    def __init__(self):
        self.number = 1
        self.name = "Round " + str(self.number)
        self.start_date = datetime.now().isoformat(timespec='minutes')

    def serialize(self):
        return {
            "name": self.name,
            "start_date": self.start_date
        }
