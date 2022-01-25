class PlayerView:
    """AddPlayer class"""

    @staticmethod
    def player():
        print("Add a player:")
        data = dict()
        data["last_name_input"] = input("Last name: ")
        data["first_name_input"] = input("First name: ")
        data["date_of_birth_input"] = input("Date of birth (DD/MM/YYYY): ")
        data["gender_input"] = input("Gender (F/M): ")
        data["ranking_input"] = input("Ranking: ")
        return data
