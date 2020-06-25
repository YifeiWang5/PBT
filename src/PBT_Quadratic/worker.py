from src.PBT_Quadratic.model import eval
class Worker:
    def __init__(self, init_theta, init_hyperParam):
        self.theta = init_theta
        self.hyperParam = init_hyperParam
        self.p = eval(init_theta) #???
        self.numStepsSinceLastUpdate = 0



