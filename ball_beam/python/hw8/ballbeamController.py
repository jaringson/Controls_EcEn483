import ballbeamParamHW8 as P
import sys
sys.path.append('..')  # add parent directory
import ballbeamParam as P0
from PDControl import PDControl

class ballbeamController:
    ''' 
        This class inherits other controllers in order to organize multiple controllers.
    '''

    def __init__(self):
        # Instantiates the SS_ctrl object
        self.zCtrl = PDControl(P.kp_z, P.kd_z, P.F_max, P.beta, P.Ts)
        self.thetaCtrl = PDControl(P.kp_th, P.kd_th, P.theta_max, P.beta, P.Ts)

    def u(self, y_r, y):
        # y_r is the referenced input
        # y is the current state
        z_r = y_r[0]
        z = y[0]
        theta = y[1]
        theta_r = y_r[0]
        # the reference angle for theta comes from the outer loop PD control
        #theta_r_tilde = self.zCtrl.PD(z_r, z, flag=False)
        #theta_r_e = 0
        #theta_r = theta_r_e + theta_r_tilde
        # the force applied to the cart comes from the inner loop PD control
        F_tilde = self.thetaCtrl.PD(theta_r, theta, flag=True)
        F_e = P0.m2*P0.g/2
        F = F_e + F_tilde



        return [F]







