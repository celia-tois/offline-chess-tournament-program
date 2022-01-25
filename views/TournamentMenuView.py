"""Define the tournament menu"""


class TournamentMenuView:
    """TournamentMenu class"""

    def __init__(self):
        print("Load a tournament:")
        print("1: Launch a round")
        print("2: End a round")
        print("q: Return to the main menu")
        user_choice = input("Your choice? ")
        return user_choice
