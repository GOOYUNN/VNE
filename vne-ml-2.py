import time
from network import Network
from analysis import Analysis
from more.algorithm import Algorithm


def main():

    # Step1: 读取底层网络和虚拟网络请求文件
    network_files_dir = 'networks-more/'
    sub_filename = 'sub-wm.txt'
    networks = Network(network_files_dir)
    sub, queue1, queue2 = networks.get_networks(sub_filename, 2000, 0, more_flag=True)

    # Step2: 配置映射算法
    node_arg = 50
    algorithm = Algorithm(node_arg=node_arg, link_arg=5)
    algorithm.configure(sub)

    # Step3: 处理虚拟网络请求事件
    start = time.time()
    algorithm.handle(sub, queue1, queue2)
    time_cost = time.time() - start
    print(time_cost)

    # Step4: 输出映射结果文件
    tool = Analysis()
    tool.save_result(algorithm.evaluation, 'ML-VNE-0326-%s-more.txt' % node_arg)


if __name__ == '__main__':
    main()
