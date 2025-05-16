#ejercicio
precio=0
cant=0
def nombre():
    try:
        name=str(input("Escriba su nombre: "))
    except Exception:
        print("Por favor, escriba su nombre: ")

def productos():
    for cant in range():
        prod=int(input("""Ingrese su producto:
                        1-Agua($150)
                        2-Bebida($180)
                        3-Energética($200)
                        4-Jugo($170)
                        5-Salir($000)
                        """))
        match prod:
            case 1:
                precio+=150
                print("cuesta ", precio, " en total")
            case 2:
                precio+=180
                print("cuesta ", precio, " en total")
            case 3:
                precio+=200
                print("cuesta ", precio, " en total")
            case 4:
                precio+=170
                print("cuesta ", precio, " en total")
            case 5:
                print("salir del sistema")
            case _:
                print("ingrese un número del menú")
        cant+=1

def precios():
    print("usted a acumulado un precio de: $", precio)
    iva=precio/100


try:
    menu=int(input("""Seleccione un menú:
                   1- Nombre
                   2- Productos que comprar
                   3- Precio total
                   4- Salir
                   """))
    while True:
        match menu:
            case 1:
                nombre()
            case 2:
                productos()
except Exception:
    print("Ingrese un número del menú: ")