import sys
import os
import numpy as np

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
dirName = os.path.dirname(__file__)
sys.path.append(os.path.join(dirName, '..', '..'))

# from src.PBT_Quadratic.worker import Worker
def QHat(theta, hyperParam):
    return 1.2-(hyperParam[0]*theta[0]*theta[0]+hyperParam[1]*theta[1]*theta[1])

def eval(theta):
    return 1.2-sum(i*i for i in theta) # - QHat()???

# def step(theta, hyperParam):
#     return
#
#     def step(self, vanilla=False, rmsprop=False, Adam=False):
#         """one step of GD"""
#         decay_rate = 0.9
#         alpha = 0.01
#         eps = 1e-5
#
#         d_surrogate_obj = -2.0 * self.h * self.theta
#
#         if vanilla:
#             self.theta += d_surrogate_obj * alpha  # ascent to maximize function
#         else:
#             self.rms = decay_rate * self.rms + (1 - decay_rate) * d_surrogate_obj ** 2
#             self.theta += alpha * d_surrogate_obj / (np.sqrt(self.rms) + eps)

def ready(evalVal, step, pop):
    return step % 4 == 0

def exploit(hyperParam, theta, evalVal, pop):
    # select the best-performing worker & use its params
    p_list = [worker.p for worker in pop]
    best_idx = p_list.index(max(p_list))
    best_worker = pop[best_idx]
    return best_worker.hyperParam, best_worker.theta

def explore(hPrime, thetaPrime, pop):
    # perturb each hyperparameter independently by a factor of 1.2 or 0.8
    possible_factors = [1.2, 0.8]
    factor_list = np.random.choice(possible_factors, size=len(hPrime))
    new_h = factor_list * hPrime
    # # perturb hyperparaters with noise from a normal distribution
    # eps = np.random.randn(*hPrime.shape) * 0.1
    # new_h = hPrime + eps
    return new_h, thetaPrime

def updateWorker(worker,newTheta, newHyperParam):
    worker.updateTheta(newTheta)
    worker.updateHyperParam(newHyperParam)
    worker.updateStep() # update the step count for the worker
    return

def main():
    # PBT_Quadratic Environment initialization
    convergenceTolerance = 10e-5 #???
    updateInterval = 4 # every 4 iteration, do an update
    init_theta = [0.9, 0.9]  # set initial weights
    #create the worker population
    numOfWorkers = 2
    init_hyperParam = [[0, 1], [1, 0]]
    # worker_list = [Worker(init_theta, init_hyperParam[i]) for i in range(numOfWorkers)]



if __name__ == '__main__':
    main()