fruta=0
cantidad=0
precio=0
while True:
    try:
        m1=int(input('''Teclear un número del menú:
                1. Productos
                2. Pago
                3. Voleta
                4. Salir
                '''))
        match m1:
            case 1:
                while True:
                    try:
                        can=int('''Ingresar cuantas frutas desea comprar
                               ''')
                        for prod in range(can+1):
                            m2=int('''Teclear el producto que va a comprar
                                   1. Manzana $230
                                   2. Naranja $300
                                   3. Frutilla $200
                                   4. Cereza $170
                                   5. Pera $250
                                   ''')
                            match m2:
                                case 1:
                                    print("Suma $230")
                                    precio+=230
                                case 2:
                                    print("Suma $300")
                                    precio+=300
                                case 3:
                                    print("Suma $200")
                                    precio+=200
                                case 4:
                                    print("Suma $170")
                                    precio+=170
                                case 5:
                                    print("Suma $250")
                                    precio+=250
                                case _:
                                    print("No es una fruta")
                            fruta+=1
                            cantidad+=precio
                            print("Lleva total de ", cantidad)
                        if prod==(can+1):
                            break
                    except ValueError:
                        print("No es un número")
            case 2:
                print("El precio total a pagar es de ", cantidad)
                while True:
                    try:
                        m3=int(input('''Teclear método de pago
                                    1. Efectivo
                                    2. Tarjeta
                                    '''))
                        
                        
                    except ValueError:
                

            case 3:
            case 4:
                print("Saliendo del sistema")
                break
            case _:
                print("Numero no tecleado")
    except ValueError:
        print("No tecleado")
