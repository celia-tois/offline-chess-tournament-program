from models.player import Player


class AddPlayer:
    """AddPlayer class"""

    def __init__(self):
        print("Add a player:")
        last_name_input = input("Last name: ")
        first_name_input = input("First name: ")
        date_of_birth_input = input("Date of birth (DD/MM/YYYY): ")
        gender_input = input("Gender (F/M): ")
        ranking_input = input("Ranking: ")

        Player(last_name_input, first_name_input, date_of_birth_input, gender_input, ranking_input).insert()
