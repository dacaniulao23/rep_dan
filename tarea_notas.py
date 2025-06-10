notas=[]
promedios=[]

while True:
    try:
        menu=int(input('''seleccione un menú
                       1. ingresar nota
                       2. borrar nota
                       3. mostrar nota
                       4. sacar promedio, nota mayor y nota menor
                       5. limpiar todas las notas
                       6. salir
                       '''))
        match menu:
            case 1:
                nota=float(input('''ingrese nota
                                 '''))
                