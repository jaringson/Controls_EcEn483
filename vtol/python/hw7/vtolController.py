import numpy as np
import vtolParamHW7 as P
import sys
sys.path.append('..')  # add parent directory
import vtolParam as P0
from PDControl import PDControl


class vtolController:

    def __init__(self):
        # Instantiates the PD object
        self.thetaCtrl = PDControl(P.kp, P.kd, P0.F_max, P.beta, P.Ts)
        self.limit = P0.F_max

    def u(self, y_r, y):
        # y_r is the referenced input
        # y is the current state
        z_r = y_r[0]
        z = y[0]

        # compute equilibrium torque tau_e
        F_e = P0.k * z
        # compute the linearized torque using PD
        F_tilde = self.thetaCtrl.PD(z_r, z, False)
        # compute total torque
        F = F_e + F_tilde
        F = self.saturate(F)
        return [F]

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u







