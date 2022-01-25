"""Define the reports menu."""

from views.MenuView import MenuView


class ReportsMenu:
    """ReportsMenu class"""

    def __init__(self):
        while True:
            print("Reports menu")
            print("1: List of the actors")
            print("2: List of the tournament's players")
            print("3: List of the tournaments")
            print("4: List of the rounds of a tournament")
            print("5: List of the matches of a tournament")
            print("q: Return to the main menu")
            user_choice = input("Your choice? ")
            if user_choice == "1":
                print("1")
                break
            elif user_choice == "2":
                print("2")
                break
            elif user_choice == "3":
                print("3")
                break
            elif user_choice == "4":
                print("4")
                break
            elif user_choice == "5":
                print("5")
                break
            elif user_choice == "q":
                MenuView()
            else:
                print("Invalid choice, please enter a correct option.")
