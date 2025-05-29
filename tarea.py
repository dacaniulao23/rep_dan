nota=0
puntaje=0
import time
while puntaje==0:
    carrera=int(input("ingrese su carrera" \
                "1.- Técnico"\
                "2.- Ingeniería" \
                "3.- Diplomado"))
    if carrera==1:
        puntaje+=60
    elif carrera==2:
        puntaje+=40
    elif carrera==3:
        puntaje+=20
    else:
        print("ese número no es una opción")
time.sleep(2)
ramos=int(input("ingrese la cantidad de ramos "))
for step in range(ramos):
    while step!=ramos:
        prom=float(input("ingrese sus promedios "))
        if prom>=1 and prom<=7:
            nota+=prom
            break
        else:
            print("promedio imposible")
promtot=nota/ramos
print("Usted tiene promedio total de ", promtot)
time.sleep(2)
if promtot>=4.5 and promtot<=5:
    print("usted obtiene puntaje de 300")
    puntaje+=300
elif promtot>5 and promtot<=6:
    print("usted obtiene puntaje de 500")
    puntaje+=500
elif promtot>6 and promtot<=7:
    print("usted obtiene puntaje de 800")
    puntaje+=800
time.sleep(2)
print("su puntaje total es de ", puntaje)