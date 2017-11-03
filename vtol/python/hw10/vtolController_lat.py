import vtolParamHW10_8 as P
import sys
sys.path.append('..')  # add parent directory
import vtolParam as P0
from PIDControl import PIDControl
import numpy as np

class vtolController_lat:
    ''' 
        This class inherits other controllers in order to organize multiple controllers.
    '''

    def __init__(self):
        # Instantiates the SS_ctrl object
        self.zCtrl = PIDControl(P.kp_z, P.ki_z, P.kd_z, P.tau_max, P.beta, P.Ts)
        self.thetaCtrl = PIDControl(P.kp_th, 0.0, P.kd_th, P.theta_max, P.beta, P.Ts)
        self.limit = P.tau_max

    def u(self, y_r, y):
        # y_r is the referenced input
        # y is the current state
        z_r = y_r[0]
        z = y[0]
        theta = y[2]
        
        # the reference angle for theta comes from the outer loop PD control
        theta_r_tilde = self.zCtrl.PID(z_r, z, flag=False)
        theta_r_e = 0
        theta_r = theta_r_e + theta_r_tilde

        # the force applied to the cart comes from the inner loop PD control
        tau_tilde = self.thetaCtrl.PD(theta_r, theta, flag=False)
        tau_e = 0
        tau = tau_e + tau_tilde


        tau = self.saturate(tau)
        return [tau]

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u





