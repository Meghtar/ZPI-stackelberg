from Player import Player

class Leader(Player):
    def create_new_strategy(self):
        # assumption: defender wants only minimize his costs/ maximize gains
        # he doesn't care about attacker point of view
        # TODO: second strategy would also like to maximize attackers' costs
        
        if len(self.previous_rounds) != 0:
            self.strategy = self.previous_rounds[-1]['opponent_strategy']
        # else:
        self.strategy = [0,0,1,0,0]