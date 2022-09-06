#!/usr/bin/env python
# coding: utf-8

# In[25]:


#Tarea 2.1: Escriba un código que tome un arreglo lleno de ceros producido con np.zeros((3,2)) 
A = np.zeros([3,2])
#y usando ciclos for lo llena para obtener una matriz del 1 al 6 intercaladamente con el mismo numero de filas y columnas

#Solucion bajo las herramientas que logre entender mediante clases y estudio propio:
#lo mas factible fue definir la matriz como un arreglo mediante el comando ravel:
B = np.ravel(A) # De esta manera puedo sumar consecuentementede forma mas facil hasta el 6
for i in range(6):
    a = i+1
    B[i]=a
C = B.reshape([3,2]) #Defino C como el cambio nuevamente a matriz del arreglo modificado
print(C)



# Calificación: 7.0