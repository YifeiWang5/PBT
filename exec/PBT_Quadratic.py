import sys
import os
import numpy as np

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
dirName = os.path.dirname(__file__)
sys.path.append(os.path.join(dirName, '..', '..'))
from src.worker import Worker
# from src.PBT import train

def QHat(theta, hyperParam):
    return 1.2-(hyperParam[0]*theta[0]*theta[0]+hyperParam[1]*theta[1]*theta[1])

def eval(theta):
    return 1.2-sum(i*i for i in theta) # - QHat()???

def lossFunc(theta, hyperParam):
    return eval(theta) - QHat(theta, hyperParam)

def step(theta, hyperParam):
    # one step gradient descent; find the delta  (loss function(param); can analytically compute it)
    # loss_func = eval(theta) - QHat(theta, hyperParam) # error from the true value given the params
    # the gradient vector
    gradient = [2*theta[0]*(1-hyperParam[0])+(1-hyperParam[1])*theta[1]*theta[1], 2*theta[1]*(1-hyperParam[1])+(1-hyperParam[0])*theta[0]*theta[0]]
    eta = -0.1 # step size/ learning factor
    delta = [eta * i for i in gradient]
    new_t = [delta[i] + theta[i] for i in range(len(theta))]
    return new_t

def ready(evalVal, step, pop):
    return step % 4 == 0

def exploit(hyperParam, theta, evalVal, pop):
    # select the best-performing worker & use its params
    p_list = [worker.p for worker in pop]
    best_idx = p_list.index(max(p_list))
    best_worker = pop[best_idx]
    result = [best_worker.hyperParam, best_worker.theta]
    return result

def explore(hPrime, thetaPrime, pop):
    # perturb each hyperparameter independently by a factor of 1.2 or 0.8
    possible_factors = [1.2, 0.8]
    factor_list = np.random.choice(possible_factors, size=len(hPrime))
    new_h = factor_list * hPrime
    return new_h, thetaPrime

# def updateWorker(worker, newTheta, newHyperParam):
#     worker.updateTheta(newTheta)
#     worker.updateHyperParam(newHyperParam)
#     worker.updateStep() # update the step count for the worker
#     return

def main():
    # PBT_Quadratic Environment initialization
    convergenceTolerance = 10e-4 #???
    # updateInterval = 4 # every 4 iteration, do an update
    init_theta = [0.9, 0.9]  # set initial weights
    #create the worker population
    numOfWorkers = 2
    init_hyperParam = [[0, 1], [1, 0]]
    worker_list = [Worker(init_theta, init_hyperParam[i]) for i in range(numOfWorkers)]
    optimal_theta = train(worker_list, step, eval, ready, exploit, explore, convergenceTolerance)
    # Visualization

if __name__ == '__main__':
    main()