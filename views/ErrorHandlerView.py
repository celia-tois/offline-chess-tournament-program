import re


class ErrorHandlerView:
    """ErrorHandlerView class"""

    @staticmethod
    def display_error(error):
        """
        display_error()
        Display an error message.
        :arg: error message
        """
        print(error)

    @staticmethod
    def is_an_int(message):
        """
        is_an_int()
        Check if the user input is an integer.
        :arg: user input
        :rtype: str
        :return: user input
        """
        while True:
            user_input = input(message)
            if re.match(r'^[0-9]*$', user_input):
                return user_input
            print("Wrong format.")

    @staticmethod
    def is_a_string(message):
        """
        is_a_string()
        Check if the user input is a string.
        :arg: user input
        :rtype: str
        :return: user input
        """
        while True:
            user_input = input(message)
            if re.match(r'^\D*$', user_input):
                return user_input
            print("Wrong format.")

    @staticmethod
    def is_a_date(message):
        """
        is_a_date()
        Check if the user input is a date.
        :arg: user input
        :rtype: str
        :return: user input
        """
        while True:
            user_input = input(message)
            if re.match(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$', user_input):
                return user_input
            print("Wrong format.")

    @staticmethod
    def gender(message):
        """
        gender()
        Check if the user input is a "F" or "M".
        :arg: user input
        :rtype: str
        :return: user input
        """
        while True:
            user_input = input(message)
            if re.match(r'^F', user_input) or re.match(r'^M', user_input):
                return user_input
            print("Wrong format.")

    @staticmethod
    def time_control(message):
        """
        time_control()
        Check if the user input is a "bullet", "blitz" or "coup rapide".
        :arg: user input
        :rtype: str
        :return: user input
        """
        while True:
            user_input = input(message)
            if re.match(r'^bullet', user_input)\
                    or re.match(r'^blitz', user_input)\
                    or re.match(r'^coup rapide', user_input):
                return user_input
            print("Wrong format.")

    @staticmethod
    def match_result(message):
        """
        match_result()
        Check if the user input is a "0", "1" or "2".
        :arg: user input
        :rtype: str
        :return: user input
        """
        while True:
            user_input = input(message)
            if user_input == "0" or user_input == "1" or user_input == "2":
                return user_input
            print("Wrong format.")
