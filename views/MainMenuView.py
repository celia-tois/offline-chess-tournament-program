"""Define the main menu."""


class MainMenuView:
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

