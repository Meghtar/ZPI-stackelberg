from Player import Player

class Leader(Player):
    def create_new_strategy(self):
        if len(self.previous_rounds) != 0:
            self.strategy = self.previous_rounds[-1]['opponent_strategy']
        # else:
        self.strategy = [0,0,1,0,0]