import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


class Plots:
    def create_simple_plot(self, trace):
        func = stats.beta(2, 5)
        trace = trace
        x = np.linspace(0.01, .99, 100)
        y = func.pdf(x)
        plt.plot(x, y, 'C1-', lw=3, label='True distribution')
        plt.hist(trace[trace > 0], bins=25, normed=True, label='Estimated distribution')
        plt.xlabel('x')
        plt.ylabel('pdf(x)')
        plt.yticks([])
        plt.legend()
        plt.show()
