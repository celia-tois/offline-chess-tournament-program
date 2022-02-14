from views.MenuView import MenuView
from views.TournamentView import TournamentView
from models.Round import Round
from models.Tournament import Tournament
from datetime import datetime


class TournamentMenuController:
    def __init__(self):
        self.tournament = TournamentView.select_tournament(Tournament().retrieve_all())
        user_choice = MenuView.display_tournament_menu()
        if user_choice == "1":
            TournamentMenuController.launch_round(self)
        elif user_choice == "2":
            TournamentMenuController.end_round(self)
        elif user_choice == "q":
            MenuView().display_main_menu()
        else:
            print("Invalid choice, please enter a correct option.")

    def launch_round(self):
        if len(self.tournament.rounds) == 0 or "end_date" in self.tournament.rounds[-1]:
            new_round = Round(self.tournament.rounds).serialize()
            if len(self.tournament.rounds) == 0:
                new_round["matches"] = TournamentMenuController.first_players_pairing(self)
            else:
                new_round["matches"] = TournamentMenuController.others_players_pairing(self)
            self.tournament.rounds.append(new_round)
            self.tournament.update()
        else:
            print("You have to end the previous round before launching a new one.")

    def end_round(self):
        new_round = self.tournament.rounds[-1]
        new_round["end_date"] = datetime.now().isoformat(timespec='minutes')
        players_pairs_updated = []
        for match in new_round["matches"]:
            winner = TournamentView.enter_match_result(match)
            if int(winner) == 0:
                players_pairs_updated.append(([match[0], 0.5], [match[1], 0.5]))
            elif int(winner) == 1:
                players_pairs_updated.append(([match[0], 1], [match[1], 0]))
            elif int(winner) == 2:
                players_pairs_updated.append(([match[0], 0], [match[1], 1]))
        new_round["matches"] = players_pairs_updated
        for match in players_pairs_updated:
            for player in match:
                for tournament_player in self.tournament.players:
                    if player[0][0]["id"] == tournament_player["id"]:
                        tournament_player["score"] += player[1]
        self.tournament.update()

    def sort_players_by_rank(self):
        def sort_by_rank(player):
            return player.get('ranking')
        players = self.tournament.players
        sorted_players = sorted(players, key=sort_by_rank)
        return sorted_players

    def sort_players_by_score(self):
        def sort_by_score(player):
            return player.get('score')
        players = self.tournament.players
        sorted_players = sorted(players, key=sort_by_score, reverse=True)
        return sorted_players

    def first_players_pairing(self):
        players = TournamentMenuController.sort_players_by_rank(self)
        first_half = players[:4]
        second_half = players[4:8]
        players_pairs = []
        player_to_match = 0
        for player in first_half:
            players_pairs.append(([player], [second_half[player_to_match]]))
            player_to_match += 1
        return players_pairs

    def others_players_pairing(self):
        players = TournamentMenuController.sort_players_by_score(self)
        players_pairs = [
            ([players[0]], [players[1]]),
            ([players[2]], [players[3]]),
            ([players[4]], [players[5]]),
            ([players[6]], [players[7]])]
        return players_pairs
