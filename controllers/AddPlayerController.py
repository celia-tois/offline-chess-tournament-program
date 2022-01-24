from views.AddPlayerView import AddPlayerView
w
from models.Player import Player


class AddPlayerController:
    def __init__(self):
        player_info = AddPlayerView.player()
        player = Player(player_info['last_name_input'], player_info['first_name_input'], player_info['date_of_birth_input'], player_info['gender_input'], player_info['ranking_input'])
        player.insert()
