import sys
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
dirName = os.path.dirname(__file__)
sys.path.append(os.path.join(dirName, '..', '..'))

from src.PBT_Quadratic.worker import Worker
# from src.PBT_Quadratic.Evaluation import Evaluation


def realQ(theta):
    return 1.2-sum(i*i for i in theta)

def main():
    # PBT_Quadratic Environment initialization
    convergenceTolerance = 10e-5 #???
    updateInterval = 4 # every 4 iteration, do an update
    init_theta = [0.9, 0.9]  # set initial weights
    #create the worker population
    numOfWorkers = 2
    init_hyperParam = [[0, 1], [1, 0]]
    worker_list = [Worker(init_theta, init_hyperParam[i]) for i in range(numOfWorkers)]
    # for worker in worker_list:
    #     while(worker's Q gradient is not below convergenceTolerance):
    #       worker.setTheta(step(θ,h))
    #       worker's eval = eval(theta(new))
    #       if worker.ready():
    #             [h_prime, theta_prime] = exploit(worker_list)
    #             if worker.getTheta() != theta_prime:
    #               worker = worker.update(h_prime, theta_prime) #???
    #               worker.setP = worker.eval() #???

    #
    #
    #

    # DIRNAME = os.path.dirname(__file__)
    # trajectoryDirectory = os.path.join(DIRNAME, '..', '..', 'data', 'evaluateObstacle',
    #                                    'trajectories')
    # if not os.path.exists(trajectoryDirectory):
    #     os.makedirs(trajectoryDirectory)



if __name__ == '__main__':
    main()