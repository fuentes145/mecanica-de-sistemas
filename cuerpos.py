import numpy as np


class Punto():
    def __init__(self, x, y, z):
        self.r = np.array([x, y, z])


 
class Cuerpos_Rigidos():
    inercia = None
    orientacion = [0,0,0]
    def __init__(self, centro_gravedad , masa):
        self.cg = np.array(centro_gravedad)
        self.m = masa
        self.o = orientacion
        self.I = inercia










