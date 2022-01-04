"""Define the tournament menu"""

import views.mainmenu as menu


class TournamentMenu:
    """TournamentMenu class"""

    def __init__(self):
        while True:
            print("Load a tournament:")
            print("1: Launch a round")
            print("2: End a round")
            print("q: Return to the main menu")
            user_choice = input("Your choice? ")
            if user_choice == "1":
                print("1")
                break
            elif user_choice == "2":
                print("2")
                break
            elif user_choice == "q":
                menu.MainMenu()
            else:
                print("Invalid choice, please enter a correct option.")