from views.ReportsView import ReportsView
from views.MenuView import MenuView
from views.TournamentView import TournamentView
from models.Player import Player
from models.Tournament import Tournament


class ReportsController:
    def __init__(self):
        while True:
            user_choice = ReportsView.display_reports_menu()
            if user_choice == "1":
                ReportsView().display_players(Player().retrieve_all())
            elif user_choice == "2":
                ReportsView().display_tournament_players(TournamentView.select_tournament(Tournament().retrieve_all()))
            elif user_choice == "3":
                ReportsView().display_tournaments(Tournament().retrieve_all())
            elif user_choice == "4":
                ReportsView().display_rounds(TournamentView.select_tournament(Tournament().retrieve_all()))
            elif user_choice == "5":
                ReportsView().display_matches(TournamentView.select_tournament(Tournament().retrieve_all()))
            elif user_choice == "q":
                MenuView.display_main_menu()
            else:
                print("Invalid choice, please enter a correct option.")
