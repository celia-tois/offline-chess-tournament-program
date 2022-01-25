from views.MainMenuView import MainMenuView
from views.TournamentMenuView import TournamentMenuView
from views.ReportsMenuView import ReportsMenu
from controllers.Controller import Controller
from views.CreateTournamentView import CreateTournamentView


class MainMenuManager:
    def __init__(self):
        while True:
            user_choice = MainMenuView.display_main_menu()
            if user_choice == "1":
                Controller.add_player()
            elif user_choice == "2":
                Controller.create_tournament()
            elif user_choice == "3":
                TournamentMenuView()
            elif user_choice == "4":
                print("4")
                break
            elif user_choice == "5":
                ReportsMenu()
            else:
                print("Invalid choice, please enter a correct option.")
