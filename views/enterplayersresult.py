from models.Round import Round


class EnterPlayersResult:
    def __init__(self):
        print("Enter results:")
        first_match = input("First match: ")
        second_match = input("Second match: ")
        third_match = input("Third match: ")
        fourth_match = input("Fourth match: ")
        results = [first_match, second_match, third_match, fourth_match]

        Round(results=results)
