productos=[]
precios=[]
while True:
    try:
        print("bienvenido a la tienda")
        menu=int(input('''teclear menú
                       1. ingresar productos
                       2. comprar productos
                       3. crear boleta
                       4. salir
                       '''))
        match menu:
            case 1:
                for c in productos:
                    producto=str(input('''ingresar producto
                                       '''))
                    productos.append(producto)
                    dec=int(input('''desea continuar?
                                  1. Si
                                  2. No
                                  '''))
                    match dec:
                        case 1:
                            print("agregar")
                        case 2:
                            print("deteniendose")
                            break
                        case _:
                            print("no es válido")
            case 2:
                for d in range(len(productos)):
                    precio=int(input('''ingresar producto
                                     '''))
                    precios.append(precios)