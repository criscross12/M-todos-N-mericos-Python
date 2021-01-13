#def EvaluarFuncion(funcion,x):
#    return eval(funcion)  
def EvaluarFuncion(funcion,x):
    return eval(funcion)  
funcion = input("Ingresa un funcion: ")
salto = float(input("Ingresa un valor de salto: "))
X = float(input("Ingresa un valor de X: "))
Y = float(input("Ingresa un valor de Y: "))
XF = int(input("Ingresa hasta X: "))
Fun = (EvaluarFuncion(funcion,X))
yi = Y + salto * Fun

Data = "h         xi        yi     f(xi,yi)    yi+1"
#print 
print (Data)
print (str(salto) + "      "+ str(X)+ "       "+ str(Y)+ "       " + str(Fun) + "       " + str(yi))


for i in range (XF):
    
    X = X + salto
    Fun = (EvaluarFuncion(funcion,X))
    #Fun1 = funcion
    Y = yi
    yi = Y + salto * Fun
    print (str(salto) + "      "+ str(X)+ "       "+ str(Y)+ "       " + str(Fun) + "       " + str(yi))


        
if X == XF:
        print ("La solucion alcansada es")
        #print (valormedio)
#print (type(datos))

