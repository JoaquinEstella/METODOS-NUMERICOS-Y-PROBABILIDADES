#!/usr/bin/env python
# coding: utf-8

# In[12]:


"""Importamos"""
import matplotlib.pyplot as plt                                 
import numpy as np


"""Definimos la función de Poisson"""

def poisson(n, lamda):
    return lamda**n*np.exp(-lamda)/np.math.factorial(n)         

"""Numero maximo de estrellas a observar"""

print('Sea un numero maximo de estrellas :')                             
λ=int(input("λ="))                                                    

"""Array de estrellas a observar desde 0 a n"""

n=np.arange(0,λ+1,1)      

"""Creamos otro array con las probabilidades de observar la cantidad -n- de estrellas"""
p=np.array([poisson(n, 15.7/2)for n in range(λ+1)])             
    
print("La distribución de probabilidad en observar estas", λ," estrellas en 30 minutos es de:")

"""Grafico de datos"""
    
plt.bar(n, p, label="Probabilidad de ver -n- estrellas dadas, en media hora", color='turquoise', linewidth=2)         
plt.title('Distribución de Poisson para obserbar -n- estrellas en media hora', color='cornflowerblue')
plt.xlabel("Cantidad -n- de estrellas observables en media hora", color='cornflowerblue')
plt.ylabel("Probabilidad de observar -n- estrellas en media hora", color='cornflowerblue')
plt.legend()
plt.show()


"""Definimos un ciclo para encontrar el Número observable de estrellas con mas probabilidad """


i=0                                                                                                        
for i in range (λ):                                             
    if p[i]==np.amax(p):
        break
    i+1
    
print('existe una probabilidad de ver', i+1, 'estrellas en media hora con un valor de: ', np.amax(p)*100,'%.')


# In[ ]:




