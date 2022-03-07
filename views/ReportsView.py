"""Define the reports menu."""
from prettytable import PrettyTable
from views.ErrorHandlerView import ErrorHandlerView


class ReportsView:
    """ReportsMenu class"""

    @staticmethod
    def display_reports_menu():
        """
        display_reports_menu()
        Display reports menu options and an input.
        :rtype: str
        :return: user choice
        """
        print("Reports menu")
        print("1: List of the actors")
        print("2: List of the tournament's players")
        print("3: List of the tournaments")
        print("4: List of the rounds of a tournament")
        print("5: List of the matches of a tournament")
        print("q: Return to the main menu")
        while True:
            user_choice = input("Your choice? ")
            if user_choice <= "5" or user_choice == "q":
                return user_choice
            else:
                ErrorHandlerView.display_error("Wrong option entered.")

    @staticmethod
    def display_table_option(table):
        """
        display_table_option()
        Display table options for the user to choose in which way
        the table will be displayed and an input.
        :arg: table
        :rtype: str
        :return: user choice
        """
        print("Display players by:")
        print("1: alphabetical order")
        print("2: ranking")
        while True:
            user_choice = input("Your choice: ")
            if user_choice == str(1):
                print(table.get_string(sortby="last_name"))
                break
            elif user_choice == str(2):
                print(table.get_string(sortby="ranking", reversesort=True))
                break
            else:
                ErrorHandlerView.display_error("Wrong option entered.")

    @staticmethod
    def display_players(data):
        """
        display_players()
        Display the players table.
        :arg: players to display
        :rtype: PrettyTable
        :return: table
        """
        table = PrettyTable()
        table.field_names = [attr for attr, value in data[0].__dict__.items()
                             if not attr == "table"]
        for info in data:
            table.add_row([value for attr, value in info.__dict__.items()
                           if not attr == "table"])
        ReportsView.display_table_option(table)

    @staticmethod
    def display_tournaments(data):
        """
        display_tournaments()
        Display the tournaments table.
        :arg: tournaments to display
        :rtype: PrettyTable
        :return: table
        """
        table = PrettyTable()
        table.field_names = [attr for attr, value in data[0].__dict__.items()
                             if not attr == "table" if not attr == "rounds" if not attr == "number_rounds" if
                             not attr == "players"]
        for info in data:
            table.add_row([value for attr, value in info.__dict__.items()
                           if not attr == "table" if not attr == "rounds" if not attr == "number_rounds" if
                           not attr == "players"])

        print(table)

    @staticmethod
    def display_rounds(data):
        """
        display_rounds()
        Call the display_table_option() function to display the table.
        :arg: rounds to display
        :rtype: PrettyTable
        :return: table
        """
        table = PrettyTable()
        rounds = [value for attr, value in data.__dict__.items()
                  if attr == "rounds"][0]
        if len(rounds) > 0:
            table.field_names = [attr for attr, value in rounds[0].__dict__.items()]
            for round in rounds:
                table.add_row([value for attr, value in round.__dict__.items()])
            print(table.get_string(fields=["name", "start_date"]))
        else:
            ErrorHandlerView.display_error("There is no round to display. Please choose another tournament.")

    @staticmethod
    def display_matches(data):
        """
        display_matches()
        Call the display_table_option() function to display the table.
        :arg: matches to display
        :rtype: PrettyTable
        :return: table
        """
        table = PrettyTable()
        rounds = [value for attr, value in data.__dict__.items()
                  if attr == "rounds"][0]
        if len(rounds) > 0:
            option = 1
            for round in rounds:
                print(f"{option}: {round.name}")
                option += 1
            while True:
                user_choice = input("Round: ")
                if user_choice <= str(len(rounds)):
                    table.field_names = ["player_1_name",
                                         "player_1_score",
                                         "player_2_name",
                                         "player_2_score"]
                    round_selected = [round for round in rounds if user_choice in round.name][0]
                    matches = [value for attr, value in round_selected.__dict__.items() if attr == "matches"]
                    for match in matches[0]:
                        print(match[0][0].first_name)
                        player_1_name = f"{match[0][0].first_name} {match[0][0].last_name}"
                        player_2_name = f"{match[1][0].first_name} {match[1][0].last_name}"
                        player_1_score = match[0][1]
                        player_2_score = match[1][1]
                        table.add_row(
                            [player_1_name, player_1_score, player_2_name, player_2_score])
                    print(table)
                    break
                else:
                    ErrorHandlerView.display_error("Wrong option entered.")
        else:
            ErrorHandlerView.display_error("There is no round to display. Please choose another tournament.")
