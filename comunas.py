aransel=200000.0
descuento=0.0
import time

comuna=str(input("ingrese su comuna"))
familia=int(input("ingrese su grupo familiar[número]"))

if comuna=="la florida" or comuna=="La Florida":
    print("tiene un descuento del 20%")
    descuento+20
    time.sleep(2)
elif comuna=="puente alto" or comuna=="Puente Alto":
    print("tiene un descuento de 25%")
    descuento+25
    time.sleep(2)
elif comuna=="san joaquín" or comuna=="San Joaquín":
    print("tiene un descuento de 15%")
    descuento+15
    time.sleep(2)