import sys
import sys
import os
import numpy as np
from functools import reduce

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


def train(population, step, eval, ready, exploit, explore, lossFunc, convergenceTolerance, stepLimit):

    for worker in population:
        while(lossFunc(worker.theta, worker.hyperParam) > convergenceTolerance and worker.step < stepLimit):
            update(worker, population, step, eval, ready, exploit, explore)
    return population
        # exploit(population[0].hyperParam, population[0].theta, population[0].p, population)[1] # best hyperParam
