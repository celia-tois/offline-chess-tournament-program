"""Define the main menu."""

from views.tournamentmenu import TournamentMenu
from views.reportsmenu import ReportsMenu
from views.addplayer import AddPlayer


class MainMenu:
    """MainMenu class"""

    def __init__(self):
        while True:
            print("Menu")
            print("1: Add a player")
            print("2: Create a tournament")
            print("3: Load a tournament")
            print("4: Modify the ranking")
            print("5: Reports")
            user_choice = input("Your choice? ")
            if user_choice == "1":
                AddPlayer()
            elif user_choice == "2":
                print("2")
                break
            elif user_choice == "3":
                TournamentMenu()
            elif user_choice == "4":
                print("4")
                break
            elif user_choice == "5":
                ReportsMenu()
            else:
                print("Invalid choice, please enter a correct option.")
