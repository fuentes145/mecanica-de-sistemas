from cuerpos import Punto
import numpy as np 
from abc import ABC, abstractmethod


class SR:
    def __init__(self, centro):
        self.objetos = list()
        self.p_cartesianas = list()
        self.p_cilindricas = list()
        self.O = np.array(centro)

    @abstractmethod
    def crear_punto(self, coordenadas, sistema='cartecianas'): 
        if sistema in ['cartecianas', 'cilindricas', 'esfericas']:
            p = Punto(coordenadas, sistema)
            self.objetos.append(p)
            
    @abstractmethod
    def puntos(self, sistema='cartecianas'):
        coordenadas = list()
        for p in self.objetos:
            if sistema==p.sistema:
                coordenadas.append(p.r)
            else:
                r = self.transfomar_coordenadas(p.r, p.sistema, sistema)
                coordenadas.append(list(r))
        return coordenadas
                
    @abstractmethod
    def distancia(self,p1,p2):
        return np.linalg.norm(p1.r-p2.r)
    

#falta esfericas
#recive coordenadas y entrega coordenadas. trabaja con arrays###
    @abstractmethod
    def transfomar_coordenadas(self, r, de, a='cartecianas'): #si viene de cartecianas solo la transforma pero si viene de otra la pasa a cartecianas y de forma recursiva vuelve a llamar a la funcion    
        if de == a:  
            return r
        
        elif de =='cartecianas' and a == 'cilindricas':

            z = r[2]
            ra = np.linalg.norm(r - self.O)
            teta = np.arctan(r[1]/r[0]) 
            r = np.array([ra,teta,z])
            return r 

        elif de =='cartecianas' and a == 'esfericas':
            ra = np.linalg.norm(r - self.O)
            teta = np.arctan(r[1]/r[0]) 
            r_xy = np.linalg.norm([r[0],r[1]])
            phi = np.arcsin(r_xy/ra)
            r = np.array([ra,teta,phi])
            return r
        
        elif de == 'cilindricas':
            x = np.cos(r[1])*r[0]
            y = np.sin(r[1])*r[0]
            z = r[2]
            r = np.array([x,y,z])
            return self.transfomar_coordenadas(r, 'cartecianas', a)
        
        elif de =='esfericas':
            z = np.cos(r[2])*r[0]
            r_xy = (r[0]**2-z**2)**(1/2)
            x = np.cos(r[1])*r_xy
            y = np.sin(r[1])*r_xy
            r = np.array([x,y,z])
            return self.transfomar_coordenadas(r, 'cartecianas', a)

        else:
            print('pifiaste')


class SRG(SR):
    def __init__(self):
        self.centro = Punto([0,0,0])
        super().__init__(self.centro)

# el centro es un objeto Punto
class SRL(SR):
    def __init__(self, centro):
        self.centro = centro
        super().__init__(self.centro.r)





"""
            if r[0] < 0 and r[1] > 0: #cuadrante 2
                teta = teta + np.pi
            elif r[0] < 0 and r[1] == 0:
                teta = np.pi
            elif r[0] > 0 and r[1] < 0: #cuadrante 4
                teta = 2*np.pi + teta
            elif r[0] < 0 and r[1] < 0: #cuadrante 3
                teta = np.pi + teta
            """
