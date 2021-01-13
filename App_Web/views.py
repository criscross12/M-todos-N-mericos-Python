from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .Biseccion import Bi
from .Derivadas import der,derm,seno,coseno
from .integracion import integer
fl = True
flq = True
flq1 = True
def derivada(request):
    global flq
    fun = ""
    x = ""
    res = ""
    res1 = ""
    sen = ""
    cosenop= ""
    try:       
        answer0 = request.GET['Func']
        if answer0 is not None and answer0!= '':
            fun=answer0
            flq = False
        answer1 = request.GET['Lw']
        if answer1 is not None and answer1!= '':
            x=float(answer1)

        res = der(fun, x) 
        res1 = derm(fun,x) 
        sen = seno(fun,x) 
        cosenop = coseno(fun,x)
        print(res)  
        print(res1)
        print(sen)
    except:
        flq = True
        pass
    Titulos={'titulo0':"Derivacion",'titulo1':"Inserta Funcion"}
    Instrucciones={'instruccion1':"Ingresa funcion",'instruccion2':"Ingresa el valor en evaluarlo"}
    MostrarValores1 = {'ShowVales':flq}
    Funcion = {'f':fun,'x':x, 'r':res, 're':res1, 'se':sen, 'co':cosenop }

    
    if MostrarValores1['ShowVales']:
        Datos = {'titles': Titulos,'ins':Instrucciones,'mostrar':MostrarValores1}
        return render(request,"derivada.html",Datos)   
    else:
        Datos = {'titles': Titulos,'ins':Instrucciones,'mostrar':MostrarValores1, 'fun': Funcion}
        return render(request,"derivada.html",Datos )

###########################################################33
def Home(request):
    global fl
    f = ""
    l = ""
    u = ""
    n = ""
    r = ""
    try:       
        answer0 = request.GET['Fun']
        if answer0 is not None and answer0!= '':
            f=answer0
            print(f)
            fl = False
 
        answer1 = request.GET['Low']
        if answer1 is not None and answer1!= '':
            l=float(answer1)

        answer2 = request.GET['Up']
        if answer2 is not None and answer2!= '':
            u=float(answer2)

        answer3 = request.GET['Num']
        if answer3 is not None and answer3!= '':
            n=int(answer3)
        
        r = Bi(f,l,u,n)

    except:
        fl = True
        pass

    Titulos={'titulo0':"Metodo de Biseccion",'titulo1':"Inserta Funcion pero sin el igual"}
    Instrucciones={'instruccion1':"Ingresa funcion",'instruccion2':"Ingresa el limite inferior",'instruccion3':"Ingresa el limite superior",'instruccion4':"Ingresa el numero de iteraciones"}
    MostrarValores = {'ShowVales':fl}
    Funcion = {'Func':f,'Lw':l,'U':u,'Nu':n,'Re':r}

    
    if MostrarValores['ShowVales']:
        Datos = {'titles': Titulos,'ins':Instrucciones,'mostrar':MostrarValores}
        return render(request,"Home.html",Datos)   
    else:
        Datos = {'titles': Titulos,'ins':Instrucciones,'mostrar':MostrarValores, 'fun': Funcion}
        return render(request,"Home.html",Datos )
#########################################################
def home(request):
    Titulos={'titulo0':"wel",'titulo1':"bienvenido a la pagina web de metodos numericos de 5to Semestre"}
    Instrucciones={'instruccion1':"Ingresa funcion",'instruccion2':"Ingresa el limite inferior",'instruccion3':"Ingresa el limite superior",'instruccion4':"Ingresa el numero de iteraciones"}
    MostrarValores = {'ShowVales':fl}

    if MostrarValores['ShowVales']:
        Datos = {'titles': Titulos,'ins':Instrucciones,'mostrar':MostrarValores}
        return render(request,"wel.html",Datos)   
    else:
        Datos = {'titles': Titulos,'ins':Instrucciones,'mostrar':MostrarValores}
        return render(request,"wel.html",Datos )

#########################################
def interger(request):
    global flq1
    f = ""
    xf = ""
    xi = ""
    resul = ""
    try:       
        answer0 = request.GET['Fun']
        if answer0 is not None and answer0!= '':
            f=answer0
            print(f)
            flq1 = False
 
        answer1 = request.GET['Low']
        if answer1 is not None and answer1!= '':
            xf=float(answer1)
            print(xf)
        answer2 = request.GET['Up']
        if answer2 is not None and answer2!= '':
            xi=float(answer2)
            print(xi)
        resul = integer(f,xf,xi)
        print(resul)
    except:
        flq1 = True
        pass

    Titulos={'titulo0':"Metodo de Integracion",'titulo1':"Inserta Funcion pero sin el igual"}
    Instrucciones={'instruccion1':"Ingresa funcion",'instruccion2':"Ingrese el valor del intervalo inferior a integrar: ",'instruccion3':"Ingrese el valor del intervalo superior a integrar: ",'instruccion4':"Ingresa el numero de iteraciones"}
    MostrarValores = {'ShowVales':flq1}
    Funcion = {'Fu':f,'Ar':xf,'Ba':xi,'Re':resul}

    
    if MostrarValores['ShowVales']:
        Datos = {'titles': Titulos,'ins':Instrucciones,'mostrar':MostrarValores}
        return render(request,"integracion.html",Datos)   
    else:
        Datos = {'titles': Titulos,'ins':Instrucciones,'mostrar':MostrarValores, 'fun': Funcion}
        return render(request,"integracion.html",Datos )

def Euler(request):
    global flq1
    f = ""
    xf = ""
    xi = ""
    resul = ""
    try:       
        answer0 = request.GET['Fun']
        if answer0 is not None and answer0!= '':
            f=answer0
            print(f)
            flq1 = False
 
        answer1 = request.GET['Low']
        if answer1 is not None and answer1!= '':
            xf=float(answer1)
            print(xf)
        answer2 = request.GET['Up']
        if answer2 is not None and answer2!= '':
            xi=float(answer2)
            print(xi)
        resul = integer(f,xf,xi)
        print(resul)
    except:
        flq1 = True
        pass

    Titulos={'titulo0':"Euler",'titulo1':"Inserta Funcion pero sin el igual"}
    Instrucciones={'instruccion1':"Ingresa funcion",'instruccion2':"Ingrese el valor del intervalo inferior a integrar: ",'instruccion3':"Ingrese el valor del intervalo superior a integrar: ",'instruccion4':"Ingresa el numero de iteraciones"}
    MostrarValores = {'ShowVales':flq1}
    Funcion = {'Fu':f,'Ar':xf,'Ba':xi,'Re':resul}

    
    if MostrarValores['ShowVales']:
        Datos = {'titles': Titulos,'ins':Instrucciones,'mostrar':MostrarValores}
        return render(request,"Euler.html",Datos)   
    else:
        Datos = {'titles': Titulos,'ins':Instrucciones,'mostrar':MostrarValores, 'fun': Funcion}
        return render(request,"Euler.html",Datos )