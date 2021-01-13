import decimal
def EvaluarFuncion(funcion,x):
    return eval(funcion)

    h = decimal.Decimal(0.000001)
    f= input('INgresa una funcion para derivar:  ')
    x = decimal.Decimal(input('Ingresa un valor para evaluar la funcion: '))
    derivada = ((EvaluarFuncion(f,(x+h))) - (EvaluarFuncion(f,(x))))/h
    print(derivada)