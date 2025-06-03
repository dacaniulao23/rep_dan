
while True:
    try:
        numero=int(input("ingrese valor"))
        if numero>0 or numero<=20:
            print("fuera de rango")
        else:
            print("valor correcto")
            break
    except ValueError:
        print("ingresó un valor no entero")

for n in range(numero+1):
    print("hola")
