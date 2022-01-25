from models.Tournament import Tournament
from models.Player import Player


class CreateTournamentView:
    """CreateTournament class"""

    @staticmethod
    def tournament():
        print("Create a tournament:")
        data = dict()
        data["name_input"] = input("Name: ")
        data["place_input"] = input("Place: ")
        data["start_date_input"] = input("Start date (DD/MM/YYYY): ")
        data["end_date_input"] = input("End date (DD/MM/YYYY): ")
        data["players_input"] = CreateTournamentView.display_players()
        data["time_control_input"] = input("Time control (bullet, blitz, coup rapide): ")
        data["description_input"] = input("Description: ")
        return data

    @staticmethod
    def display_players():
        players_to_display = Player().retrieve_all()
        players_selected = []
        while len(players_selected) < 8:
            for player in players_to_display:
                print(f"{player['id']}: {player['first_name']} {player['last_name']}")
            players_input = input("Player: ")
            for player in players_to_display:
                if int(players_input) == player['id']:
                    players_selected.append(player)
                    players_to_display.remove(player)
        return players_selected
