import numpy as np
from tiempo import tiempo, dt

# despues con kuargs o args ver el tipo de coordenadas q se entrega dependiendo del tipo
#no se como armar el contador de puntos... c para los id
class Punto():
    def __init__(self):
        self.orientacion = list()
        self.trayectoria = list()
        
    def movimiento(self, r):
        self.trayectoria.append(r)

# el punto solo tiene la orientacion relativa... es mas natural a como se resolveran problemas
    def rotacion(self, M):
        self.orientacion.append(M)



class Cuerpos_Rigidos():
    inercia = None
    orientacion = [0,0,0]
    def __init__(self, centro_gravedad , masa):
        self.cg = np.array(centro_gravedad)
        self.m = masa
        self.o = orientacion # angulos de euler
        self.I = inercia
        
    def aplicar_fuerza(self, F):
        pass
        