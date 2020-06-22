from exec.PBT_Quadratic import realQ

class Worker:
    def __init__(self, init_theta, init_hyperParam):
        self.theta = init_theta
        self.hyperParam = init_hyperParam
        self.p = self.eval() #???
        self.numStepsSinceLastUpdate = 0

    def eval(self):
        currQ = 1.2-(self.hyperParam[0]*self.theta[0]+self.hyperParam[1]*self.theta[1])
        delta = realQ(self.theta)-currQ
        return delta

    def ready(self):
        isReady= False
        if self.numStepsSinceLastUpdate >= 4:
            isReady = True
        return isReady

    def update(self):
        self.numStepsSinceLastUpdate = 0
        return