def Imatriz(matriz,f):
    print()
    for i in range(f):
        print(matriz[i])

def llenar(matriz,f,c):
    print()
    for i in range(f):
        for j in range(c):
            matriz[i][j]= float(input("Ingrese el valor del coeficiente: "))

def gaussdonw(matriz,f,c):
    for i in range(f):
        for j in range(f):
            if j>i:
                for k in reversed(range(c)):
                    if matriz[i][i] !=0:
                        matriz[j][k]=matriz[j][k]-(matriz[i][k]*matriz[j][i]/matriz[i][i])

def gaussup(matriz,f,c):
    for i in range(f):
        for j in range(f):
            if j<i:
                for k in range(c):
                    print(matriz[k])
                    if matriz[j][j] != 0:
                        matriz[j][k]=matriz[j][k]-(matriz[i][k]*matriz[j][i]/matriz[i][i])
                        

filas = int(input("Ingresa el numero de filas: "))
columnas= int(input("Ingrese el mumero de columnas: "))

matriz = [0]*filas
for c in range(filas):
    matriz[c] = [0]*columnas

llenar(matriz,filas,columnas)
gaussdonw(matriz,filas,columnas)
#gaussup(matriz,filas,columnas)
Imatriz(matriz,filas)

