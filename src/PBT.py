import sys
import sys
import os
import numpy as np
from functools import reduce


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Local import
from exec.PBT_Quadratic import step, eval, ready, exploit, explore, lossFunc, population, convergenceTolerance
def update(worker, population, step, eval, ready, exploit, explore):
    worker.setTheta(step(θ, h))
    curr_eval = eval(worker.theta)
    if ready(curr_eval, worker.step, population):
        [h_prime, theta_prime] = exploit(worker.hyperParam, worker.theta, curr_eval, population)
        if worker.getTheta() != theta_prime:
            [temp_h, temp_t] = explore(h_prime, theta_prime, population)
            temp_eval = eval(temp_t)
            worker.updateWorker(temp_h, temp_t, temp_eval, worker.step + 1)
        else:
            worker.updateWorker(worker.hyperParam, worker.theta, curr_eval, worker.step+1)
    return


def train(population, step, eval, ready, exploit, explore, lossFunc, convergenceTolerance):

    for worker in population:
        while(lossFunc(worker.theta, worker.hyperParam) > convergenceTolerance):
            update(worker, population, step, eval, ready, exploit, explore)

#
#

    return exploit(population[0].hyperParam, population[0].theta, population[0].p, population)[1] # best hyperParam
