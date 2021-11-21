
class Player:
    def __init__(self, gain_and_costs, attack_probabilities, initial_strategy):
        self.strategy = initial_strategy
        self.attack_probabilities = attack_probabilities
        self.gain_and_costs = gain_and_costs
    
    def get_strategy(self):
        return self.strategy

class Leader(Player):
    def create_new_strategy(self, previous_strategies, previous_follower_strategies, previous_outcomes): # TODO: remove which not needed
        return []

class Follower(Player):
    def create_new_strategy(self, previous_strategies, previous_leader_strategies, previous_outcomes): # TODO: remove which not needed
        return []

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


if __name__ == "__main__": 

    # TODO: add array/map containing Pi_idle/Pi_busy/Pi_open/Pi_close and c's values

    gain_and_costs = [{
        "number": 1,
        "gain": 1,
        "attack_costs": [1, 1, 1]
    },
    {
        "number": 2,
        "gain": 1,
        "attack_costs": [1, 2, 3]
    }]

    attack_probabilities = {
        "countermeasure_1" : [0, 0.1, 1, 0.9],
        "countermeasure_2" : [0, 0.1, 1, 0.9],
        "countermeasure_3" : [0, 0.1, 1, 0.9]
    }

    leader = Leader(gain_and_costs, attack_probabilities, [1, 0, 0, 1])
    follower = Follower(gain_and_costs, attack_probabilities, [0, 1, 1, 0])

    game = Game(gain_and_costs, attack_probabilities, leader, follower)

    amount_of_rounds = 10

    for _ in range(amount_of_rounds):
        game.realise_round()
