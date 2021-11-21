class Game:
    def __init__(self, gain_and_costs, attack_probabilities, leader, follower):
        self.leader = leader
        self.follower = follower
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