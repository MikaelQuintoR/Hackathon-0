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
op=input(str("Ingrese la operacion"))
print(Suma(op))

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
op=input(str("Ingrese la operacion"))
print(Resta(op))

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
op=input(str("Ingrese la operacion"))


if:
    "c" in op:
    op = input(str("Ingrese la operacion"))
elif "+" in op:
    print(suma(op))
elif "-" in op:
    print(resta(op))
elif "/" in op:
    print(division(op))
elif "*" in op:
    print(multiplicacion(op))
