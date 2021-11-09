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
    vel.append(vel[-1])
    return vel

def integrar(puntos):
    pos = [0]
    for i in range(len(puntos)-1):
        dx = puntos[i+1]*dt+pos[i]
        pos.append(dx)
    return pos



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

# hay q entregar todo en cartesianas, el metodo 'puntos' se encarga de esto
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
    
r = np.array([ 1.41421356, -2.35619449  ,1.57079633])

def momento_de_inercia(forma: str,masa,radio=0,altura=0):
    if forma=="esfera":
        i=np.array([[2/5*masa*radio**2,0,0],[0,2/5*masa*radio**2,0],[0,0,2/5*masa*radio**2]])
    if forma=="cono":
        i=np.array([[3/20*masa*(radio**2+4*altura**2),0,0],[0,3/20*masa*(radio**2+4*altura**2),0],[0,0,3/10*masa*radio**2]])
    if forma=="cilindro":
        i=np.array([[1/12*masa*(altura**2+3*radio**2),0,0],[0,1/12*masa*(altura**2+3*radio**2),0],[0,0,1/2*masa*radio**2]])
    
    
    return i
'''
    
'''