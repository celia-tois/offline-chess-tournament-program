from models.tournament import Tournament


class CreateTournament:
    """CreateTournament class"""

    def __init__(self):
        print("Create a tournament:")
        name_input = input("Name: ")
        place_input = input("Place: ")
        date_input = [input("Start date (DD/MM/YYYY): "), input("End date (DD/MM/YYYY): ")]
        players_input = [input("Player 1: "), input("Player 2: "), input("Player 3: "), input("Player 4: "),
                         input("Player 5: "), input("Player 6: "), input("Player 7: "), input("Player 8: ")]
        time_control_input = input("Time control (bullet, blitz, coup rapide): ")
        description_input = input("Description: ")

        Tournament(name_input, place_input, date_input, players_input, time_control_input, description_input)