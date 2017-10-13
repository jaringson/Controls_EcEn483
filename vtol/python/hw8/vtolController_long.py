import numpy as np
import vtolParamHW7 as P
import sys
sys.path.append('..')  # add parent directory
import vtolParam as P0
from PDControl import PDControl


class vtolController_long:

    def __init__(self):
        # Instantiates the PD object
        self.hCtrl = PDControl(P.kp, P.kd, P0.F_max, P.beta, P.Ts)
        self.limit = P0.F_max

    def u(self, y_r, y):
        # y_r is the referenced input
        # y is the current state
        h_r = y_r[0]
        h = y[1]

        # compute equilibrium force F_e
        F_e = (P0.mc + P0.mr + P0.ml) * P0.g
        # compute the linearized force using PD
        F_tilde = self.hCtrl.PD(h_r, h, False)
        # compute total force
        F = F_e + F_tilde
        F = self.saturate(F)
        return [F]

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u








