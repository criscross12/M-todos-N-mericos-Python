def integer(fun,xfinal,xinicial):
    def EvaluarFuncion(funcion,x):
        return eval(funcion)
    def verificar(f):
        print(f)
    n = (10000)
    ##f = input("ingresa la funcion para integrar: ")
    #xi = decimal.Decimal(input("Ingrese el valor del intervalo inferior a integrar: "))
    #xf = decimal.Decimal(input("Ingrese el valor del intervalo superior a integrar: "))
    b = float((xfinal-xinicial)/n)
    integralsimple = float(0)
    for i in range(n):
        integralsimple = integralsimple + (b*EvaluarFuncion(fun,i*b))
    print(integralsimple)
    return integralsimple