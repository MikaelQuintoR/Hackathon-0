def Suma( operacion :str):
    global n1
    n=""
    for i in operacion:
        if i!="+":
            n+=i
        else :
            n1=int(n)
            n=""
    n2=int(n)
    return n1+n2


def Resta( operacion :str):
    global n1
    n=""
    for i in operacion:
        if i!="-":
            n+=i
        else :
            n1=int(n)
            n=""
    n2=int(n)
    return n1-n2

def multiplicacion(operacion :str):
    global n1
    n=""
    for i in operacion:
        if i!="":
            n+=i
        else :
            n1=int(n)
            n=""
    n2=int(n)
    return n1n2


def division( operacion :str):
    global n1
    n=""
    for i in operacion:
        if i!="/":
            n+=i
        else :
            n1=int(n)
            n=""
    n2=int(n)
    return n1/n2

op = input(str("Ingrese la operacion"))

if"c" in op:
    op = input(str("Ingrese la operacion"))
elif "+" in op:
    print(Suma(op))
elif "-" in op:
    print(Resta(op))
elif "/" in op:
    print(division(op))
elif "*" in op:
    print(multiplicacion(op))
def Suma( operacion :str):
    global n1
    n=""
    for i in operacion:
        if i!="+":
            n+=i
        else :
            n1=int(n)
            n=""
    n2=int(n)
    return n1+n2


def Resta( operacion :str):
    global n1
    n=""
    for i in operacion:
        if i!="-":
            n+=i
        else :
            n1=int(n)
            n=""
    n2=int(n)
    return n1-n2

def multiplicacion(operacion :str):
    global n1
    n=""
    for i in operacion:
        if i!="":
            n+=i
        else :
            n1=int(n)
            n=""
    n2=int(n)
    return n1n2


def division( operacion :str):
    global n1
    n=""
    for i in operacion:
        if i!="/":
            n+=i
        else :
            n1=int(n)
            n=""
    n2=int(n)
    return n1/n2

op = input(str("Ingrese la operacion"))

if"c" in op:
    op = input(str("Ingrese la operacion"))
elif "+" in op:
    print(Suma(op))
elif "-" in op:
    print(Resta(op))
elif "/" in op:
    print(division(op))
elif "*" in op:
    print(multiplicacion(op))
def Suma( operacion :str):
    global n1
    n=""
    for i in operacion:
        if i!="+":
            n+=i
        else :
            n1=int(n)
            n=""
    n2=int(n)
    return n1+n2


def Resta( operacion :str):
    global n1
    n=""
    for i in operacion:
        if i!="-":
            n+=i
        else :
            n1=int(n)
            n=""
    n2=int(n)
    return n1-n2

def multiplicacion(operacion :str):
    global n1
    n=""
    for i in operacion:
        if i!="*":
            n+=i
        else :
            n1=int(n)
            n=""
    n2=int(n)
    return n1*n2


def division( operacion :str):
    global n1
    n=""
    for i in operacion:
        if i!="/":
            n+=i
        else :
            n1=int(n)
            n=""
    n2=int(n)
    return n1/n2

op = input(str("Ingrese la operacion"))

if"c" in op:
    op = input(str("Ingrese la operacion"))
elif "+" in op:
    print(Suma(op))
elif "-" in op:
    print(Resta(op))
elif "/" in op:
    print(division(op))
elif "*" in op:
    print(multiplicacion(op))
