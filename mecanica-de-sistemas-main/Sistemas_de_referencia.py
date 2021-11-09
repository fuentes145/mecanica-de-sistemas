from cuerpos import Punto
import numpy as np 
from abc import ABC, abstractmethod
from funciones import transformar_coordenadas, derivar, plot
from tiempo import tiempo, dt
from matrices_rotacion import R_x, R_y, R_z


class SRG():
    def __init__(self, sistema = 'cartesianas'):
        self.nombre = 'O'
        self.centro = Punto()
        map(self.centro.movimiento(np.array([0,0,0])), tiempo)
        self.objetos = {'centro': self.centro}
        self.sistema = sistema
        self.orientacion = [np.array([[1,0,0],[0,1,0],[0,0,1]]) for i in range(len(tiempo))]
                            
        
# si no especifico este punto va a estar quieto siempre
    def crear(self, nombre): 
        objeto = Punto()
        self.objetos[nombre] = objeto

    def agregar(self, nombre, objeto):
        self.objetos[nombre] = objeto
    

#podria hacer que solito busque como llegar hasta el sr0. o q sea otro metodo llamado ver global q busque la recursivamente los centros hasta q encuentre el sr0.
#especificar en el metodo que punto es el que quiero ver.    
#creo q esta funcion esta de mas por q podria solo ver el punto y chao
    def ver(self, nombre):
        objeto = self.objetos[nombre]
        coordenadas = list()
        for r in objeto.trayectoria:
            r = transformar_coordenadas(r, self.sistema)
            coordenadas.append(r)
        return coordenadas

#trabaja con objetos punto y no redefine su atributo trayectoria sino que retorna su trayectoria cambiada 
    def cambiar_sistema(self, p, transformar_a='cartesianas'): #si viene de cartesianas solo la transforma pero si viene de otra la pasa a cartesianas y de forma recursiva vuelve a llamar a la funcion    
        tra = list()    
        for i in p.trayectoria:
            tra.append(transformar_coordenadas(i, de=self.sistema, a=transformar_a))
        return tra
    

    def velocidad(self, nombre):
        trayec = self.cambiar_sistema(self.objetos[nombre])
        return derivar(trayec)
        
    def aceleracion(self, nombre):
        return derivar(self.velocidad(nombre))
    
    
    
    
# el centro es un SR Punto que hay que entregarle al SRL
# los puntos definidos en un sistema de referencia 'estan fijos a el' se mueven junto con el y rotan respecto a el si el rota 
class SRL(SRG):
    def __init__(self, SR_relativo, nombre_centro, sistema = 'cartesianas'):
        self.nombre = SR_relativo.nombre + nombre_centro
        self.sr_relativo = SR_relativo
        self.centro = self.sr_relativo.objetos[nombre_centro]
        self.sistema = sistema
        self.objetos = {'centro': self.centro}  
        self.orientacion = self.sr_relativo.orientacion
        



# si no llamo esta funcion mi SR va a tener la misma orientacion que tiene el SR con el cual fue definido
# si llamo esta funcion la orientacion del SR va a ser; la orientacion del SR antiguo punto M de orientacion del objeto centro
    def orientar(self):
        for i in range(len(tiempo)):    
            self.orientacion[i] = np.dot(self.orientacion[i], self.centro.orientacion[i])

# hacer que se defina en el sistema Sr_relativo
    def fu(self, nombre):
        R = list()
        B = self.cambiar_sistema(self.objetos[nombre])
        M = self.orientacion
        A = self.sr_relativo.cambiar_sistema(self.centro)
        for t in range(len(tiempo)):
            Mt = np.transpose(M[t])
            b = B[t]
            a = A[t]
            r = a + Mt.dot(b)
            R.append(r)
        R = [transformar_coordenadas(r, 'cartesianas', self.sr_relativo.sistema) for r in R]
        return R





#puntos_globales = list(map(lambda a, b: a+b, srb.ver('A'), srb.ver('centro') ))

'''
#ahora es solo una coordendada despues implementar para trayectoria
# tampoco utliza la orientacion asume que estan todos derechos

    def ver_origen(self, nombre):
        objeto = self.objetos[nombre]
        vector = [np.array([0,0,0]) for i in range(len(tiempo))]
        sr = self
        while sr.nombre != 'O':
            vector = list(map(lambda a,b: a+b, sr.cambiar_sistema(sr.centro), vector))
            sr = sr.sr_relativo
        tr = self.cambiar_sistema(objeto)
        tr = list(map(lambda a,b: a+b, tr, vector))     
        return tr


'''


