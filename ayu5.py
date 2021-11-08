# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 08:58:46 2021

@author: Felipe
"""

from Sistemas_de_referencia import SRG, SRL
from cuerpos import Punto, Cuerpo_Rigido
import numpy as np
from funciones import plot, transformar_coordenadas, derivar, integrar
from matrices_rotacion import *
from tiempo import tiempo, dt
import sympy as sp


sr0 = SRG('cilindricas')
m = 1
g = 9.81
R = 1
sr0.crearc('A', m)

teta_inicial = 0


posicion_inicial = np.array([R, teta_inicial, 0])
sr0.objetos['A'].trayectoria.append(posicion_inicial)

angulos = [teta_inicial] 

def tencion(teta):
    return np.abs(3*m*g*np.sin(teta))

def fneta(teta):
    return [-tencion(teta), -m*g*np.cos(teta), 0]
            

for t in tiempo:
    #sr0.objetos['A'].trayectoria[-1][0] = 1
    f = fneta(angulos[-1])
    print(f)
    f = Mcilindricas(angulos[-1]).dot(f) 
    sr0.objetos['A'].fuerza(f)
    angulos.append(sr0.objetos['A'].trayectoria[-1][1])

plot(sr0.ver('A'))


'''
np.linspace(np.deg2rad(-90), np.deg2rad(90))
p = np.linspace(3, 10)
val = balanceo(p)
print(val)
'''
    
    