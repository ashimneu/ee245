#!/usr/bin/env python

import math
import numpy as np
from crazyflieParser import CrazyflieParser

if __name__ == '__main__':

    index = 1   # for cf1
    initialPosition = [0,1.5,0] # x,y,z coordinate for this crazyflie
    cfs = CrazyflieParser(index, initialPosition)
    cf = cfs.crazyflies[0]
    time = cfs.timeHelper

    cf.setParam("commander/enHighLevel", 1)
    cf.setParam("stabilizer/estimator", 2) # Use EKF
    cf.setParam("stabilizer/controller", 2) # Use mellinger controller
    #cf.setParam("ring/effect", 7)

    cf.takeoff(targetHeight = 0.5, duration = 3.0)
    time.sleep(3.0)

    # FILL IN YOUR CODE HERE
    # Please try both goTo and cmdPosition

    # Figure 8 curve
    def figEight(n,a):
        # n - number of way points along 8 curve
        # a - quasi radius
        time = np.linspace(0,2*np.pi,n)
        x = a*np.sin(time)
        y = a*np.sin(time)*np.cos(time)
        z = np.zeros(1,n)
        wpTemp = np.stack((x,y,z))
        wp = np.zeros(3,n)
        for i in range(len(x)):
            wp[0,i] = wpTemp[0][i]
            wp[1,i] = wpTemp[1][i]
            wp[2,i] = wpTemp[2][i]
        return wp

    n = 20
    a = 0.5
    d1 = 3.0
    EightCurve = figEight(n,a)
    cf.goTo(goal = EightCurve[0], yaw = 0.0, duration=d1)
    time.sleep(d1)

    for i in range(len(EightCurve)):

        cf.cmdPosition(pose = EightCurve[i], yaw = 0.0)












    

    cf.land(targetHeight = 0.0, duration = 5.0)
    time.sleep(5.0)
