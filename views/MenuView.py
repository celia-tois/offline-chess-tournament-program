"""Define the main menu."""


class MenuView:
    """MainMenu class"""

    @staticmethod
    def display_main_menu():
        print("Menu")
        print("1: Add a player")
        print("2: Create a tournament")
        print("3: Load a tournament")
        print("4: Modify the ranking")
        print("5: Reports")
        user_choice = input("Your choice? ")
        return user_choice

    @staticmethod
    def display_tournament_menu():
        print("Load a tournament:")
        print("1: Launch a round")
        print("2: End a round")
        print("q: Return to the main menu")
        user_choice = input("Your choice? ")
        return user_choice
