from views.MenuView import MenuView
from controllers.launchround import LaunchRound
from controllers.endround import EndRound


class TournamentMenuController:
    def __init__(self, tournament):
        while True:
            user_choice = MenuView.display_tournament_menu()
            if user_choice == "1":
                print("1")
            elif user_choice == "2":
                LaunchRound()
            elif user_choice == "3":
                EndRound()
            elif user_choice == "q":
                MenuView()
            else:
                print("Invalid choice, please enter a correct option.")