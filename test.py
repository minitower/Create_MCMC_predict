import numpy as np
import scipy.stats as stats


def posterior_grid(posit_prop=0.5, negative_prop=0.5, grid_points=50):
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
