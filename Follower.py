from Player import Player
import random

class Follower(Player):
    def create_new_strategy(self):
        # temporary random strategy each time
        rnd = format(random.getrandbits(5), '05b')
        res = [int(i) for i in list(rnd)]
        print('random: {}, res: {}'.format(rnd, res))
        self.strategy = res
        # self.strategy = [1,1,1,0,1]