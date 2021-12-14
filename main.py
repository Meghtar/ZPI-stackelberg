from Game import Game
from Configuration import *

if __name__ == "__main__": 

    game = Game(gain_and_costs_leader, gains_and_costs_follower, attack_probabilities)

    amount_of_rounds = 100

    for _ in range(amount_of_rounds):
        game.realise_round()
    
    game.summarise_games()
