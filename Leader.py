from Player import Player
import random

class Leader(Player):
    def __init__(self,  gain_and_costs, attack_probabilities, initial_strategy):
        super().__init__(gain_and_costs, attack_probabilities, initial_strategy)

    def create_new_strategy(self):
        # programmer shall change strategy here
        self.strategy2()
    
    def strategy1(self):
        ### strategy 1:
        # simply randomly switching bits of best strategy, and willing to find best strategy this way 
        # get the best strategy so far
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

        best_strat[place_to_switch] = 1 - best_strat[place_to_switch]

        self.strategy = best_strat

    def inc_arr(self, arr):
        res = 1
        mlt = 1
        for e in arr[::-1]:
            res += e * mlt
            mlt <<= 1
        new_arr = []
        new_arr_str = "{0:{fill}5b}".format(res, fill='0')
        for chr in new_arr_str:
            new_arr.append(int(chr))
        return new_arr

    def strategy2(self):
        # strategy 2:
        # calculate which strategy will cost least for leader
        if len(self.previous_rounds) == 0:
            return
        self.inc_arr(self.previous_rounds[len(self.previous_rounds) - 1]['strategy'])
        if len(self.previous_rounds) < 31:
            self.strategy = self.inc_arr(self.previous_rounds[len(self.previous_rounds) - 1]['strategy'])
            return
        best_strat = []
        best_payoff = -9999
        for round in self.previous_rounds:
            if round['payoff'] > best_payoff:
                best_payoff = round['payoff']
                best_strat = round['strategy']
        self.strategy = best_strat

    def strategy3(self):
        # strategy 3:
        # choose most and least expensive countermeasure
        # aggregated cost will be max cost that leader may pay for all countermeasures
        # 
        if len(self.previous_rounds) == 0:
            self.strat3_counter = 0
            self.sum_of_min_max_costs = self.calc_sum_of_min_max_costs()
            self.strat3_possibilities = self.generate_all_strats_for_strat3()

        if len(self.previous_rounds) < len(self.strat3_possibilities):
            self.strategy = self.strat3_possibilities[self.strat3_counter]
            self.strat3_counter += 1
            return
        best_strat = []
        best_payoff = -9999
        for round in self.previous_rounds:
            if round['payoff'] > best_payoff:
                best_payoff = round['payoff']
                best_strat = round['strategy']
        self.strategy = best_strat

    def calc_sum_of_min_max_costs(self):
        min_cost = 9999
        max_cost = -9999
        for i in range(1, 6):
            cost = 0
            for j in range(5):
                cost += self.gain_and_costs[j][i]
            if cost > max_cost:
                max_cost = cost
            if cost < min_cost:
                min_cost = cost
        return min_cost + max_cost

    def get_countermeasure_cost(self, ctr):
        cost = 0
        for j in range(5):
            # print(self.gain_and_costs[j][ctr + 1])
            cost += self.gain_and_costs[j][ctr + 1]
        return cost

    def get_strategy_countremeasures_cost(self, strategy):
        cost = 0
        for j in range(5):
            # print(self.gain_and_costs[j][ctr + 1])
            if strategy[j] == 1:
                cost += self.get_countermeasure_cost(j)
        return cost

    def generate_all_strats_for_strat3(self):
        last_candidate = [0,0,0,0,0]
        possible_strats = []
        possible_strats.append(last_candidate)
        round = 1

        while round < 31:
            candidate = self.inc_arr(last_candidate)
            if self.get_strategy_countremeasures_cost(candidate) <= self.sum_of_min_max_costs:
                possible_strats.append(candidate)
            last_candidate = candidate
            round += 1
        return possible_strats[1:]
