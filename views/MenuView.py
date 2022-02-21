from views.ErrorHandlerView import ErrorHandlerView

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
        while True:
            user_choice = input("Your choice? ")
            if user_choice <= "5":
                return user_choice
            ErrorHandlerView.display_error("Wrong option entered.")

    @staticmethod
    def display_tournament_menu():
        print("Load a tournament:")
        print("1: Launch a round")
        print("2: End a round")
        print("q: Return to the main menu")
        while True:
            user_choice = input("Your choice? ")
            if user_choice <= "2" or user_choice == "q":
                return user_choice
            ErrorHandlerView.display_error("Wrong option entered.")

    @staticmethod
    def display_players(players_to_display):
        for player in players_to_display:
            print(player)
        while True:
            players_input = input("Player: ")
            for player in players_to_display:
                if players_input == str(player.id):
                    return player
            ErrorHandlerView.display_error("Wrong option entered.")

    @staticmethod
    def modify_ranking(players_to_display):
        player_selected = MenuView.display_players(players_to_display)
        new_ranking = ErrorHandlerView.is_an_int(f"Enter {player_selected.first_name} "
                                                 f"{player_selected.last_name} ranking: ")
        for player in players_to_display:
            if player_selected.id == player.id:
                player.ranking = int(new_ranking)
            player.update()
