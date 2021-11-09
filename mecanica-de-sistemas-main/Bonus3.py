from Sistemas_de_referencia import SRG, SRL
from cuerpos import Punto
import numpy as np
from funciones import plot, transformar_coordenadas, derivar
from matrices_rotacion import *
from tiempo import tiempo, dt
#Dimensiones
masa_disco=19
r_disco=0.1
distancia_barra=1
r_barra=0.025
p0=np.array([r_barra,0,np.pi/4])
#sistemas
sr0=SRG()
sr0.crear('A')
sr1=SRL(sr0,'A','cilindricas')



#Inercias
momento=masa_disco*r_disco**2*1/2+1**2*masa_disco

#Fuerzas y torques
def grav():
    return np.array([9.8, 0.,3.14159265])
# print(np.cross(grav,p0))
# np.cross()
for t in tiempo:
    sr0.objetos["A"].rotacion(t)
print(sr0.objetos['A'].orientacion[3])
#plot(sr0.objetos['A'].orientacion)


