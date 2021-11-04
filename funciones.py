# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:25:38 2021

@author: pipe
"""
import numpy as np
import matplotlib.pyplot as plt
from tiempo import tiempo, dt




#deriva numericamente una lista de numeros respecto a un delta t
def derivar(puntos):  
    vel = list()
    for i in range(len(puntos)-1):
        v = (puntos[i+1]-puntos[i]) / dt
        vel.append(v)
    return vel

#recive coordenadas y entrega coordenadas. trabaja con arrays###
#si viene de cartecianas solo la transforma pero si viene de otra la pasa 
#a cartecianas y de forma recursiva vuelve a llamar a la funcion
def transformar_coordenadas(r, de, a='cartecianas'):


    if de == a:  
        return r
    
    elif de =='cartecianas' and a == 'cilindricas':
        z = r[2]
        ra = np.linalg.norm(r)
        teta = np.arctan(r[1]/r[0]) 
        if r[0]<0:
            teta += np.pi
        r = np.array([ra,teta,z])
        return r 

    elif de =='cartecianas' and a == 'esfericas':
        ra = np.linalg.norm(r)
        teta = np.arctan(r[1]/r[0])
        if r[0]<0:
            teta += np.pi
        r_xy = np.linalg.norm([r[0],r[1]])
        phi = np.arcsin(r_xy/ra)
        r = np.array([ra,teta,phi])
        return r
    
    elif de == 'cilindricas':
        x = np.cos(r[1])*r[0]
        y = np.sin(r[1])*r[0]
        z = r[2]
        r = np.array([x,y,z])
        return transformar_coordenadas(r, 'cartecianas', a)
    
    
    elif de =='esfericas':
        x = np.sin(r[2])*np.cos(r[1])*r[0]
        y = np.sin(r[2])*np.sin(r[1])*r[0]
        z = np.cos(r[2])*r[0]
        r = np.array([x,y,z])
        return transformar_coordenadas(r, 'cartecianas', a)

    else:
        print('pifiaste')

# hay q entregar todo en cartecianas, el metodo 'puntos' se encarga de esto
# buscar otra libreria mas pro...
# hay q definir la de tal manera q yo entregue cierto SR y los nombres de lo que quiero plotear
#   luego el .r va a ser mas grande los puntos .trayectoria y los objetos tambien son de otro color
def plot(puntos):
    X = [p[0] for p in puntos]
    Y = [p[1] for p in puntos]
    Z = [p[2] for p in puntos]
        
    fig = plt.figure(figsize=(17,12))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X,Y,Z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    maxx = max(X) - min(X)
    if maxx<0.5:
        plt.xlim([min(X)-0.5,  max(X)+0.5])
    maxy = max(Y) - min(Y)
    if maxy<0.5:
        plt.ylim([min(Y)-0.5,  max(Y)+0.5])
    maxz = max(Z) - min(Z)
    if maxz<0.5:
        print('si fallo el grafico es por q en z varia poco')
    plt.show()
    
r = np.array([-1,-1,0])
print(transformar_coordenadas(r, 'cartecianas', a='esfericas'))
r =transformar_coordenadas(r, 'cartecianas', a= 'esfericas')
print(transformar_coordenadas(r, 'esfericas', a='cartecianas'))
    
'''
    
'''
    