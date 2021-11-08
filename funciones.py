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
    derivada = list()
    for i in range(len(puntos)-1):
        d = (puntos[i+1]-puntos[i]) / dt
        derivada.append(d)
    return derivada

#integra numericamente una lista de numeros respecto a un delta t
def integrar(puntos, inicial):
    integrada = [inicial]
    for i in range(len(puntos)-1):
        a = puntos[i+1] * dt + integrada[i]
        integrada.append(a)
    return integrada

#recive coordenadas y entrega coordenadas. trabaja con arrays###
#si viene de cartesianas solo la transforma pero si viene de otra la pasa 
#a cartesianas y de forma recursiva vuelve a llamar a la funcion
def transformar_coordenadas(r, de, a='cartesianas'):
    if de == a:  
        return r
    
    elif de =='cartesianas' and a == 'cilindricas':
        x,y,z = r
        ra = np.sqrt(x**2+y**2)  
        teta = np.arctan2(r[1],r[0]) 
        r = np.array([ra,teta,z])
        return r 

    elif de =='cartesianas' and a == 'esfericas':
        x,y,z = r
        ra = np.linalg.norm(r)
        teta = np.arctan2(y,x)
        r_xy = np.linalg.norm([x,y])
        phi = np.arctan2(r_xy,z)
        r = np.array([ra,teta,phi])
        return r
    
    elif de == 'cilindricas':
        x = np.cos(r[1])*r[0]
        y = np.sin(r[1])*r[0]
        z = r[2]
        r = np.array([x,y,z])
        return transformar_coordenadas(r, 'cartesianas', a)
    
    
    elif de =='esfericas':
        x = np.sin(r[2])*np.cos(r[1])*r[0]
        y = np.sin(r[2])*np.sin(r[1])*r[0]
        z = np.cos(r[2])*r[0]
        r = np.array([x,y,z])
        return transformar_coordenadas(r, 'cartesianas', a)

    else:
        print('pifiaste')

print(transformar_coordenadas(np.array([-0.0, -9.81, 0]), 'cilindricas'))
# hay q entregar todo en cartesianas, el metodo 'ver' se encarga de esto
# hay q definir la de tal manera q yo entregue cierto SR y los nombres de lo que quiero plotear
# el primer punto hacer lo otro color y los objetos tambien son de otro color
# buscar como hacer q mantengan las proporciones
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
    



'''
    
'''