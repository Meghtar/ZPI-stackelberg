from Game import Game
from Configuration import *

if __name__ == "__main__": 

    game = Game(gains_and_costs, attack_probabilities)

    amount_of_rounds = 2

    for _ in range(amount_of_rounds):
        game.realise_round()
