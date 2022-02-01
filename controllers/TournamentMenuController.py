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
        new_round = Round().serialize()
        self.tournament['rounds'] = new_round
        self.tournament.update()
        new_round["matches"] = TournamentMenuController.first_players_pairing(self)
        # print("round", Round().serialize())
        # print("updated", self.tournament)

    # def end_round(self):
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
        print(players_pairs_updated)

    def sort_players(self):
        def sort_by_rank(player):
            return player.get('ranking')
        players = self.tournament['players']
        sorted_players = sorted(players, key=sort_by_rank)
        return sorted_players

    def first_players_pairing(self):
        players = TournamentMenuController.sort_players(self)
        first_half = players[:4]
        second_half = players[4:8]
        players_pairs = []
        player_to_match = 0
        for player in first_half:
            players_pairs.append(([player], [second_half[player_to_match]]))
            player_to_match += 1
        return players_pairs
