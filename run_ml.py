from algorithm import Algorithm
from analysis import Analysis


if __name__ == '__main__':
    result_dir = 'results_algorithm/'
    tool = Analysis(result_dir)
    name = 'ML'
    algorithm = Algorithm(name, result_dir, node_arg=50, link_method=1)
    runtime = algorithm.execute(network_path='networks/',
                                sub_filename='sub-ts.txt')
    tool.save_evaluations(algorithm.evaluation, '%s-VNE.txt' % name)
    print(runtime)
