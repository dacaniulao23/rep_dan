
#     -5-4-3 -2 -1
# numeros=[7,5,33,24,9]
#      0 1 2  3  4

# print(numeros[-1])

# for numero in numeros:
#     print(numero)

# print(numeros)

# numeros.append(64)
# print(numeros)

# numeros.insert(3,100)
# print(numeros)

#for i in range(len(numeros))

# frutas=["manzana", "mango", "membrillo"]
# for fruta in frutas:
#     print(fruta)

nombres=[]
apellidos=[]
while True:
    print('''
          1. insertar nombre y apellidos
          2. mostrar nombres y apellidos
          3. buscar nombres y apellidos
          4. salir
          ''')
    op=int(input("seleccione una opcion: "))
    match op:
        case 1:
            nom=input('''ingrese un nombre:
                      ''')
            nombres.append(nom)
            apell=input('''ingrese un apellido:
                        ''')
            apellidos.append(apell)
        case 2:
            for c in range(len(nombres)):
                print(nombres, " ",apellidos)
        case 3:
            busca=int(input('''buscar nombre y apellidos
                            '''))
            print(nombres[busca])
            print(apellidos[busca])
        case 4:
            print("saliendo")
            break
        case _:
            print("opcion invalida")