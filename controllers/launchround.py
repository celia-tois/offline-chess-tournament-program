from controllers.pairgeneration import PairGeneration
from models.Round import Round
from datetime import datetime


class LaunchRound:
    def __init__(self):
        start_time = datetime.now().time()
        Round(start_time= start_time)
        PairGeneration()
