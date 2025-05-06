import random, time

num1=int(input("ingrese dos dígitos "))
num2=int(input())

while num1>num2:
    print("el segundo dígito debe ser mayor")
    n1=input()
    n2=input()

veces=0
rango=random.randint(num1,num2)
for step in range(rango):
    time.sleep(2)
    print("▄")
    veces+=1

print("el símbolo ▄ se escribió ", veces, " veces")