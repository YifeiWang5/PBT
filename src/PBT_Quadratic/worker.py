from exec.PBT_Quadratic import eval
class Worker:
    def __init__(self, init_theta, init_hyperParam):
        self.theta = init_theta
        self.hyperParam = init_hyperParam
        self.p = eval(init_theta)
        self.step = 0
        self.Qhist = []

    def updateHyperParam(self, newHyperParam):
        self.hyperParam = newHyperParam
        return
    def updateTheta(self, newTheta):
        self.theta = newTheta
        return

    def updateStep(self):
        self.step += 1
        return



