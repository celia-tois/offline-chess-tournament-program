from views.ErrorHandlerView import ErrorHandlerView


class TournamentView:
    """CreateTournament class"""

    @staticmethod
    def create_tournament(players_to_display):
        """
        create_tournament()
        Display inputs so that the user enter new tournament' information.
        :arg: list of players to display
        :rtype: dict
        :return: new tournament information
        """
        print("Create a tournament:")
        data = dict()
        data["name_input"] = ErrorHandlerView.is_a_string("Name: ")
        data["place_input"] = ErrorHandlerView.is_a_string("Place: ")
        data["start_date_input"] = ErrorHandlerView.is_a_date("Start date (DD/MM/YYYY): ")
        data["end_date_input"] = ErrorHandlerView.is_a_date("End date (DD/MM/YYYY): ")
        data["players_input"] = (TournamentView
                                 .display_players(players_to_display))
        data["time_control_input"] = ErrorHandlerView.time_control(
            "Time control (bullet, blitz, coup rapide): ")
        data["description_input"] = ErrorHandlerView.is_a_string("Description: ")
        return data

    @staticmethod
    def display_players(players_to_display):
        """
        display_players()
        Display all the players and return a list of the players
        selected by the user.
        :arg: list of players to display
        :rtype: list of objects
        :return: selected players
        """
        players_selected = []
        while len(players_selected) < 8:
            for player in players_to_display:
                print(player)
            while True:
                players_input = input("Player: ")
                player_id = ""
                for player in players_to_display:
                    if players_input == str(player.id):
                        player_id = player.id
                        players_selected.append(player)
                        players_to_display.remove(player)
                if players_input != str(player_id):
                    ErrorHandlerView.display_error("Wrong option entered.")
                else:
                    break
        return players_selected

    @staticmethod
    def select_tournament(tournaments_to_display):
        """
        select_tournament()
        Display all the tournaments and return the tournament
        selected by the user.
        :arg: list of tournaments to display
        :rtype: class instance
        :return: selected tournament
        """
        print("Select a tournament:")
        for tournament in tournaments_to_display:
            print(tournament)
        while True:
            tournament_input = input("Tournament: ")
            tournament_selected_id = ""
            tournament_selected = ""
            for tournament in tournaments_to_display:
                tournament_id = [value for attr, value
                                 in tournament.__dict__.items()if attr == "id"][0]
                if tournament_input == str(tournament_id):
                    tournament_selected_id = tournament_id
                    tournament_selected = tournament
            if tournament_input != str(tournament_selected_id):
                ErrorHandlerView.display_error("Wrong option entered.")
            else:
                return tournament_selected

    @staticmethod
    def enter_match_result(match):
        """
        enter_match_result()
        Display options and an input so that the user enter the match's winner.
        :arg: match
        :rtype: str
        :return: winner of the match
        """
        print("Select the winner:")
        print("0: equality")
        option = 1
        for player in match:
            print(f"{option}: {player[0]['first_name']} "
                  f"{player[0]['last_name']}")
            option += 1
        winner = ErrorHandlerView.match_result("Winner: ")
        return winner
