#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Tarea 3.6
"""a) tomando en cuenta a mano los resultados de cada ciclo se puede deducir que para tal "n",
los resultados concuerdan en un patron. Siendo este de SUMATORIA GAUSSIANA para la suma
y SUMATORIA GAUSSIANA para las multiplicaciones tambien, solamente que se le resta un "1" al resultado"""

"""#b) se puede reducir la cantidad de operaciones respectivas a la serie completa, modificando unicamente
la posicion de la sumatoria: ΣAiBj --> ΣAiΣBj
De esta manera en vez de describirse como una SUMATORIA GAUSSIANA, se describe con un continuo "n" de multiplicaciones 
para la suma, y el mismo caso para las multiplicaciones pero con un "1" menos tambien """

"""c) Si corremos el algoritmo para los dos casos de series, con "n = 10000", el codigo corresponde a : """

#Caso 1
import matplotlib.pyplot as plt #Importamos las herramientas necesarias
import numpy as np
n = input("ingresar numero para calcular sum: ") #piden un valor de "n" exacto pero aqui se da 
#lugar a indagar con cualquier valor
n = int (n)
A = np.random.rand(n) #Representa la dimensión de el 
#array de salida de la función aleatoria. Si no se especifica ningún valor, se devuelve un valor escalar.
B = np.random.rand(n)
sum = 0
for i in range(1, n):
    for j in range(1, i+1):
        sum += A[i]*B[j]

print("SUM hasta n=", n, "es: ", sum )


# In[7]:


#Caso 2
import matplotlib.pyplot as plt 
import numpy as np
n = input("ingresar numero para calcular sum: ") 
n = int (n)
A = np.random.rand(n) 
B = np.random.rand(n)
sum = 0 

for i in range(len(B)+1): # len da lugar a los elementos del arreglo
    sum += (B[:i].sum())*(A[i-1]) 
print("SUM hasta n=", n, "es: ", sum )


# In[ ]:


#Los valores son similares, con un margen de error casi infimo.

# Calificación: 7.0