import os


class File_work:

    def __init__(self):
        self.config_path = [os.path.dirname(__file__) + '/conf/config.ini',
                            os.path.dirname(__file__) + '/conf/conf_for_plot_style.ini']
        self.directhion_path = os.path.dirname('main.py')
        self.path_with_filename = os.path.abspath('main.py')
        self.path_with_real_data = os.path.join(os.path.dirname(__file__),
                                                'Data_storage/travel_insurance.csv')
        self.counter = 0
        if not os.path.exists(self.config_path[0]):
            raise FileNotFoundError('Core config file was corrupted or something went wrong')
        if not os.path.exists(self.config_path[1]):
            raise FileNotFoundError('Models setting file was corrupted or something went wrong')

    @staticmethod
    def write_in_file(path, message):
        """
        Func for write some message to file
        :param path: absolute path to necessary file (str type)
        :param message: data with message in string format (str type)
        :return: None (None type)
        """
        with open(path, 'a+') as f:
            if type(message) is None:
                pass
            else:
                f.write(message)
            f.close()
            print(message + 'success writen on file!')

    def read_from_file(self, path):

        """
        Func for read some message from file
        :param path: absolute path to necessary file (str type)
        :return: message from data (str type)
        """
        if os.path.split(path)[1].split('.')[1] != 'csv':
            with open(path) as f:
                data = f.read()
        else:
            import pandas as pd
            data = pd.read_csv(path, header=0, encoding='UTF-8')
        return data

    def decode_config(self, select_conf=None):
        """
        Func for convert data from .ini file
        :param select_conf: list with len = count of config scripts and create quasi variable
        from config path (lst type)
        :return: dict with config of script
        """
        if select_conf is None:
            select_conf = [1, 1]
        tmp = []  # init tmp var
        for i in select_conf:
            if i == 1 or i:
                data = self.read_from_file(path=self.config_path[self.counter])
                data = data.split('\n')
                for i in data:
                    tmp.append(tuple(i.split('=')))
                self.counter += 1
            else:
                self.counter += 1
                pass
        return dict(tmp)

    def decode_plot_type_conf (self, dict_conf):
        """
        Func to create code more 'readability', simple and object-oriente.
        :param dict_conf: out of decode_conf code
        :return: matplotlib.pyplot for saving % showing
        """
        if dict_conf['plot']=='plt.plot':
            plt.plot (color = blue, callable(True))
            plt.axis ()
