import copy
import time
from network import Network
from analysis import Analysis
from algorithm import Algorithm
from queue import PriorityQueue
from event import Event
import tensorflow as tf


def main():

    # Step1: 读取底层网络和虚拟网络请求文件
    network_files_dir = 'networks/'
    results_dir = 'results_single/'
    sub_filename = 'sub-wm.txt'
    networks = Network(network_files_dir)
    substrate, requests = networks.get_networks_single_layer(sub_filename, 1000)

    with open(results_dir + 'time.txt', 'a') as f:

        # Step1: 模拟虚拟网络请求事件队列
        events = PriorityQueue()
        for req in requests:
            events.put(Event(req))

        # Step2: 配置映射算法
        node_arg = 150
        algorithm = Algorithm('ml', node_arg=node_arg, link_arg=5)

        start = time.time()
        # Step3: 依次处理虚拟网络请求事件
        with tf.Session() as sess:
            algorithm.configure(substrate, sess)
            algorithm.handle(substrate, events)
        runtime = time.time() - start
        f.write("%-10s\t%-20s\n" % (node_arg, runtime))

        # Step4: 输出映射结果文件
        tool = Analysis(results_dir)
        tool.save_result(algorithm.evaluation, 'ML-VNE-old-%s.txt' % node_arg)


if __name__ == '__main__':
    main()