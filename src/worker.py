import sys
import os
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Local import
# from exec.PBT_Quadratic import eval

class Worker:
    def __init__(self, init_theta, init_hyperParam):
        self.theta = init_theta
        self.hyperParam = init_hyperParam
        self.p = 1.2-sum(i*i for i in init_theta)
        self.step = 0
        # for plotting
        self.theta_history = []
        self.eval_history = []

    def updateWorker(self, newHyperParam, newTheta, newEval, newStep):
        self.hyperParam = newHyperParam
        self.theta = newTheta
        self.p = newEval
        self.step = newStep
        self.theta_history.append(np.copy(self.theta))
        self.eval_history.append(self.p)
        return



