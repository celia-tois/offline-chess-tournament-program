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
    def display_table(data):
        field_names = []
        table = PrettyTable()
        for key in data[0]:
            field_names.append(key)
        table.field_names = field_names
        for info in data:
            data_values = []
            for key, value in info.items():
                data_values.append(value)
            table.add_row(data_values)
        print(table)
