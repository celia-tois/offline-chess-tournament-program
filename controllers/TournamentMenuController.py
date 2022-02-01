from views.MenuView import MenuView
from views.TournamentView import TournamentView
from models.Round import Round
from models.Tournament import Tournament
from datetime import datetime

from views.enterplayersresult import EnterPlayersResult


class TournamentMenuController:
    def __init__(self):
        self.tournament = TournamentView.select_tournament(Tournament().retrieve_all())
        user_choice = MenuView.display_tournament_menu()
        if user_choice == "1":
            TournamentMenuController.launch_round(self)
        elif user_choice == "2":
            TournamentMenuController.end_round()
        elif user_choice == "q":
            MenuView()
        else:
            print("Invalid choice, please enter a correct option.")

    def launch_round(self):
        self.tournament['rounds'] = Round().serialize()
        self.tournament.update()
        TournamentMenuController.first_players_pairing(self)
        # print("round", Round().serialize())
        # print("updated", self.tournament)

    @staticmethod
    def end_round():
        end_date = datetime.now().time().isoformat(timespec='minutes')
        round_ended = Round(end_date=end_date)
        round_ended.insert()
        # EnterPlayersResult(end_time=end_time)

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
            players_pairs.append([player, second_half[player_to_match]])
            player_to_match += 1
        return players_pairs

