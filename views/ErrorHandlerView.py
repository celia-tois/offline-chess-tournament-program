import re


class ErrorHandlerView:

    @staticmethod
    def display_error(error):
        print(error)

    @staticmethod
    def is_an_int(message):
        while True:
            user_input = input(message)
            if re.match(r'^[0-9]*$', user_input):
                return user_input
            print("Wrong format.")

    @staticmethod
    def is_a_string(message):
        while True:
            user_input = input(message)
            if re.match(r'^\D*$', user_input):
                return user_input
            print("Wrong format.")

    @staticmethod
    def is_a_date(message):
        while True:
            user_input = input(message)
            if re.match(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$', user_input):
                return user_input
            print("Wrong format.")

    @staticmethod
    def gender(message):
        while True:
            user_input = input(message)
            if re.match(r'^F', user_input) or re.match(r'^M', user_input):
                return user_input
            print("Wrong format.")


