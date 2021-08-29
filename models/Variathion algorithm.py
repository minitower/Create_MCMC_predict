import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


def posterior_grid(grid_points=50, heads=6, tails=9):
    """
    Func for grid computing of distribution of random var
    :param grid_points: number of point on axis for grid cell (optional)
    :param heads:
    :param tails:
    :return:
    """
    grid = np.linspace(0, 1, grid_points)
    prior = np.repeat(1 / grid_points, grid_points)  # равномерное априорное распределение
    likelihood = stats.binom.pmf(heads, heads + tails, grid)
    posterior = likelihood * prior
    posterior /= posterior.sum()
    return grid, posterior


data = np.repeat([0, 1], (10, 10))
points = 2000
h = data.sum()
t = len(data) - h
grid, posterior = posterior_grid(points, h, t)
plt.plot(grid, posterior, 'o-')
plt.title(f'heads = {h}, tails = {t}')
plt.yticks([])
plt.xlabel('θ')
plt.show()
