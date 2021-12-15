from Configuration import attack_and_remedy_prob
from Follower import Follower
from Leader import Leader
import random

class Game:
    def __init__(self, gain_and_costs_leader, gains_and_costs_follower, attack_probabilities):
        self.leader = Leader(gain_and_costs_leader, attack_probabilities, [0, 0, 0, 0, 1])
        self.follower = Follower(gains_and_costs_follower, attack_probabilities, [1, 0, 0, 1, 0])
        self.attack_probabilities = attack_probabilities
        self.gain_and_costs_leader = gain_and_costs_leader
        self.gains_and_costs_follower = gains_and_costs_follower
        self.round_counter = 0
        self.attack_count = 5
        self.defence_count = 5
        self.best_leader_round = {
            'round': -1,
            'payoff': -99999,
            'opp_payoff': 99999,
            'strategy': [0,0,0,0,0],
            'opp_strategy': [0,0,0,0,0]
        }
        self.best_follower_round = {
            'round': -1,
            'payoff': -99999,
            'opp_payoff': 99999,
            'strategy': [0,0,0,0,0],
            'opp_strategy': [0,0,0,0,0]
        }

    def probability(self, leader, follower):
        # print('leader: {}, follower: {}, prob: {}'.format(leader, follower, self.attack_probabilities[leader][follower]))
        return self.attack_probabilities[leader][follower]

    def leader_gain(self, asset_number):
        # print('asset: {}, leader_gain: {}'.format(asset_number, self.gain_and_costs_leader[asset_number][0]))
        return self.gain_and_costs_leader[asset_number][0]

    def leader_cost(self, asset_number, countermeasure):
        # print('asset: {}, countermeasure: {}, cost: {}'.format(asset_number, countermeasure, self.gain_and_costs_leader[asset_number][countermeasure + 1]))
        return self.gain_and_costs_leader[asset_number][countermeasure + 1]

    def follower_gain(self, asset_number):
        # print('asset: {}, leader_gain: {}'.format(asset_number, self.gains_and_costs_follower[asset_number][0]))
        return self.gains_and_costs_follower[asset_number][0]

    def follower_cost(self, asset_number, countermeasure):
        # print('asset: {}, countermeasure: {}, cost: {}'.format(asset_number, countermeasure, self.gains_and_costs_follower[asset_number][countermeasure + 1]))
        return self.gains_and_costs_follower[asset_number][countermeasure + 1]

    def calculate_leader_payoff(self):
        total_payoff = 0
        for i in range(self.attack_count):
            for j in range(self.defence_count):
                total_payoff += self.leader.get_strategy(i) * self.follower.get_strategy(j) * \
                    (self.probability(leader=i, follower=j) * \
                    ((-1) * self.leader_gain(i) - self.leader_cost(i,j))) + \
                    (1 - self.probability(leader=i, follower=j)) * \
                    (self.leader_gain(i) - self.leader_cost(i,j))
        return total_payoff

    def calculate_follower_payoff(self):
        total_payoff = 0
        for i in range(self.attack_count):
            for j in range(self.defence_count):
                total_payoff += self.leader.get_strategy(i) * self.follower.get_strategy(j) * \
                    (self.probability(leader=i, follower=j) * \
                    (self.follower_gain(j) - self.follower_cost(i,j))) + \
                    (1 - self.probability(leader=i, follower=j)) * \
                    ((-1) * self.follower_cost(i,j))
        return total_payoff

    def realise_round(self):
        self.round_counter += 1
        print('Realising round ' + str(self.round_counter))

        self.leader.create_new_strategy()
        self.follower.create_new_strategy(self.leader.get_whole_strategy()) # TODO: leader strat already known
        #self.follower.create_new_strategy()

        print('Leader strategy:')
        print(self.leader.get_whole_strategy())

        print('Follower strategy:')
        print(self.follower.get_whole_strategy())

        print('--------------------')

        leader_payoff = self.calculate_leader_payoff()
        follower_payoff = self.calculate_follower_payoff()

        # Adding games to summary
        if leader_payoff > self.best_leader_round['payoff']:
            self.best_leader_round['payoff'] = leader_payoff
            self.best_leader_round['opp_payoff'] = follower_payoff
            self.best_leader_round['round'] = self.round_counter
            self.best_leader_round['strategy'] = self.leader.get_whole_strategy()
            self.best_leader_round['opp_strategy'] = self.follower.get_whole_strategy()

        if follower_payoff > self.best_follower_round['payoff']:
            self.best_follower_round['payoff'] = follower_payoff
            self.best_follower_round['opp_payoff'] = leader_payoff
            self.best_follower_round['round'] = self.round_counter
            self.best_follower_round['strategy'] = self.follower.get_whole_strategy()
            self.best_follower_round['opp_strategy'] = self.leader.get_whole_strategy()


        print('Payoffs:')
        print('Leader_payoff={lp}\tFollower_payoff={fp}'.format(lp=leader_payoff, fp=follower_payoff))

        self.leader.add_last_result(
            self.leader.get_whole_strategy(),
            self.follower.get_whole_strategy(),
            leader_payoff,
            follower_payoff
        )
        self.follower.add_last_result(
            self.follower.get_whole_strategy(),
            self.leader.get_whole_strategy(),
            follower_payoff,
            leader_payoff
        )

    def summarise_games(self):
        print('==================================')
        print('Best round for Leader:')
        print('Round number: {}'.format(
            self.best_leader_round['round']
        ))
        print('Leader strategy: {} \t Follower strategy: {}'.format(
            self.best_leader_round['strategy'],
            self.best_leader_round['opp_strategy']
        ))
        print('Leader payoff: {} \t Follower payoff: {}'.format(
            self.best_leader_round['payoff'],
            self.best_leader_round['opp_payoff']
        ))
        print('==================================')
        print('Best round for Follower:')
        print('Round number: {}'.format(
            self.best_follower_round['round']
        ))
        print('Follower strategy: {} \t Leader strategy: {}'.format(
            self.best_follower_round['strategy'],
            self.best_follower_round['opp_strategy']
        ))
        print('Follower payoff: {} \t Leader payoff: {}'.format(
            self.best_follower_round['payoff'],
            self.best_follower_round['opp_payoff']
        ))
        print('==================================')

    def best_attacker_strategy(self, strategy_array):
        best_strategy = []
        for i in range(0, len(strategy_array)):
            best_strategy = attack_and_remedy_prob[i].index(max(attack_and_remedy_prob[i]))
        #jeśli oba prawdopodobieństwa najlepszej strategi są takie same to wybierz losowo jedno z nich.
        return best_strategy[random.randint(0, len(best_strategy)-1)]
