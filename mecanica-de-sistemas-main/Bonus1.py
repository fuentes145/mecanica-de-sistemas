#Testing
import numpy as np
from matrices_rotacion import *

# Si bien no este codigo no es una funcion sino que recibe inputs y el archivo .txt como variables. Entonces aún cumple con las indicaciones.



# se comienza por transformar el archivo .STP en uno .STL en la siguiente página: https://anyconv.com/stp-to-stl-converter/
# Luego se usa la página https://drububu.com/miscellaneous/voxelizer/?out=obj para transformar la figura en N pequeños cubos de masa M/N.
# Se importa el el archivo y se aplica la ecuacion para los centros de masa y tensor de inercia
# asumiendo una masa de 1

masa=float(input())
coords = np.loadtxt('.txt', unpack=True, delimiter=',', dtype=int)
x, y, z  = coords
numero_ele=len(x)
mc=masa/numero_ele
Ix = mc*sum(coords[1]**2 + coords[2]**2)/numero_ele
Iy = mc*sum(coords[0]**2 + coords[2]**2)/numero_ele
Iz = mc*sum(coords[0]**2 + coords[1]**2)/numero_ele
Ixy = -sum(mc*coords[0]*coords[1])/numero_ele
Iyz = -sum(mc*coords[1]*coords[2])/numero_ele
Ixz = -sum(mc*coords[0]*coords[2])/numero_ele

#a)
centro_de_masa=np.array([Ix,Iy,Iz])
#b)
tensor_de_inercia= np.array([[Ix, Ixy, Ixz],[Ixy, Iy, Iyz],[Ixz, Iyz, Iz]])
#c) dado un punto cualquiera
pto=int(input())
pos=np.array([x[pto],y[pto],z[pto]])
r=pos-centro_de_masa
#por teorema de steiner M*R^2, pero para que R sea una matriz se utiliza producto punto,se multiplica 
# por la identidad y se resta el producto exterior
out=masa*(r.dot(r)*np.eye(3)-np.outer(r,r))
nuevoI=tensor_de_inercia+out
#d)Para rotar la matriz de inercia se usa multiplicacion matricial por la matriz de rotacion querida y du transpuesta a ambos lados
angulo=float(input)
Irotado=R_x(angulo).dot(nuevoI.dot(R_x(angulo).transpose())) #para una rotacion de pi respecto al eje x. Se las matrices de rotacion propias

#e) Para encontrar los ejes principales se usa su definicion como una matriz con valor I en cada entrada diagonal y 0 en las otras.
#Con esto se puede plantear la ecuacion caracteristica (Momento de inercia - I)x=0. Entonces se buscan los valores propios
eje_principal1=np.eye(3).dot(np.linalg.eig(tensor_de_inercia)[0][0])
eje_principal2=np.eye(3).dot(np.linalg.eig(tensor_de_inercia)[0][1])
eje_principal3=np.eye(3).dot(np.linalg.eig(tensor_de_inercia)[0][2])


#PIEZA 1
masa=1
coords = np.loadtxt('p1.txt', unpack=True, delimiter=',', dtype=int)
x, y, z  = coords
numero_ele=len(x)
mc=masa/numero_ele
Ix = mc*sum(coords[1]**2 + coords[2]**2)/numero_ele
Iy = mc*sum(coords[0]**2 + coords[2]**2)/numero_ele
Iz = mc*sum(coords[0]**2 + coords[1]**2)/numero_ele
Ixy = -sum(mc*coords[0]*coords[1])/numero_ele
Iyz = -sum(mc*coords[1]*coords[2])/numero_ele
Ixz = -sum(mc*coords[0]*coords[2])/numero_ele

#a)
centro_de_masa=np.array([Ix,Iy,Iz])
#b)
tensor_de_inercia= np.array([[Ix, Ixy, Ixz],[Ixy, Iy, Iyz],[Ixz, Iyz, Iz]])
#c)
pto=11+1
pos=np.array([x[pto],y[pto],z[pto]])
r=pos-centro_de_masa
out=masa*(r.dot(r)*np.eye(3)-np.outer(r,r))
nuevoI=tensor_de_inercia+out
#d)
Irotado=R_x(np.pi).dot(nuevoI.dot(R_x(np.pi).transpose()))
#e)
eje_principal1=np.eye(3).dot(np.linalg.eig(tensor_de_inercia)[0][0])
eje_principal2=np.eye(3).dot(np.linalg.eig(tensor_de_inercia)[0][1])
eje_principal3=np.eye(3).dot(np.linalg.eig(tensor_de_inercia)[0][2])
####
#PIEZA 3

masa=1
coords = np.loadtxt('p3.txt', unpack=True, delimiter=',', dtype=int)
x, y, z  = coords
numero_ele=len(x)
mc=masa/numero_ele
Ix = mc*sum(coords[1]**2 + coords[2]**2)/numero_ele
Iy = mc*sum(coords[0]**2 + coords[2]**2)/numero_ele
Iz = mc*sum(coords[0]**2 + coords[1]**2)/numero_ele
Ixy = -sum(mc*coords[0]*coords[1])/numero_ele
Iyz = -sum(mc*coords[1]*coords[2])/numero_ele
Ixz = -sum(mc*coords[0]*coords[2])/numero_ele

#a)
centro_de_masa=np.array([Ix,Iy,Iz])
#b)
tensor_de_inercia= np.array([[Ix, Ixy, Ixz],[Ixy, Iy, Iyz],[Ixz, Iyz, Iz]])
#c) dado un punto cualquiera, por ejemplo, el onceavo cubo:
pto=11+1
pos=np.array([x[pto],y[pto],z[pto]])
r=pos-centro_de_masa
#por teorema de steiner M*R^2, pero para que R sea una matriz se utiliza producto punto,se multiplica 
# por la identidad y se resta el producto exterior
out=masa*(r.dot(r)*np.eye(3)-np.outer(r,r))
nuevoI=tensor_de_inercia+out
#d)Para rotar la matriz de inercia se usa multiplicacion matricial por la matriz de rotacion querida y du transpuesta a ambos lados
Irotado=R_x(np.pi).dot(nuevoI.dot(R_x(np.pi).transpose())) #para una rotacion de pi respecto al eje x. Se las matrices de rotacion propias

#e) Para encontrar los ejes principales se usa su definicion como una matriz con valor I en cada entrada diagonal y 0 en las otras.
#Con esto se puede plantear la ecuacion caracteristica (Momento de inercia - I)x=0. Entonces se buscan los valores propios
eje_principal1=np.eye(3).dot(np.linalg.eig(tensor_de_inercia)[0][0])
eje_principal2=np.eye(3).dot(np.linalg.eig(tensor_de_inercia)[0][1])
eje_principal3=np.eye(3).dot(np.linalg.eig(tensor_de_inercia)[0][2])