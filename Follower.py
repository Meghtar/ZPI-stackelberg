from Player import Player

class Follower(Player):
    def create_new_strategy(self):
        self.strategy = [0,0,0,0,0]