from analysis import Analysis
from algorithm import Algorithm


if __name__ == '__main__':
    tool = Analysis('results_granularity/')
    for i in range(3):
        granularity = i + 1
        algorithm = Algorithm('ML%d' % granularity,
                              node_arg=50,
                              link_method=1,
                              granularity=granularity)
        algorithm.execute(network_path='networks/',
                          sub_filename='sub-wm.txt')
        tool.save_evaluations(algorithm.evaluation, '%s.txt' % granularity)
