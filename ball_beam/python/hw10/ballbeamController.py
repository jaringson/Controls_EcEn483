import ballbeamParamHW10 as P
import sys
sys.path.append('..')  # add parent directory
import ballbeamParam as P0
from PIDControl import PIDControl
import numpy as np

class ballbeamController:
    ''' 
        This class inherits other controllers in order to organize multiple controllers.
    '''

    def __init__(self):
        # Instantiates the SS_ctrl object
        self.zCtrl = PIDControl(P.kp_z, P.ki_z, P.kd_z, P.F_max, P.beta, P.Ts)
        self.thetaCtrl = PIDControl(P.kp_th, P.ki_th, P.kd_th, P.theta_max, P.beta, P.Ts)
        self.limit = P.F_max

    def u(self, y_r, y):
        # y_r is the referenced input
        # y is the current state
        z_r = y_r[0]
        z = y[0]
        theta = y[1]
        
        # the reference angle for theta comes from the outer loop PD control
        theta_r = self.zCtrl.PID(z_r, z, flag=False)

        # the force applied to the cart comes from the inner loop PD control
        F_tilda = self.thetaCtrl.PID(theta_r, theta, flag=False)
        F_e = (P0.m1*P0.g*1.0*z/ P0.l) + P0.m2*P0.g/2.0 
        F = F_e + F_tilda


        F = self.saturate(F)
        return [F]

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u






