
class Player:
    def __init__(self, initial_strategy):
        self._strategy = initial_strategy
    
    def get_strategy(self):
        return self._strategy

class Leader(Player):
    pass

class Follower(Player):
    pass

if __name__ == "__main__":
    leader = Leader([1, 0, 0, 1])
    follower = Follower([0, 1, 1, 0])

    print("initial leader strategy: ", leader.get_strategy())
    print("initial follower strategy: ", follower.get_strategy())