"""Define the players"""


class Player:
    """Player class"""

    def __init__(self, last_name, first_name, date_of_birth, gender, ranking):
        """Init the last_name, first_name, date_of_birth, gender and the rank"""

        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
