import decimal
from sympy import sin,cos,diff
def der(f,x):
    def EvaluarFuncion(funcion,x):
        return eval(funcion)
    def verificar(f):
        print(f)
    h = float(0.000001)
    verificar(f)
    derivada = ((EvaluarFuncion(f,(x+h))) - (EvaluarFuncion(f,(x))))/h
    return derivada
def derm(f,x):
    def EvaluarFuncion(funcion,x):
        return eval(funcion)
    def verificar(f):
        print(f)
    h = float(0.000001)
    verificar(f)
    derivada1 = ( (-25*EvaluarFuncion(f,x)) +(48*EvaluarFuncion(f,(x+h))) - (36*EvaluarFuncion(f,(x+(2*h)))) + (16*EvaluarFuncion(f,(x+(3*h))))- (3*EvaluarFuncion(f,(x+(4*h)))) ) / (12*h)
    return derivada1

def seno(f,x):
    def EvaluarFuncion(funcion,x):
        return eval(funcion)
    def verificar(f):
        print(f)
    h = float(0.000001)
    verificar(f)
    fn = diff(sin(x))
    print(fn)
    seno1 = ( (-25*EvaluarFuncion(f,fn)) + (48*EvaluarFuncion(f,(fn+h))) - (36*EvaluarFuncion(f,(fn+(2*h)))) + (16*EvaluarFuncion(f,(fn+(3*h))))- (3*EvaluarFuncion(f,(fn+(4*h)))) ) / (12*h)
    return seno1

def coseno(f,x):
    def EvaluarFuncion(funcion,x):
        return eval(funcion)
    def verificar(f):
        print(f)
    h = float(0.000001)
    verificar(f)
    fn = diff(cos(x))
    print(fn)
    seno11 = ( (-25*EvaluarFuncion(f,fn)) + (48*EvaluarFuncion(f,(fn+h))) - (36*EvaluarFuncion(f,(fn+(2*h)))) + (16*EvaluarFuncion(f,(fn+(3*h))))- (3*EvaluarFuncion(f,(fn+(4*h)))) ) / (12*h)
    return seno11