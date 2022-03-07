from views.ReportsView import ReportsView
from views.TournamentView import TournamentView
from views.ErrorHandlerView import ErrorHandlerView
from models.Player import Player
from models.Tournament import Tournament


class ReportsController:
    """ReportsController class"""

    def __init__(self):
        """
        __init__()
        Redirect the user to the option selected.
        """
        while True:
            user_choice = ReportsView.display_reports_menu()
            if user_choice == "1":
                if len(Player().retrieve_all()) > 0:
                    ReportsView().display_players(Player().retrieve_all())
                else:
                    ErrorHandlerView.display_error(
                        "No players have been created. Please, create at least 1 player.")
            elif user_choice == "2":
                if len(Tournament().retrieve_all()) > 0:
                    ReportsView().display_players(
                        TournamentView.select_tournament(
                            Tournament().retrieve_all()).players)
                else:
                    ErrorHandlerView.display_error(
                        "No tournaments have been created. Please, create at least 1 tournament.")
            elif user_choice == "3":
                if len(Tournament().retrieve_all()) > 0:
                    ReportsView().display_tournaments(Tournament().retrieve_all())
                else:
                    ErrorHandlerView.display_error(
                        "No tournaments have been created. Please, create at least 1 tournament.")
            elif user_choice == "4":
                if len(Tournament().retrieve_all()) > 0:
                    ReportsView().display_rounds(TournamentView.select_tournament(
                        Tournament().retrieve_all()))
                else:
                    ErrorHandlerView.display_error(
                        "No tournaments have been created. Please, create at least 1 tournament.")
            elif user_choice == "5":
                if len(Tournament().retrieve_all()) > 0:
                    ReportsView().display_matches(TournamentView.select_tournament(
                        Tournament().retrieve_all()))
                else:
                    ErrorHandlerView.display_error(
                        "No tournaments have been created. Please, create at least 1 tournament.")
            elif user_choice == "q":
                break
            else:
                print("Invalid choice, please enter a correct option.")
