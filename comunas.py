aransel=200000.0
descuento=0.0
import time

comuna=str(input("ingrese su comuna"))
familia=int(input("ingrese su grupo familiar[número]"))

if comuna.lower()=="la florida":
    print("tiene un descuento del 20%")
    descuento=20.0
    time.sleep(2)
elif comuna=="puente alto" or comuna=="Puente Alto":
    print("tiene un descuento de 25%")
    descuento=25
    time.sleep(2)
elif comuna=="san joaquín" or comuna=="San Joaquín":
    print("tiene un descuento de 15%")
    descuento=15
    time.sleep(2)
   
if familia==1:
        print("se suma un descuento de 2%")
        descuento+=2.0
elif familia>=2 and familia<=4:
        print("se suma un descuento de 3%")
        descuento+=3.0
elif familia>=5:
        print("se suma un descuento de 5%")
        descuento+=5

time.sleep(2)
descuento=aransel*descuento/100
total=aransel-descuento
print("el precio total es de ", total)