def suma():
    n1=int(input("ingrese un número:  "))
    n2=int(input("ingrese otro número:  "))

    print("el resultado de la suma es ", n1+n2)
def resta():
    n1=int(input("ingrese un número:  "))
    n2=int(input("ingrese otro número:  "))

    print("el resultado de la resta es ", n1-n2)
def multiplicacion():
    n1=int(input("ingrese un número:  "))
    n2=int(input("ingrese otro número:  "))

    print("el resultado de la multiplicacion es ", n1*n2)
def division():
    try: 
        n1=int(input("ingrese un número:  "))
        n2=int(input("ingrese otro número:  "))

        print("el resultado de la division es ", n1/n2)
    except: ZeroDivisionError
    print("error de division")

while True:
    op=int(input("""seleccione sus opciones
                 1-suma
                 2-resta
                 3-multiplicacion
                 4-división
                 """))

    match op:
        case 1:
            print("suma")
            suma()
        case 2:
            print("resta")
            resta()
        case 3:
            print("multiplicacion")
            multiplicacion()
        case 4:
            print("division")
            division()
        case _:
            print("opcion no válida")

#nuevo menu repursivo
# tener tres programas hechos y ejecutarlos
# tener la opcion de salir y ejecutarlos correctamente


while True:
    try:
        num=int(input("ingrese un número mayor a 3 "))
        if num>3:
            break
    except Exception:
        print("solo debe ingresar números ")