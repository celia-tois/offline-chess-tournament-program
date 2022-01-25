from models.Round import Round
from views.enterplayersresult import EnterPlayersResult
from datetime import datetime


class EndRound:
    def __init__(self):
        end_time = datetime.now().time()
        Round(end_time)
        EnterPlayersResult(end_time=end_time)

