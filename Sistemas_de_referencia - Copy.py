from cuerpos import Punto
import numpy as np 
from abc import ABC, abstractmethod



class SR:
    def __init__(self, centro):
        self.objetos = list()
        self.p_cartesianas = list()
        self.p_cilindricas = list()
        self.O = centro.r

    @abstractmethod
    def agregar(self, p): 
        self.objetos.append(p)

    @abstractmethod
    def ver(self, sistema):
        if sistema == "cartecianas":
            [print(p.r) for p in self.objetos]
        elif sistema == "cilindricas":
            [print(self.cilindricas(p)) for p in self.objetos]
        else:
            print("eskribe vien la wea")

    @abstractmethod
    def distancia(self,p1,p2):
        return np.linalg.norm(p1.r-p2.r)
    @abstractmethod
    def modulo(self, p):
        return np.linalg.norm(p.r - self.O)

    @abstractmethod
    def cilindricas(self, p):
        z = p.r[2]
        r = self.modulo(p)
        teta = np.arctan(p.r[1]/p.r[0]) #teta en radianes
        #arreglar para q siempre los angulos sean postivos
        if p.r[0] < 0 and p.r[1] > 0: #cuadrante 2
                teta = teta + np.pi
        elif p.r[0] < 0 and p.r[1] == 0:
            teta = np.pi
        elif p.r[0] > 0 and p.r[1] < 0: #cuadrante 4
            teta = 2*np.pi + teta
        elif p.r[0] < 0 and p.r[1] < 0: #cuadrante 3
            teta = np.pi + teta
        return np.array([r,teta,z])

class SRG(SR):
    def __init__(self):
        self.centro = Punto(0,0,0)
        super().__init__(self.centro)

class SRL(SR):
    def __init__(self, punto):
        self.centro = punto
        super().__init__(self.centro)







