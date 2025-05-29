Marianne=50
Edelgard=56
import random, time
print("Edelgard: ", Edelgard*"▄", 
                "Hit: 81% "
                "Dmg: 7 "
                "Crit: 63% ")
print("Marianne: ", Marianne*"▄", 
                "Hit: 93% "
                "Dmg: 5 "
                "Crit: 45% ")

dado=1
while Marianne>=0 and Edelgard>=0:
    if dado%2==0:
        print("Turno de Marianne")
        time.sleep(2)
        hit2=random.randint(9,10)
        crit2=random.randint(4,10)
        if hit2==10 and crit2==10:
            print("Daño crítico!")
            Edelgard-=5*3
            print("Edelgard: ", Edelgard*"▄")
        elif hit2==10 and crit2!=10:
            print("Ha dañado a Edelgard")
            Edelgard-=5
            print("Edelgard: ", Edelgard*"▄")
        elif hit2!=10 and crit2==10:
            print("Daño crítico!")
            Edelgard-=5*3
            print("Edelgard: ", Edelgard*"▄")
        else:
            print("miss")
    else:
        print("Turno de Edelgard")
        time.sleep(2)
        hit1=random.randint(8,10)
        crit1=random.randint(7,10)
        if hit1==10 and crit1==10:
            print("Daño crítico!")
            Marianne-=7*3
            print("Marianne: ", Marianne*"▄")
        elif hit1==10 and crit1!=10:
            print("Ha dañado a Marianne")
            Marianne-=7
            print("Marianne: ", Marianne*"▄")
        elif hit1!=10 and crit1==10:
            print("Daño crítico!")
            Marianne-=7*3
            print("Marianne: ", Marianne*"▄")
        else:
            print("miss")
    dado+=1
    time.sleep(2)

if Marianne<=0:
    print("Gana Edelgard")
else:
    print("Gana Marianne")