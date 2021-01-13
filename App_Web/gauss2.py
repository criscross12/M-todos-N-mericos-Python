# Método de Gauss
# Solución a Sistemas de Ecuaciones
# de la forma A.X=B
import numpy as np
# INGRESO
A = np.array([[4,2,5],
              [2,5,8],
              [5,4,3]])

B = np.array([[60.70],
              [92.90],
              [56.30]])
# PROCEDIMIENTO
casicero = 1e-15 # Considerar como 0
# Evitar truncamiento en operaciones
A = np.array(A,dtype=float) 
# Matriz aumentada
AB = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)
# Pivoteo parcial por filas
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]
# Para cada fila en AB
for i in range(0,n-1,1):
    # columna desde diagonal i en adelante
    columna = abs(AB[i:,i])
    dondemax = np.argmax(columna)
    # dondemax no está en diagonal
    if (dondemax !=0):
        # intercambia filas
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[dondemax+i,:]
        AB[dondemax+i,:] = temporal
AB1 = np.copy(AB)

for i in range(0,n-1,1):
    pivote = AB[i,i]
    adelante = i+i
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
AB2 = np.copy(AB)


ultfila = n-1
ultcolumna = m-1

i = ultfila
for i in range(ultfila,0-1,-1):
    pivote = AB[i,i]
    atras = i-1
    for k in range(atras,0-1,-1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor     
    AB[i,:] = AB[i,:]/pivote


# SALIDA
print('Matriz aumentada:')
print(AB0)
print('Pivoteo parcial por filas')
print(AB1)
print('eliminación hacia adelante')
print(AB2)
print('eliminacion hacia atras: ')
print(AB)