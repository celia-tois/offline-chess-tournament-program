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
            if user_choice <= "5":
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
    def display_table(data):
        """
        display_table()
        Display the table.
        :arg: data to display
        :rtype: PrettyTable
        :return: table
        """
        table = PrettyTable()
        table.field_names = [attr for attr, value in data[0].__dict__.items()
                             if not attr == "table"]
        for info in data:
            table.add_row([value for attr, value in info.__dict__.items()
                           if not attr == "table"])
        return table

    @staticmethod
    def display_players(data):
        """
        display_players()
        Call the display_table_option() function to display the table.
        :arg: players to display
        :rtype: PrettyTable
        :return: table
        """
        ReportsView.display_table_option(ReportsView.display_table(data))

    @staticmethod
    def display_tournaments(data):
        """
        display_tournaments()
        Call the display_table_option() function to display the table.
        :arg: tournaments to display
        :rtype: PrettyTable
        :return: table
        """
        table = ReportsView.display_table(data)
        print(table.get_string(fields=["name",
                                       "place",
                                       "start_date",
                                       "end_date",
                                       "time_control",
                                       "description"]))

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
        table.field_names = [attr for attr in rounds[0]]
        for round in rounds:
            table.add_row([value for attr, value in round.items()])
        print(table.get_string(fields=["name", "start_date"]))

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
        option = 1
        for round in rounds:
            print(f"{option}: {round['name']}")
            option += 1
        while True:
            user_choice = input("Round: ")
            if user_choice <= str(len(rounds)):
                table.field_names = ["player_1_name",
                                     "player_1_score",
                                     "player_2_name",
                                     "player_2_score"]
                matches = [round for round in rounds
                           if user_choice in round['name']][0]['matches']
                for match in matches:
                    player_1_name = ""
                    player_2_name = ""
                    player_1_score = match[0][1]
                    player_2_score = match[1][1]
                    for info in match[0][0]:
                        player_1_name = f"{info['first_name']} {info['last_name']}"
                    for info in match[1][0]:
                        player_2_name = f"{info['first_name']} {info['last_name']}"
                    table.add_row(
                        [player_1_name, player_1_score, player_2_name, player_2_score])
                print(table)
                break
            else:
                ErrorHandlerView.display_error("Wrong option entered.")
