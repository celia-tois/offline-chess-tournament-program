from views.ErrorHandlerView import ErrorHandlerView


class TournamentView:
    """CreateTournament class"""

    @staticmethod
    def create_tournament(players_to_display):
        print("Create a tournament:")
        data = dict()
        data["name_input"] = ErrorHandlerView.is_a_string("Name: ")
        data["place_input"] = ErrorHandlerView.is_a_string("Place: ")
        data["start_date_input"] = ErrorHandlerView.is_a_date("Start date (DD/MM/YYYY): ")
        data["end_date_input"] = ErrorHandlerView.is_a_date("End date (DD/MM/YYYY): ")
        data["players_input"] = (TournamentView
                                 .display_players(players_to_display))
        data["time_control_input"] = input(
            "Time control (bullet, blitz, coup rapide): ")
        data["description_input"] = ErrorHandlerView.is_a_string("Description: ")
        return data

    @staticmethod
    def display_players(players_to_display):
        """
        display_players()
        Display all the players and return a list of the players
        selected by the user.
        :rtype: list of objects
        :return: selected players
        """
        players_selected = []
        while len(players_selected) < 8:
            for player in players_to_display:
                print(player)
            while True:
                players_input = input("Player: ")
                for player in players_to_display:
                    if int(players_input) == player.id:
                        players_selected.append(player)
                        players_to_display.remove(player)
                    ErrorHandlerView.display_error("Wrong option entered.")
        return players_selected

    @staticmethod
    def select_tournament(tournaments_to_display):
        """
        select_tournament()
        Display all the tournaments and return the tournament
        selected by the user.
        :rtype: str
        :return: selected tournament
        """
        print("Select a tournament:")
        for tournament in tournaments_to_display:
            print(tournament)
        tournament_input = input("Tournament: ")
        for tournament in tournaments_to_display:
            tournament_id = [value for attr, value
                             in tournament.__dict__.items()if attr == "id"][0]
            if int(tournament_input) == tournament_id:
                return tournament

    @staticmethod
    def enter_match_result(match):
        print("Select the winner:")
        print("0: equality")
        option = 1
        for player in match:
            print(f"{option}: {player[0]['first_name']} "
                  f"{player[0]['last_name']}")
            option += 1
        winner = input("Winner: ")
        return winner
