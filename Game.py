from Follower import Follower
from Leader import Leader

class Game:
    def __init__(self, gain_and_costs, attack_probabilities):
        self.leader = Leader(gain_and_costs, attack_probabilities, [1, 0, 0, 1])
        self.follower = Follower(gain_and_costs, attack_probabilities, [1, 0, 0, 1])
        self.gain_and_costs = gain_and_costs
        self.attack_probabilities = attack_probabilities
        self.round_counter = 0
    
    def calculate_leader_payoff(self):
        return 0
    
    def calculate_follower_payoff(self):
        return 0
    
    def realise_round(self):
        print('Realising round ' + str(self.round_counter))
        self.round_counter += 1
        pass