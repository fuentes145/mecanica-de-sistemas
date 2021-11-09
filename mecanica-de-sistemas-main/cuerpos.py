import numpy as np
from tiempo import tiempo, dt
from funciones import derivar, integrar

# despues con kuargs o args ver el tipo de coordenadas q se entrega dependiendo del tipo
#no se como armar el contador de puntos... c para los id
class Punto():
    def __init__(self,masa=1):
        self.orientacion = list()
        self.trayectoria = list()
        self.masa=masa
        self.velocidad = list()
        self.aceleracion = list()
        self.Fneta=[[]]
        
        
    def movimiento(self, r, tipo="posicion"):
        if tipo=='posicion':
            self.trayectoria.append(r)
            if len(self.trayectoria)==len(tiempo):
                self.velocidad=derivar(self.trayectoria)
                self.aceleracion=derivar(self.velocidad)
        elif tipo=='velocidad':
            self.velocidad.append(r)
            if len(self.velocidad)==len(tiempo):
                self.trayectoria=integrar(self.trayectoria)
                self.aceleracion=derivar(self.velocidad)
        elif tipo=='aceleracion':
            self.aceleracion.append(r)
            if len(self.aceleracion)==len(tiempo):
                self.velocidad=integrar(self.aceleracion)
                self.trayectoria=integrar(self.velocidad)
        else:
            print("escribiste mal")

            
    def agregar_fuerza(self,fuerza: np.array):
        a=len(self.Fneta)-1
        if len(self.Fneta[a])<len(tiempo):
            self.Fneta[a].append(fuerza)

        else: 
            self.Fneta.append(np.array(np.array([])))
            self.Fneta[a+1]=np.append(self.Fneta[a+1],(fuerza))
        

    
    def aplicar_Fneta(self):
        aceleracion=sum(self.Fneta)/self.masa
        if len(self.aceleracion)==len(tiempo):
            self.aceleracion+=aceleracion #Ojo que esta con += esto es por si ya se estaba moviendo y luego se agrega una fuerza
        self.velocidad+=integrar(self.aceleracion) 
        self.trayectoria+=integrar(self.velocidad)



# el punto solo tiene la orientacion relativa... es mas natural a como se resolveran problemas
    def rotacion(self, M):
        self.orientacion.append(M)


class Cuerpos_Rigidos():
    inercia = None
    orientacion = [0,0,0]
    def __init__(self, centro_gravedad , masa):
        self.cg = np.array(centro_gravedad)
        self.m = masa
        #self.o = orientacion # angulos de euler
        #self.I = inercia
        
    def aplicar_fuerza(self, F):
        pass
        