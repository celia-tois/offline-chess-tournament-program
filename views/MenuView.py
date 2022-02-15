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

    @staticmethod
    def display_players(players_to_display):
        for player in players_to_display:
            print(f"{player['id']}: {player['first_name']} {player['last_name']}")
        players_input = input("Player: ")
        for player in players_to_display:
            if int(players_input) == player['id']:
                player_selected = player
        return player_selected

    @staticmethod
    def modify_ranking(players_to_display):
        player_selected = MenuView.display_players(players_to_display)
        new_ranking = input(f"Enter {player_selected['first_name']} {player_selected['last_name']} ranking: ")
        for player in players_to_display:
            if player_selected["id"] == player["id"]:
                player["ranking"] = int(new_ranking)
            print(player)
        print(players_to_display)

