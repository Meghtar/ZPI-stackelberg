import random

from Configuration import gains_and_costs_follower, attack_probabilities
from Player import Player


class Follower(Player):
    def __init__(self, gain_and_costs, attack_probabilities, initial_strategy):
        super().__init__(gain_and_costs, attack_probabilities, initial_strategy)
        self.all_game_possibilities = self.generate_all_game_possibilities()

    def generate_all_game_possibilities(self):
        perm = []

        while len(perm) != 31:  # 31 możliwości bo w jedno miejsce możemy wstawić {1, 0}, a mamy pięć ataków, więc 2^5 - 1, bo nie powinien stosować strategii [0, 0, 0, 0, 0]
            rnd = format(random.getrandbits(5), '05b')
            res = [int(i) for i in list(rnd)]
            if res not in perm and res != [0, 0, 0, 0, 0]:
                perm.append(res)
        print(len(perm))
        return perm

    def get_prob(self, leader, follower):
        return attack_probabilities[leader][follower]

    def follower_gain(self, asset_number):
        return gains_and_costs_follower[asset_number][0]

    def follower_cost(self, asset_number, countermeasure):
        return gains_and_costs_follower[asset_number][countermeasure + 1]

    def create_new_strategy(self, leader_strategy):
        self.strategy = [1, 1, 1, 0, 1]
        best_strategy_score = -1000

        for game in self.all_game_possibilities:
            for i in range(len(game)):
                for j in range(len(game)):
                    strategy_score = leader_strategy[i] * game[j] * \
                                     (self.get_prob(leader_strategy[i], game[j]) * \
                                      (self.follower_gain(j) - self.follower_cost(i, j))) + \
                                     (1 - self.get_prob(leader_strategy[i], game[j])) * \
                                     ((-1) * self.follower_cost(i, j))
                    if strategy_score > best_strategy_score:
                        best_strategy_score = strategy_score
                        self.strategy = game
        # print("Najlepsza strategia ", self.strategy, " punkty ", best_strategy_score)
