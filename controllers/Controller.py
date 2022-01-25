from views.AddPlayerView import AddPlayerView
from views.CreateTournamentView import CreateTournamentView
from models.Player import Player
from models.Tournament import Tournament


class Controller:

    @staticmethod
    def add_player():
        player_info = AddPlayerView.player()
        player = Player(player_info['last_name_input'], player_info['first_name_input'], player_info['date_of_birth_input'], player_info['gender_input'], player_info['ranking_input'])
        player.insert()

    @staticmethod
    def create_tournament():
        tournament_info = CreateTournamentView.tournament()
        tournament = Tournament(tournament_info["name_input"], tournament_info["place_input"], tournament_info["start_date_input"], tournament_info["end_date_input"], tournament_info["players_input"], tournament_info["time_control_input"], tournament_info["description_input"])
        tournament.insert()
