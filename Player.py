class Player:
    def __init__(self, gain_and_costs, attack_probabilities, initial_strategy):
        self.strategy = initial_strategy
        self.attack_probabilities = attack_probabilities
        self.gain_and_costs = gain_and_costs
        self.previous_rounds = []
    
    def get_whole_strategy(self):
        return self.strategy
    
    def get_strategy(self, index):
        return self.strategy[index]

    def add_last_result(self, player_strategy, opponent_strategy, player_payoff, opponent_payoff):
        self.previous_rounds.append({
            "strategy": player_strategy,
            "opponent_strategy": opponent_strategy,
            "payoff": player_payoff,
            "opponent_payoff": opponent_payoff
        })

    def create_new_strategy(self):
        raise NotImplementedError