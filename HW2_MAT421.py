# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 23:28:14 2022

@author: samie
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate 
def my_interp_plotter(x,y,X,option):
    kind = option
    plt.figure(figsize=(10,8))
    plt.plot(x,y,'ro',label="data")
    f=interpolate.interp1d(x,y,kind)
    Y=f(X)
    plt.plot(X,Y,"b",label=kind)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    if kind == "nearest":
        plt.title("nearest interpolation of data")
    elif kind=="linear":
        plt.title("linear interpolation of data")
    else:
        plt.title("cubic interpolation of data")
        plt.show()
        x=np.array([0,0.1,0.15,0.35,0.6,0.7,0.95,1])
        y=np.array([1,0.8187,0.7408,0.4966,0.3012,0.2466,0.1496,0.1353])
        #for kind in ['nearest','linear','spline']:
        my_interp_plotter(x,y,np.linspace(0,1,101),"nearest")
        my_interp_plotter(x,y,np.linspace(0,1,101),"linear")
        my_interp_plotter(x,y,np.linspace(0,1,101),"cubic")
