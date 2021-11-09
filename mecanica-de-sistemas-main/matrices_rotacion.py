# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:25:38 2021

@author: pipe
"""
import numpy as np

# para hacer una rotacion compuesta estas se pueden ir multiplicando, 
#el orden importa en las rotaciones y tambien en la multiplicacion de matrices

# las matrices de transformacion son ortonormales y unitarias por lo tanto la inversa
# es igual a la traspuesta, entonces transpongo y multiplico para debolver la transformacion


def R_x(o):
    return np.array([ [1, 0, 0], [0, np.cos(o), -np.sin(o)], [0, np.sin(o), np.cos(o)]])

def R_y(o):
    return np.array([ [np.cos(o), 0, np.sin(o)], [0, 1, 0], [-np.sin(o), 0, np.cos(o)]])

def R_z(o):
    return np.array([[np.cos(o), -np.sin(o), 0], [np.sin(o), np.cos(o), 0], [0, 0, 1]])

