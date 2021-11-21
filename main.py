from Leader import Leader
from Follower import Follower
from Game import Game
from Configuration import *

if __name__ == "__main__": 

    leader = Leader(gain_and_costs, attack_probabilities, [1, 0, 0, 1])
    follower = Follower(gain_and_costs, attack_probabilities, [0, 1, 1, 0])

    game = Game(gain_and_costs, attack_probabilities, leader, follower)

    amount_of_rounds = 10

    for _ in range(amount_of_rounds):
        game.realise_round()
