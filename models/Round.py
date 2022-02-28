from datetime import datetime


class Round:
    def __init__(self, tournament):
        self.number = 1
        self.name = "Round " + str(len(tournament) + 1)
        self.start_date = datetime.now().isoformat(timespec='minutes')
        self.end_date = None
        self.matches = []

    def serialize(self):
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matches": [[(match[0][0].serialize(), match[0][1].serialize()),
                         (match[1][0].serialize(), match[1][1].serialize())]
                        for match in self.matches]
        }

    def deserialize(self, round):
        self.name = round["name"]
        self.start_date = round["start_date"]
        self.end_date = round["end_date"]
        self.matches = [[[match[0][0].deserialize(round), match[0][1]].deserialize(round),
                         [match[1][0].deserialize(round), match[1][1].deserialize(round)]]
                        for match in self.matches]
        return self
