cred=0

suma=0

ing=int(input("ingrese su cantidad de ingresos"))
if ing>=500000 and ing<1000000:
    cred+=300000
elif ing>=1000000 and ing<1500000:
    cred+=650000
elif ing>=1500000:
    cred+=1000000

nivE=str(input("ingrese su nivel educacional"))

if nivE.lower=="básico" or nivE.lower=="basica":
    bono=suma*1
    suma+=bono
elif nivE.lower=="medio" or nivE.lower=="media":
    bono=suma*1.3
    suma+=bono
elif nivE.lower=="superior":
    bono=suma*1.5
    suma+=bono
cred+=suma