from views.PlayerView import PlayerView
from views.TournamentView import TournamentView
from views.ErrorHandlerView import ErrorHandlerView
from models.Player import Player
from models.Tournament import Tournament


class Controller:
    """Controller class"""

    @staticmethod
    def add_player():
        """
        add_player()
        Create a new player by calling the function player() inside
        PlayerView class and giving the acquired values to Player class.
        """
        player_info = PlayerView.player()
        player = (Player(player_info['last_name_input'],
                         player_info['first_name_input'],
                         player_info['date_of_birth_input'],
                         player_info['gender_input'],
                         player_info['ranking_input']))
        player.insert()

    @staticmethod
    def create_tournament():
        """
        create_tournament()
        Create a new tournament by calling the function create_tournament()
        inside TournamentView class and giving the acquired values to Tournament
        class.
        """
        if len(Player().retrieve_all()) >= 8:
            tournament_info = (TournamentView
                               .create_tournament(Player().retrieve_all()))
            tournament = (Tournament(tournament_info["name_input"],
                                     tournament_info["place_input"],
                                     tournament_info["start_date_input"],
                                     tournament_info["end_date_input"],
                                     tournament_info["players_input"],
                                     tournament_info["time_control_input"],
                                     tournament_info["description_input"]))
            tournament.insert()
        else:
            ErrorHandlerView.display_error("Not enough players have been created. Please, add at least 8 players.")
