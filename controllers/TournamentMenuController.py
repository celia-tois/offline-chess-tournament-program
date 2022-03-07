from views.MenuView import MenuView
from views.TournamentView import TournamentView
from views.ErrorHandlerView import ErrorHandlerView
from models.Round import Round
from models.Tournament import Tournament
from datetime import datetime


class TournamentMenuController:
    """TournamentMenuController class"""

    def __init__(self):
        """
        __init__()
        Redirect the user to the option selected.
        """
        if len(Tournament().retrieve_all()) > 0:
            self.tournament = (TournamentView
                               .select_tournament(Tournament().retrieve_all()))
            while True:
                user_choice = MenuView.display_tournament_menu()
                if user_choice == "1":
                    TournamentMenuController.launch_round(self)
                elif user_choice == "2":
                    TournamentMenuController.end_round(self)
                elif user_choice == "q":
                    break
                else:
                    print("Invalid choice, please enter a correct option.")
        else:
            ErrorHandlerView.display_error("No tournaments have been created. Please, create at least 1 tournament.")

    def launch_round(self):
        """
        launch_round()
        Launch a new round if the previous round has ended.
        """
        if len(self.tournament.rounds) < 4:
            if len(self.tournament.rounds) == 0 or self.tournament.rounds[-1].end_date is not None:
                new_round = Round(self.tournament.rounds)
                if len(self.tournament.rounds) == 0:
                    new_round.matches = TournamentMenuController.first_players_pairing(self)
                else:
                    new_round.matches = TournamentMenuController.others_players_pairing(self)
                self.tournament.rounds.append(new_round)
                self.tournament.update()
                print("A round has been launched.")
            else:
                ErrorHandlerView.display_error("You have to end the previous round before launching a new one.")
        else:
            ErrorHandlerView.display_error("You have already launched 4 rounds. This tournament has ended.")

    def end_round(self):
        """
        end_round()
        End the round by adding the end_date value and the result of each match,
        as the user entered them.
        """
        if (len(self.tournament.rounds) == 0
                or self.tournament.rounds[-1].end_date is None):
            new_round = self.tournament.rounds[-1]
            new_round.end_date = datetime.now().isoformat(timespec='minutes')
            for match in new_round.matches:
                result = TournamentView.enter_match_result(match)
                if int(result) == 0:
                    match[0][1] = 0.5
                    match[1][1] = 0.5
                elif int(result) == 1:
                    match[0][1] = 1
                    match[1][1] = 0
                elif int(result) == 2:
                    match[0][1] = 0
                    match[1][1] = 1
                for player in match:
                    for tournament_player in self.tournament.players:
                        if player[0].id == tournament_player.id:
                            tournament_player.score += player[1]
            self.tournament.update()
            print("The round has ended.")
        else:
            ErrorHandlerView.display_error("You have to launch a round before ending one.")

    def sort_players_by_rank(self):
        """
        sort_players_by_rank()
        Sort the players from a tournament by their ranking.
        :rtype: list
        :return: list of sorted players
        """
        players = self.tournament.players
        sorted_players = sorted(players, key=lambda x: int(x.ranking), reverse=True)
        return sorted_players

    def sort_players_by_score_and_rank(self):
        """
        sort_players_by_score_and_rank()
        Sort the players from a tournament by their score then by their ranking.
        :rtype: list
        :return: list of sorted players
        """
        players = self.tournament.players
        sorted_players = sorted(players,
                                key=lambda x: (x.score, x.ranking), reverse=True)
        return sorted_players

    def first_players_pairing(self):
        """
        first_players_pairing()
        Pair the players for the matches of the first round.
        :rtype: list
        :return: list of tuple of pair of players
        """
        players = TournamentMenuController.sort_players_by_rank(self)
        players_pairs = [
            ([players[0], -1], [players[4], -1]),
            ([players[1], -1], [players[5], -1]),
            ([players[2], -1], [players[6], -1]),
            ([players[3], -1], [players[7], -1])]
        return players_pairs

    def others_players_pairing(self):
        """
        others_players_pairing()
        Pair the players for the matches after the first round.
        :rtype: list
        :return: list of tuple of pair of players
        """
        players = TournamentMenuController.sort_players_by_score_and_rank(self)
        players_pairs = [
            ([players[0], -1], [players[1], -1]),
            ([players[2], -1], [players[3], -1]),
            ([players[4], -1], [players[5], -1]),
            ([players[6], -1], [players[7], -1])]
        for round in self.tournament.rounds:
            first_player_id = round.matches[0][0][0].id
            second_player_id = round.matches[0][1][0].id
            if first_player_id == players[0].id or first_player_id == players[1].id:
                if second_player_id == players[0].id or second_player_id == players[1].id:
                    players_pairs = [
                        ([players[0], -1], [players[2], -1]),
                        ([players[1], -1], [players[3], -1]),
                        ([players[4], -1], [players[5], -1]),
                        ([players[6], -1], [players[7], -1])
                    ]
        return players_pairs
