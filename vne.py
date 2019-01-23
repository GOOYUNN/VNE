import time
from substrate import Substrate
from maker import simulate_events
from analysis import save_result


def main():

    # Step1: create the substrate network and VNRs.
    network_path = 'requests/'
    sub_filename = 'sub.txt'
    sub = Substrate(network_path, sub_filename)
    event_queue = simulate_events(network_path, 2000)

    # Step2: choose an algorithm to run
    algorithm = input("Please select an algorithm('grc','mcts','rl','mine'): ")

    # Step3: handle requests
    start = time.time()
    for req in event_queue:

        # the id of current request
        req_id = req.graph['id']

        if req.graph['type'] == 0:
            """a request which is newly arrived"""

            print("\nTry to map request%s: " % req_id)
            sub.mapping(req, algorithm)

        if req.graph['type'] == 1:
            """a request which is ready to leave"""

            if req_id in sub.mapped_info.keys():
                print("\nRelease the resources which are occupied by request%s" % req_id)
                sub.change_resource(req, 'release')

    end = time.time()-start
    print(end)

    # Step4: output results
    save_result(sub, '%s-VNE.txt' % algorithm)


if __name__ == '__main__':
    main()
