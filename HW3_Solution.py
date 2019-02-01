import numpy as np
import SimPy.FigureSupport as Fig

class Game(object):
    def __init__(self, id, prob_head):
        self._id= id
        self._rnd = np.random
        self._rnd.seed(id)
        self._probHead = prob_head
        self._countWins = 0

    def simulate(self, n_of_flips):

        count_tails = 0 #number of consecutive tails so far, set to 0

        for i in range(n_of_flips):
            if self._rnd.random_sample() < self._probHead:
                if count_tails >= 2:
                    self._countWins += 1
                count_tails = 0

            else:
                count_tails += 1

    def get_reward(self):
        return 100*self._countWins - 250

class SetOfGames:
    def __init__(self, prob_head, n_games):
        self._gameRewards = []
        self._num_loss = 0 #number of losses; start with zero

        for n in range(n_games):
            #create a new game
            game = Game(id=n, prob_head=prob_head)
            #simulate the game with 20 flips
            game.simulate(20)
            #store the reward
            self._gameRewards.append(game.get_reward())
            if self._gameRewards[n]<0: #if the reward is less than zero then add one to number of losses
                self._num_loss+=1

    def get_ave_reward(self):
        return sum(self._gameRewards)/len(self._gameRewards)

    def get_reward_list(self):
        return self._gameRewards

    def get_loss_probability(self):
        return self._num_loss/len(self._gameRewards) #number of losses divided by the number of rewards

games = SetOfGames(prob_head=0.5, n_games=1000)
print('Expected reward when the probability of head is 0.5:', games.get_ave_reward())

# plot the histogram
Fig.graph_histogram(
    data=games.get_reward_list(),
    title='Histogram of Game Rewards',
    x_label='Game Rewards',
    y_label='Count')

#Print the probability of losing by calculating the proportion of losses out of 1000 games
print('Probability of loss:',games.get_loss_probability())