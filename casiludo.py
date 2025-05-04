import random, time

meta=30
turno=1

j1=0
j2=0

while j1<meta and j2<meta:
    print("Turno: ", turno)
    if turno%2==0:
        print("Turno del J2")
        dado=random.randint(1,6)
        time.sleep(3)
        j2=j2+dado
        print("J2 avanza", dado, " casillas,",
              "llega hasta el espacio ", j2)
    else:
        print("Turno del J1")
        dado=random.randint(1,6)
        time.sleep(3)
        j1=j1+dado
        print("J1 avanza", dado, " casillas,",
              "llega hasta el espacio ", j1)
    turno=turno+1

if j1>j2:
    print("ganó J1")
else:
    print("ganó J2")