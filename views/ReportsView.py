"""Define the reports menu."""
from prettytable import PrettyTable


class ReportsView:
    """ReportsMenu class"""

    @staticmethod
    def display_reports_menu():
        print("Reports menu")
        print("1: List of the actors")
        print("2: List of the tournament's players")
        print("3: List of the tournaments")
        print("4: List of the rounds of a tournament")
        print("5: List of the matches of a tournament")
        print("q: Return to the main menu")
        user_choice = input("Your choice? ")
        return user_choice

    @staticmethod
    def display_table_option(table):
        print("Display players by:")
        print("1: alphabetical order")
        print("2: ranking")
        user_choice = input("Your choice: ")
        if user_choice == str(1):
            print(table.get_string(sortby="last_name"))
        elif user_choice == str(2):
            print(table.get_string(sortby="ranking", reversesort=True))

    @staticmethod
    def display_table(data):
        table = PrettyTable()
        table.field_names = [attr for attr, value in data[0].__dict__.items() if not attr == "table"]
        for info in data:
            table.add_row([value for attr, value in info.__dict__.items() if not attr == "table"])
        return table

    @staticmethod
    def display_players(data):
        ReportsView.display_table_option(ReportsView.display_table(data))

    @staticmethod
    def display_tournament_players(data):
        table = PrettyTable()
        players = [value for attr, value in data.__dict__.items() if attr == "players"][0]
        table.field_names = [attr for attr in players[0]]
        for player in players:
            table.add_row([value for attr, value in player.items()])
        ReportsView.display_table_option(table)

    @staticmethod
    def display_tournaments(data):
        table = ReportsView.display_table(data)
        print(table.get_string(fields=["name", "place", "start_date", "end_date", "time_control", "description"]))

    @staticmethod
    def display_rounds(data):
        table = PrettyTable()
        rounds = [value for attr, value in data.__dict__.items() if attr == "rounds"][0]
        table.field_names = [attr for attr in rounds[0]]
        for round in rounds:
            table.add_row([value for attr, value in round.items()])
        print(table.get_string(fields=["name", "start_date"]))

    @staticmethod
    def display_matches(data):
        table = PrettyTable()
        rounds = [value for attr, value in data.__dict__.items() if attr == "rounds"][0]
        option = 1
        for round in rounds:
            print(f"{option}: {round['name']}")
            option += 1
        user_choice = input("Round: ")
        table.field_names = ["player_1_name", "player_1_score", "player_2_name", "player_2_score"]
        matches = [round for round in rounds if user_choice in round['name']][0]['matches']
        for match in matches:
            player_1_name = ""
            player_2_name = ""
            player_1_score = match[0][1]
            player_2_score = match[1][1]
            for info in match[0][0]:
                player_1_name = f"{info['first_name']} {info['last_name']}"
            for info in match[1][0]:
                player_2_name = f"{info['first_name']} {info['last_name']}"
            table.add_row([player_1_name, player_1_score, player_2_name, player_2_score])
        print(table)


