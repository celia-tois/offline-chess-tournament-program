from models.Tournament import Tournament

class PairGeneration:
    def __init__(self):
        with open("tournament.json", "r") as tournament:
            for tournaments in tournament:
                print(Tournament.deserialize(self, tournaments))
