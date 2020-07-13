import sys
import sys
import os
import numpy as np
from functools import reduce


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Local import
from exec.PBT_Quadratic import step, eval, ready, exploit, explore

def train(population, step, eval, ready, exploit, explore, convergenceTolerance):
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

    return
