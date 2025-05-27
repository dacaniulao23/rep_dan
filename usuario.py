nousuario=True
usuario1=None
usuario2=None
usuario3=None

contraseña1=None
contraseña2=None
contraseña3=None


while True:
    try:
        menu=int(input('''
                       1. Iniciar sesión
                       2. Registrar usuario
                       3. Salir
                       
                       '''))
        match menu:
            case 1:
                if nousuario:
                    print("Debe registrarse un usuairo")
                else:
                    usuario=str(input('''Escriba el usuario
                                        '''))
                    contraseña=str(input('''Ingrese contraseña
                                         '''))
                    if (usuario==usuario1 and contraseña==contraseña1) or (usuario==usuario2 and contraseña==contraseña2) or (usuario==usuario3 and contraseña==contraseña3):
                        while True:
                            try:
                                pantalla=int(input('''
                                                    1. Realizar llamada
                                                    2. Enviar correo
                                                    3. Cerrar sesión'''))
                            except Exception:
                                print("debe ser un número")
                    else:
                        print("Usuario o Contraseña incorrectos")
            case 2:
                    usuario=str(input('''Registrar usuario
                                       
                                      '''))
                    contraseña=str(input('''Escribir contraseña
                                          
                                         '''))
                    nousuario=False
                    
            case 3:
                    print("Saliendo del sistema")
                    break
            case _:
                    print("Ingrese un número del menú")

    except Exception:
        print ("ingrese el número")

    