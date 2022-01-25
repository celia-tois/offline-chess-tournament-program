from views.TournamentMenuView import TournamentMenuView
from views.MainMenuView import MainMenuView
from controllers.launchround import LaunchRound
from controllers.endround import EndRound


class TournamentMenuController:
    def __init__(self, tournament):
        while True:
            user_choice = TournamentMenuView()
            if user_choice == "1":
                LaunchRound()
            elif user_choice == "2":
                EndRound()
            elif user_choice == "q":
                MainMenuView()
            else:
                print("Invalid choice, please enter a correct option.")