import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from file_task import *
import os

fw = File_work()


class Plots:
    def __init__(self, plot_conf, data):
        """
        For init this class firstly - read plot_conf from %PATH%\\conf\\conf_for_plot_style.ini
        :param plot_conf: dict, whose contains config for plot
        :param data: pd.DataFrame with real_data+
        """
        self.plot_conf = plot_conf
        # Check for type of data (pd.DataFrame)
        self.data = data
        if type(self.data) != pd.DataFrame:
            try:
                self.data = pd.DataFrame(self.data)
            except:
                raise TypeError('Can not convert ' + type(self.data) + ' to pd.DataFrame')
        # Search for NaN value in data pd.DataFrame:
        self.n_col = len (self.data.columns)
        if type (self.data) == pd.Series:
            print ('Build 2-D plot')
        elif type (self.data) == pd.DataFrame:
            print ('Build 2-D plot with {}'.format(self.n_col))
        else:
            raise TypeError ('Something wrong with data')

    def build_1_dimension_plot(self, data, plot_conf):
        """
        This func create plot with all col of pd.DataFrame, where axis x is pd.DataFrame.index
        :param df: pd.DataFrame with data
        :param type: ['plot'] list with type plots
        :param color: 'blue' lst with color of plots
        :param date_range: list with 2 value: start and end of data range
        :return: matplotlib.pyplot
        """
        if self.data.shape [1] == 1:
            # 2-D plot for data
            plt.figure(figsize=(10, 10))
            #try:
            print (plot_conf['plot_type'])
            os.system (''+ self.plot_conf ['plot_type']+ " (data, color=self.plot_conf['color'])")
            #except:
                #print('Wrong type name, creating plot')
                #plt.plot(data[data.columns[0]].unstack(level=0), color=self.plot_conf['color'])
            plt.ylabel("Data")
            plt.xlabel('Timestamp')
            plt.savefig(os.path.dirname(__file__) + '\\img.png')
        if self.data.shape[1] > 1:
            # 2-D plot for data with
            self.init_type_of_img()

    def init_type_of_img (self):
        lst_types = []
        if self.n_col == len (self.plot_conf ['plot_type_subplots']):
            for i in zip(self.data.columns, self.plot_conf.plot_type_subplots):
                lst_types.append(i)
                print (lst_types )
    def plot_type_choise (self):
        """
        Func to coising plot type via conf_for_plot_style.ini. Contains style like:
        ['plot', 'hist', 'scater', '']

        :return:
        """