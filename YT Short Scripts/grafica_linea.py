#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 10:41:36 2021
Para los shorts Diarios de mision codigo

@author: Dany Jacquez

Como hacer una simple grafica de linea
"""

# Paso 1: Importar modulo pyplot de matplotlib
# si no lo tienes solo usa esta linea en una terminal para instalarlo
# pip install matplotlib

import matplotlib.pyplot as plt


# Paso 2: Definir los datos que vamos a graficar
# Para esto definiremos 2 listas

x = [1, 5, 6, 7, 10, 15, 30]
y = [30, 12, 100, 75, 9, 58, -5]

# Paso 3: Hacer la grafica
plt.plot(x, y)

#Paso 4: Mostrar la grafica
#plt.show()


# Bonus: Vamos a poner informacion en los ejes y un titulo a la grafica
plt.title("Suscribete al canal para mas tips de PYTHON")
plt.xlabel("Dia")
plt.ylabel("Ganancias")

plt.show()

