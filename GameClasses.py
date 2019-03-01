import numpy as np


class Game:
    def __init__(self, id, prob_head):
        self.id = id
        self.rnd = np.random.RandomState(seed=id)
        self.probHead = prob_head
        self.countWins = 0

    def simulate(self):
        """
        simulates 20 coin tosses and counts the number of times {T, T, H} occurred
        """

        n_consecutive_tails = 0  # number of consecutive tails so far, set to 0

        # flip the coin 20 times
        for i in range(20):

            # find if this flip resulted in head or tail
            if self.rnd.random_sample() < self.probHead:

                # if it is head, check if the last 2 tosses resulted in {T, T}
                if n_consecutive_tails >= 2:
                    # if so, {T, T, H} has occurred
                    self.countWins += 1

                # if this is tail, we set the number of consecutive tails to 0
                n_consecutive_tails = 0

            else:
                # this flip resulted in tail, so we increment the number of consecutive tails by 1
                n_consecutive_tails += 1

    def get_reward(self):
        """
        :return: the reward from this game = 100 * (number of {T, T, H}) - 250
        """
        return 100 * self.countWins - 250


class SetOfGames:
    def __init__(self, prob_head, n_games):

        self.gameRewards = []
        self.numLosses = 0  # number of games we lose money

        for n in range(n_games):
            # create a new game
            game = Game(id=n, prob_head=prob_head)
            # simulate the game with 20 flips
            game.simulate()
            # get the reward
            reward = game.get_reward()
            # store the reward
            self.gameRewards.append(reward)
            # find if we lost in this game
            if reward < 0:
                self.numLosses += 1

    def get_ave_reward(self):
        """
        :return: the average reward from playing all games
        """
        return sum(self.gameRewards) / len(self.gameRewards)

    def get_loss_probability(self):
        """
        :return: the proportion of games that we lost money
        """
        return self.numLosses / len(self.gameRewards)
