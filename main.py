from Sistemas_de_referencia import SRG, SRL
from cuerpos import Punto
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

t = 100
radios = np.linspace(1, 1, t)
angulosteta = np.linspace(0, 3*np.pi/2, t)
angulosphi = np.linspace(np.pi/2, np.pi/2, t)





def plot(puntos):
    X = [p[0] for p in puntos]
    Y = [p[1] for p in puntos]
    Z = [p[2] for p in puntos]
        
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X,Y,Z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
    

if __name__ == "__main__":
    print("Cinematica de sistemas mecanicos") 
    
    sr0 = SRG()
    
    for i in range(t):
        r = radios[i]
        teta = angulosteta[i]
        phi = angulosphi[i]
        sr0.crear_punto([r, teta, phi], 'esfericas')
    
    puntos = sr0.puntos()
    plot(puntos)


