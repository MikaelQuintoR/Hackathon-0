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
op=input(str("Ingrese la operación: "))
print(multiplicacion(op))
