from Sistemas_de_referencia import SRG, SRL
from cuerpos import Punto
import numpy as np
from funciones import plot, transformar_coordenadas, derivar, integrar
from matrices_rotacion import *
from tiempo import tiempo, dt

#defino el SRG
sr0 = SRG('esfericas')
#defino ecuaciones de movimiento
def  s(t):
    return 2-0.05*t**2 

# creo sistemas de referencia y puntos necesario del problema.
sr0.crear('B')
srb = SRL(sr0, 'B', 'cilindricas')
srb.crear('A')


#defino trayectorias y orientaciones
for t in tiempo:
    srb.objetos['A'].movimiento(np.array([1, t*np.pi, 2]))
    sr0.objetos['B'].movimiento(np.array([2, np.pi, np.pi/2-t*np.pi/8]))
    sr0.objetos['B'].rotacion(R_y(-np.pi*t/8))
    
srb.orientar() # aca hago q srb vaya cambiando su orientacion con el punto B

#ocupo el codigo para resolver el problema...
sr0.crear('A')
sr0.objetos['A'].trayectoria = srb.fu('A')



#respuestas 
plot(sr0.ver('A'))
vel = sr0.velocidad('A')
#plot(vel)
pos = integrar(vel, np.array([-1,0,2]))
plot(pos)
#plot(sr0.aceleracion('A'))

'''
plot(srb.velocidad('A'))
plot(srb.aceleracion('A'))
'''





