def Bi(funcion,valorbajo,valoralto,iteraciones):
    def EvaluarFuncion(funcion,x):
        return eval(funcion)
    resultado = ""
    verifica = True
    for i in range (iteraciones):
        
        valormedio = (valorbajo + valoralto)/2

        a = (EvaluarFuncion(funcion,valorbajo))
        b = (EvaluarFuncion(funcion,valormedio))
        c = (EvaluarFuncion(funcion,valoralto))

        if a < 0 and b >= 0 :
            valorbajo = valorbajo
            valoralto =  valormedio
        elif a >= 0 and b < 0:
            valorbajo = valorbajo
            valoralto =  valormedio    
        elif b < 0 and c >= 0 :
            valorbajo = valormedio
            valoralto =  valoralto
        elif b >= 0 and c < 0 :
            valorbajo = valormedio
            valoralto =  valoralto
        else:
            verifica = False
            resultado="Algo anda mal con tus limites"

        
    if verifica:
        resultado = valormedio 
    else:
        resultado
            
    return resultado