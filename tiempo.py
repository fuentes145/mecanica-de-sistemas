# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 01:22:46 2021

@author: Felipe

"""

segundo_final = 10
frames = 1000

import numpy as np

class Tiempo():
    def __init__(self, tiempo_final, frames):
        self.t = np.linspace(0, tiempo_final, frames)
        self.dt = self.t[1]-self.t[0]
        
instacia_tiempo = Tiempo(segundo_final, frames)

tiempo = instacia_tiempo.t
dt = instacia_tiempo.dt



