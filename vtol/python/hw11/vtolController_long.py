import numpy as np
import vtolParamHW11_long as P
import sys
sys.path.append('..')  # add parent directory
import vtolParam as P0


class vtolController_long:

    def __init__(self):

        self.h_dot = 0.0          # derivative of theta
        self.h_d1 = 0.0          # Angle theta delayed by 1 sample
        self.K = P.K                 # state feedback gain
        self.kr = P.kr               # Input gain
        self.limit = P0.F_max         # Maxiumum force
        self.beta = P.beta           # dirty derivative gain
        self.Ts = P.Ts               # sample rate of controller

    def u(self, y_r, y):
        # y_r is the referenced input
        # y is the current state
        h_r = y_r[0]
        h = y[1]

        # differentiate theta
        self.differentiateH(h)

        # Construct the state
        x = np.matrix([[h], [self.h_dot]])

        # compute equilibrium force F_e
        F_e = (P0.mc + P0.mr + P0.ml) * P0.g
        # compute the linearized force using PD
        F_tilde = -self.K*x + self.kr*h_r
        # compute total force
        F = F_e + F_tilde
        F = self.saturate(F)
        return [F]


    def differentiateH(self, h):
        '''
            differentiate h
        '''
        self.h_dot = self.beta*self.h_dot + (1-self.beta)*((h- self.h_d1) / self.Ts)
        self.h_d1 = h

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u








