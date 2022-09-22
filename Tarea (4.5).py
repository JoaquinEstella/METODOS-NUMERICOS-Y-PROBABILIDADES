#!/usr/bin/env python
# coding: utf-8

# In[1]:
# %%

import numpy as np                  ## Importamos paquetes externos
import matplotlib.pyplot as plt     
import math


# In[2]:


"""Procedemos a crear un programa que calcule el valor de sen(x) usando
una expansion en serie de taylor"""
#Si bien se pide que el valor del argumento "(x)" en radianes sea de 1
#Damos lugar a que el usuario de el que el quiera y mas encima en grados si le parece

x_deg = float( input("Cual es el valor del argumento (grados):"))

x = math.radians(x_deg)

n = int(input("Numero de terminos a sumar: ")) #Numero de terminos a sumar

err_verd = 100.00 # Error verdadero porcentual

sen_verd = math.sin(x) #Valor verdadero de sen(x)

sen_x = 0.0 #Acumulador en cero
for k in range(n): #Ciclo para sumar terminos
    sen_x = sen_x + (-1)**k * x**(2*k+1) / math.factorial((2*k+1)) #Serie de taylor
    
    err_verd = abs( (sen_verd - sen_x) / sen_verd ) * 100
    print("{:^5d} {:^13d} {:^10.10f} {:^15.4g}" .format(k +1, k, sen_x, err_verd)) #Presentacion de temrinos
    
    print()


# In[21]:


"""Para facilitar el grafico de la serie con sen(1), me es preferible para mis conocimientos (ya que no se como hacerlo 
de otra manera) generar una definicion de esta y luego graficarla como variable"""

# Comentario del profesor: ¿Quién es m? Cuando uno lee el código a la carrera no queda claro.
def sin_taylor(m):      
# Faltó un docstring en esta función. Hay confusión en el uso de docstrings. 

    # No se define la variable approx, el código no funciona
    approx = np.zeros(len(m)) # AGREGADO POR EL PROFESOR

    for i in range(1,len(m)+1):     
        s = 0         
        for k in range(i):
            s += ((((-1)**k)*(x**((2*k)+1)))/(np.math.factorial((2*k)+1)))   ##Serie de taylor seno
            
        approx[i-1] = s           ##guardamos los valores en el arreglo
    
    return approx       ##nos devuelve el arreglo con el resultado contenido en él


# In[24]:


#Defino el programa en variable
n = np.arange(0,5) ## AGREGADO POR EL PROFESOR
# Este código no funciona, tal vez hay que definir n antes de esta línea
f = sin_taylor(n) 

#Defino una serie de vectores
#n = np.arange(0,5)   # COMENTADO POR EL PROFESOR   
#approx = np.zeros(5) # COMENTADO POR EL PROFESOR
x = 1 
v_real = np.sin(1)*np.ones(5) #vector real de sen(1)
error = v_real - f

#figura para contener el gráfico
fig = plt.figure()
fig.add_subplot()
ax = fig.add_subplot(1,1,1)

ax.errorbar(n,f,yerr=error,color='red',linestyle='none',label='Barra de error')  #error
ax.plot(n,f,color='black',label='Aproximación para el $\sin (1)$',linestyle=':')   #función
ax.plot(n,v_real,color='blue',label='Valor real de $\sin (1)$',linestyle='-')
fig.suptitle('Valor aproximado en funcion de n')   
ax.set_xlabel('n')
ax.set_ylabel('App de $\sin (1)$')
plt.legend()

plt.show()


# CALIFICACIÓN: 5.0. El código entregado no funcionaba

# In[ ]:




