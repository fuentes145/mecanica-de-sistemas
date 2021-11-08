import numpy as np
from tiempo import tiempo, dt
from funciones import integrar, transformar_coordenadas



# podira definir cada punto y cuerpo con sus nombres de biblioteca... en vola sirve despues
class Punto():
    def __init__(self):
        self.orientacion = list()
        self.trayectoria = list()
        
        
    def movimiento(self, r):
        self.trayectoria.append(r)

# el punto solo tiene la orientacion relativa a su SR anterior... es mas natural a como se resolveran problemas
    def rotacion(self, M):
        self.orientacion.append(M)

# las trayectorias y orientaciones se definen relativas al centro de gravedad.
# self.puntos es un diccionario con puntos de interes sobre el cuerpo
class Cuerpo_Rigido(Punto):
    def __init__(self, sr, masa, velocidad_inicial = np.array([0,0,0])):
        super().__init__()
        self.sr = sr
        self.m = masa
        #la velocidades se guardadan en cartecianas por ahora
        self.velocidad = [velocidad_inicial]
        self.aceleracion = list()
        self.cg = Punto()
        self.puntos = {'centro de gravedad': self.cg}
        
        self.F = list()

#recive fuerza y calcula su posicion en el siguiente instante 
# hay q entregar las fuerzas en cartecianas
    def fuerza(self, F):
        a = F/self.m
        v = self.velocidad[-1] + a*dt
        self.velocidad.append(v)
        r = transformar_coordenadas(self.trayectoria[-1], self.sr.sistema)
        r = r + v*dt
        self.trayectoria.append(transformar_coordenadas(r, 'cartesianas', self.sr.sistema))
        return F
    
    
        