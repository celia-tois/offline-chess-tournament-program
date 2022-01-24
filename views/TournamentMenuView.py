"""Define the tournament menu"""

import views.mainmenu as menu
import controllers.launchround as launchround
import controllers.endround as endround


class TournamentMenu:
    """TournamentMenu class"""

    def __init__(self, tournament):
        while True:
            print("Load a tournament:")
            print("1: Launch a round")
            print("2: End a round")
            print("q: Return to the main menu")
            user_choice = input("Your choice? ")
            if user_choice == "1":
                launchround.LaunchRound()
            elif user_choice == "2":
                endround.EndRound()
            elif user_choice == "q":
                menu.MainMenu()
            else:
                print("Invalid choice, please enter a correct option.")