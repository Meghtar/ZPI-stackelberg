from Follower import Follower
from Leader import Leader

class Game:
    def __init__(self, gain_and_costs, attack_probabilities):
        self.leader = Leader(gain_and_costs, attack_probabilities, [1, 0, 0, 1])
        self.follower = Follower(gain_and_costs, attack_probabilities, [1, 0, 0, 1])
        self.gain_and_costs = gain_and_costs
        self.attack_probabilities = attack_probabilities
        self.round_counter = 0
    
    def sigma(self, i):
        return 1

    def calculate_leader_payoff(self):
        total_payoff = 0
        attack_count = 5
        defence_count = 5
        for i in range(attack_count):
            for j in range(defence_count):
                # sigma_i - strategia gracza (followersa/leadera) wobec i-tego elementu 
                total_payoff += self.sigma(j) * self.sigma(i) * \
                    (self.prob(attacks[i], countermeasures[j]) * \
                    ((-1) * Val_a - CostDef(a,a,c,j))) + \
                    (1 -self.prob(attacks[i], countermeasures[j])) * \
                    (Val_a - CostDef(a,a,c,j)) # TODO: insert all necessary data and functions
        return 0
    
    def calculate_follower_payoff(self):
        total_payoff = 0
        attack_count = 5
        defence_count = 5
        for i in range(attack_count):
            for j in range(defence_count):
                total_payoff += self.sigma(j) * self.sigma(i) * \
                    (self.prob(attacks[i], countermeasures[j]) * \
                    (Gain(a) - CostAttack(a,a,c,i))) + \
                    (1 -self.prob(attacks[i], countermeasures[j])) * \
                    ((-1) * CostAttack(a,a,c,i)) # TODO: insert all necessary data and functions
        return 0
    
    def realise_round(self):
        print('Realising round ' + str(self.round_counter))
        self.round_counter += 1
        pass