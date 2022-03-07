from views.MenuView import MenuView
from views.ErrorHandlerView import ErrorHandlerView
from models.Player import Player
from models.Tournament import Tournament
from controllers.ReportsController import ReportsController
from controllers.Controller import Controller
from controllers.TournamentMenuController import TournamentMenuController


class MainMenuController:
    """MainMenuController class"""

    def __init__(self):
        """
        __init__()
        Redirect the user to the option selected.
        """
        while True:
            user_choice = MenuView.display_main_menu()
            if user_choice == "1":
                Controller.add_player()
            elif user_choice == "2":
                Controller.create_tournament()
            elif user_choice == "3":
                TournamentMenuController()
            elif user_choice == "4":
                MenuView.modify_ranking(Player().retrieve_all())
            elif user_choice == "5":
                ReportsController()
            else:
                print("Invalid choice, please enter a correct option.")
