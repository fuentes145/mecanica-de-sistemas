from Sistemas_de_referencia import SRG, SRL
from cuerpos import Punto
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Cinematica de sistemas mecanicos") 
    
    sr0 = SRG()

    punto1 = Punto(-1,1,2) 
    punto2 = Punto(3,3,7)
    sr1 = SRL(punto1)

    sr0.agregar(punto1)
    sr0.agregar(punto2)
    sr0.ver("cilindricas")