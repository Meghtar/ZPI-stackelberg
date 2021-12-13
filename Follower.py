from Player import Player

class Follower(Player):
    def create_new_strategy(self):
        self.strategy = [1,1,1,0,1]