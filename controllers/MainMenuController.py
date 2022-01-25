from views.MenuView import MenuView
from views.ReportsMenuView import ReportsMenu
from controllers.Controller import Controller


class MainMenuManager:
    def __init__(self):
        while True:
            user_choice = MenuView.display_main_menu()
            if user_choice == "1":
                Controller.add_player()
            elif user_choice == "2":
                Controller.create_tournament()
            elif user_choice == "3":
                MenuView.display_tournament_menu()
            elif user_choice == "4":
                print("4")
                break
            elif user_choice == "5":
                ReportsMenu()
            else:
                print("Invalid choice, please enter a correct option.")
