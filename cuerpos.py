import numpy as np


# despues con kuargs o args ver el tipo de coordenadas q se entrega dependiendo del tipo
class Punto():
    def __init__(self, coordenadas, sistema='cartecianas'):
        self.sistema = sistema
        self.r = np.array([coordenadas[0], coordenadas[1], coordenadas[2]])


class Cuerpos_Rigidos():
    inercia = None
    orientacion = [0,0,0]
    def __init__(self, centro_gravedad , masa):
        self.cg = np.array(centro_gravedad)
        self.m = masa
        self.o = orientacion
        self.I = inercia