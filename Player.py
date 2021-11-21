class Player:
    def __init__(self, gain_and_costs, attack_probabilities, initial_strategy):
        self.strategy = initial_strategy
        self.attack_probabilities = attack_probabilities
        self.gain_and_costs = gain_and_costs
    
    def get_strategy(self):
        return self.strategy