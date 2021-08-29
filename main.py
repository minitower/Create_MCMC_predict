from models.Stochastic_models import *
from plot_creator.create_plot import *
from file_task import File_work

model_list = ['MCMC', 'Various']

if __name__ == '__main__':
    # load config of modeling
    fw = File_work()
    dict_conf = fw.decode_config(select_conf=[1, 1])
    data = fw.read_from_file(fw.path_with_real_data)
    # Prototype of launch correct model
    print(dict_conf)
    if dict_conf['model_type'] == 'MCMC':
        MCMC = MCMC_models(np.array(data[dict_conf['param_for_analysis']]))
        trace = pd.DataFrame(MCMC.metropolis_for_discrete())
        plot_data = data[dict_conf['param_for_analysis']].copy()
        plot_data['Estimated'] = trace
        plt = Plots(dict_conf, plot_data)
        # Index of pd.DataFrame - y dim
        # Index of pd.DataFrame - x dim
        plt.build_1_dimension_plot(data, plot_conf=dict_conf)

    # if data.find('Various modeling') != -1:
    # launch Various modeling process
    # else:
    #    raise TypeError ('Something wrong with model name in file'
    #                     +conf_path+', please correct model name and relaunch program')
