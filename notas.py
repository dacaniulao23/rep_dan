def promedio():
    notas=0
    cantidad=0
    print("Ingrese la cantidad de notas del alumno ", alumno)
    cantnot=int(input())
                      
    for i in range (cantnot):
        try:
            while True:
                calif=float(input("""Ingrese la nota del alumno:
                                    """))
                if calif>=1 and calif<=7:
                    break
        except Exception:
            print("deben ser notas")
        notas+=calif
        cantidad+=1
    promed=notas/cantidad
    print("El promedio del alumno", alumno, " es ", promed)
    if promed>=4:
        print("el alumno aprovó")
    else:
        ("el alumno reprovó")

alumno=0        
cant=int(input("ingrese la cantidad de alumnos: "))
for alumno in range (cant):
    alumno+=1
    promedio()
