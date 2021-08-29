import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.interpolate as inter


class MCMC_models:

    def __init__(self, df_basic, interpolate=0):
        """
        Initiation necessary values for MCMC algorithms
        :param real_data: data with
        :param interpolate:
        """
        self.df_basic = stats.beta(2, 4)
        self.interpolate = interpolate
        if self.interpolate == 1:
            self.df_basic = inter.interp1d(self.real_data.index,
                                           self.real_data[0], kind='cubic')

    def metropolis_for_discrete(self, draws=10000):
        """
        Func of Monte-Carlo Markov Chain with Metropolis-Hasting algorithm with discrete data
        :param draws: number of iterations (int type)
        :return: estimated distribution (list type)
        """
        trace = np.zeros(draws)
        print(self.df_basic)
        old_x = 0.5  # self.df_basic.mean()
        old_prob = self.df_basic.pdf(old_x)
        delta = np.random.normal(0, 0.5, draws)
        for i in range(draws):
            new_x = old_x + delta[i]
            new_prob = self.df_basic.pdf(new_x)
            acceptance = new_prob / old_prob
            if acceptance >= np.random.random():
                trace[i] = new_x
                old_x = new_x
                old_prob = new_prob
            else:
                trace[i] = old_x
        return trace

    def metropolis_for_inf(self, draws=10000):
        """
        Func of Monte-Carlo Markov Chain with Metropolis-Hasting algorithm with infinite data
        :param draws: number of iterations (int type)
        :return: estimated distribution (list type)
        """
        trace = np.zeros(draws)
        old_x = 0.5  # self.real_data.mean()
        old_prob = self.real_data.pdf(old_x)
        delta = np.random.normal(0, 0.5, draws)
        for i in range(draws):
            new_x = old_x + delta[i]
            new_prob = self.real_data.pdf(new_x)
            acceptance = new_prob / old_prob
            if acceptance >= np.random.random():
                trace[i] = new_x
                old_x = new_x
                old_prob = new_prob
            else:
                trace[i] = old_x
        return trace


    def posterior_grid(self, posit_prop=0.5, negative_prop=0.5, grid_points=50):
        """
        Grid computing for Bayesian probability concept. If, in some reason, MCMC didn't work
        correct model, algorithm starts grid computing. In this model we must predict only fact of client refund.
        This fact can be interpretate as Bernuli destination (p^n+q^t, where p = (1-q))
        :param posit_prop: in this model we must predict only fact of client refund
        :param negative_prop: if Bernuli - negative = 1-positive
        :param grid_points: number of dot, where parallel line from ever axis have, at least, one equal dot
        :return grid, posterior: n_dots in axis, posterior distention of random var
        """
        grid = np.linspace(0, 1, grid_points)
        prior = np.repeat(1 / grid_points, grid_points)  # равномерное априорное распределение
        likelihood = stats.binom.pmf(posit_prop, posit_prop + negative_prop, grid)
        posterior = likelihood * prior
        posterior /= posterior.sum()
        return grid, posterior
