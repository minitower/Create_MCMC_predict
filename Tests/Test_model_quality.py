import pandas as pd


class Testing_distribution():

    def __init__(self, trace, dis):
        """
        For create element of this class you must have:
        1) Dis from forecasting models MCMC or variables distribution.
        2) Predicted value for some modeling
        :var trace: Path with presaved models + graph photo
        :var dis: some values from distribution
        :return: estimate of model for createconclusion from investigation
        """
        self.trace = trace
        self.dis = dis


    def Kullback_Leibler_divergence(self, trace, dis):
        """
        Func for find distanse betwen 2 distri
        :param trace:pyplog.fgure
        :param dis:
        :return:
        """
