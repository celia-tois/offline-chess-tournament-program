from views.ErrorHandlerView import ErrorHandlerView


class PlayerView:
    """AddPlayer class"""

    @staticmethod
    def player():
        print("Add a player:")
        data = dict()
        data["last_name_input"] = ErrorHandlerView.is_a_string("Last name: ")
        data["first_name_input"] = ErrorHandlerView.is_a_string("First name: ")
        data["date_of_birth_input"] = ErrorHandlerView.is_a_date("Date of birth (DD/MM/YYYY): ")
        data["gender_input"] = ErrorHandlerView.gender("Gender (F/M): ")
        data["ranking_input"] = ErrorHandlerView.is_an_int("Ranking: ")
        return data
