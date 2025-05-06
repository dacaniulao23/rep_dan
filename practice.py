# #print = escribir
print("es hora de practicar")

# #input = leer
# #int = definir como ENTERO
n1=int(input("ingrese un número"))

r1=0
r2=0
r3=0

# #for __ in range() = para __ hasta __
for step in range(n1):
    n2=int(input("ingrese otro número"))
#     #if = si __ entonces
#     #and = y
    if n2>=0 and n2<4:
        r1=r1+1
        print(r1)
#     #elif = sino
    elif n2>=4 and n2<8:
        r2=r2+1
        print(r2)
#     #or = o
    elif n2==7 or n2<10:
        r3=r3+1
        print(r3)
#     #elif = sino "final"
    else:
        print("error")

if r1>r2 and r1>r3:
    print ("el mayor alcanzó a ser ", r1)
elif r1<r2 and r2>r3:
    print ("el mayor alcanzó a ser ", r2)
else:
    print ("el mayor alcanzó a ser ", r3)

#str = definir como CARACTER
clave=str(input("ingrese clave"))
#___.lower = acertar escritura independiente de las mayúsculas
while clave.lower!="torna":
    print("clave incorrecta, intente de nuevo")
    clave=input()

n3=int(input("ingrese un nuevo número"))
#import = insertar comando
import time
par=0
impar=0
total=0
for pas in range(1,n3+1):
#incluir (1,__+1) para que el conteo NO SEA desde 0
#y que incluya el número límite
    print(pas)
    #time.sleep(_) = esperar __ segundos/minutos
    time.sleep(1)
    # % = MOD
    if pas%2==0:
        par=par+1
        total=total+pas
    else:
        impar=impar+1
        total=total+pas
print("el total de pares fue ", par)
print("el total de impares fue", impar)
print("la suma total es ", total)

#from random = aleatorio
import random
#randint(_) = aleatorio(_)
azar1=random.randint(1,5)
azar2=random.randint(6,10)
print("resultado aleatorio de ", azar1)
print("resultado aleatorio de ", azar2)

#import random
#___=random.randint()

n4=50
#True = verdadero
valor=True
#"valor" no necesita comparativa ya que de por si es lógico
while n4>=0 and valor:
    total=n4-10
    resp=str(input("seguir?(si)(no)"))
    if resp=="no":
#False = falso
        valor=False
print("hay un total de", total)
#from random import randint
#____=randint
from random import randint
#float = definir como REAL
deci=float(randint(0,20))

