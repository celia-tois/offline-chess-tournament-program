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
                ReportsView().display_table(Player().retrieve_all())
            elif user_choice == "2":
                ReportsView().display_table(TournamentView.select_tournament(Tournament().retrieve_all())["players"])
            elif user_choice == "3":
                print("3")
                break
            elif user_choice == "4":
                print("4")
                break
            elif user_choice == "5":
                print("5")
                break
            elif user_choice == "q":
                MenuView.display_main_menu()
            else:
                print("Invalid choice, please enter a correct option.")
