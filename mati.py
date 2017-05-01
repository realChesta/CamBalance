import numpy as np
import scipy as sp


def math(x0, y0, x1, y1, dt, td):
    V0 = np.sqrt(np.square(x0-x1)+np.square(y0-y1))/dt
    X0 = np.sqrt(np.square(x1)+np.square(y1))
    a0 = np.arctan(x)
