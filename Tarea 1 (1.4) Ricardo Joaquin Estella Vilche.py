#!/usr/bin/env python
# coding: utf-8

# In[28]:


#En la tarea se pide valores especificos siendo x=1 e y=2, pero se dio lugar a indagar con cualquier otros#
x = float(input("Si el valor de x es -->"))
y = float(input("Si el valor de y es -->"))
#Definimos un z para facilitar mas adelante la condicion de las operaciones
z = x + y
#Revisamos que el denominador no de 0 en caso de asignar tales valores
if z == 0:
    print("Syntax error: El resultado de la operacion con x=",x, "e y=",y, "da como resultado 0 en el demoninador, haciendo imposible la division")

if z != 0:
    #si se cumple esto, ahi recien calculamos lo pedido
    resultado = (2*x)/(3*(z))
    print("El Resultado es:", resultado, )

   

