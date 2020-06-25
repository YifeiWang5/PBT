def realQ(theta):
    return 1.2-sum(i*i for i in theta)

def QHat(theta, hyperParam):
    return 1.2-(hyperParam[0]*theta[0]*theta[0]+hyperParam[1]*theta[1]*theta[1])

def eval(theta):
    return realQ(theta) # - QHat()???

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

def ready(count):
    isReady= False
    if count >= 4:
        isReady = True
    return isReady