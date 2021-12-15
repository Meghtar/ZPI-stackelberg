from Player import Player
import random

class Leader(Player):
    def create_new_strategy(self):
        # programmer shall change strategy here
        self.strategy0()
        # self.strategy = [1,1,1,1,1]

    def strategy0(self):
        # strategy 0: 
        # just selecting random bits
        rnd = '00000'
        while rnd == '00000':
            rnd = format(random.getrandbits(5), '05b')

        res = [int(i) for i in list(rnd)]
        # print('random: {}, res: {}'.format(rnd, res))
        self.strategy = res
    
    def strategy1(self):
        ### strategy 1:
        # simply randomly switching bits of best strategy, and willing to find best strategy this way 

        # get the best strat so far
        # modify 1 bit

        if len(self.previous_rounds) == 0:
            return

        best_strat = []
        best_payoff = -9999

        for round in self.previous_rounds:
            if round['payoff'] > best_payoff:
                best_payoff = round['payoff']
                best_strat = round['strategy']
        
        place_to_switch = random.randint(0,4)

        # print('+++++')
        # print('best strat so far: {}'.format(best_strat))

        best_strat[place_to_switch] = 1 - best_strat[place_to_switch]

        # print('best strat after switch: {}'.format(best_strat))
        # print('+++++')
        self.strategy = best_strat

    def strategy2(self):
        pass

    def strategy3(self):
        pass
