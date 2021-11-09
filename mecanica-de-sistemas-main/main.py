import numpy as np
from tiempo import t, dt


    
if __name__ == "__main__":
    print("Cinematica de sistemas mecanicos") 
    
    sr0.crear('B', [0, 0, np.pi/2])
    srb = SRL(sr0, 'B', 'cilindricas')
    srb.crear('A', [2, 0, 2])
    
    for t in tiempo:
        srb.objetos['A'].trayectoria.append(np.array([1, np.pi*t, 2]))
        sr0.objetos['B'].trayectoria.append(np.array([2, 0, np.pi*3/2+t*np.pi/8]))




