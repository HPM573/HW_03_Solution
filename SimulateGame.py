import deampy.plots.histogram as hist

import GameClasses as Cls

fair_games = Cls.SetOfGames(id=0, prob_head=0.5)
fair_games.simulate(n_games=1000)
print('Expected reward when the probability of head is 0.5:', fair_games.get_ave_reward())

# plot the histogram
hist.plot_histogram(
    data=fair_games.gameRewards,
    title='Fair Game',
    bin_width=100,
    x_label='Game Rewards',
    y_label='Count')

# Print the probability of losing by calculating the proportion of losses out of 1000 games
print('Probability of loss when the probability of head is 0.5:', fair_games.get_loss_probability())


bias_games = Cls.SetOfGames(id=0, prob_head=0.4)
bias_games.simulate(n_games=1000)
print('Expected reward when the probability of head is 0.4:', bias_games.get_ave_reward())

# plot the histogram
hist.plot_histogram(
    data=bias_games.gameRewards,
    title='Biased Game (Probability of Head is 0.4)',
    bin_width=100,
    x_label='Game Rewards',
    y_label='Count')

# Print the probability of losing by calculating the proportion of losses out of 1000 games
print('Probability of loss when the probability of head is 0.4:', bias_games.get_loss_probability())
