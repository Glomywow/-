# Импортим всякую дичь
import random
import sys
trig = "*КЛИК КЛАК*"
compbang = "*БАХ!* Компьютер упал, дергая левой ногой он проклянул тебя!!"
compsafe = "Компьютер с покерфейсом передал тебе револьвер, он знал что так и будет"
userbang = "*БАХ!* Вы погибли, компьютер забрал куш. Конец игры"
usersafe = "Кажется тебе повезло лох, пистолет не выстрелил и это хорошо!"
 
 
# Если введеное значение юзера лож, то идем в следующий раунд
def falsefun():
    while userinput > intodds:
        failint = float(input("Введите число "  + strodds + " или меньше"))
        if failint <= intodds:
            break
    input(trig)
    if failint == ranint:
            print(userbang)
            sys.exit()
    else:
            input(usersafe)
 
# Если введеное число юзера истина, то идем в следующий раунд
def truefun():
    input(trig)
    if userinput == ranint:
        print(userbang)
        sys.exit()
    else:
        input(usersafe)
 
 
 
# INTRO
 
print("Привет! Добро пожаловать в Русскую рулетку! Правила здесь как в жизни. \n   Игроку необходимо каждый раунд вбивать число, которое будет уменьшаться каждый раз"
      " Если игрок угадает число, то это будет последняя угаданная вещь в его жизни. \n                              В этой игре нет победы, есть только боль ")
 
# Раунд 1
 
ranint = (random.randint(1 ,6))
strodds = str(6)
intodds = float(6)
 
 
userinput = float(input("Начем игру? Напиши число от 1 до 6"))
 
if userinput > 6:
    falsefun()
else:
    truefun()
 
 
# Раунд 2 (компьютер)
ranint = (random.randint(1 ,5))
input("Компьютер выбирает число между 1 и 5")
 
input(trig)
if ranint == 2:
    input(compbang)
    sys.exit()
else:
    input(compsafe)
 
# Раунд 3
ranint = (random.randint(1 ,4))
userinput = float (input("О ты еще здесь, нервничаешь? Напоминаю числа: 1 до 4"))
strodds = str(4)
intodds = float(4)
 
if userinput > 4:
    falsefun()
else:
    truefun()
 
# Раунд 4 (компьютер)
ranint = (random.randint(1 ,3))
input("Компьютер выбирает числа от 1 до 3")
 
input(trig)
if ranint == 3:
    input(compbang)
    sys.exit()
else:
    input(compsafe)
 
# Раунд 5
ranint = (random.randint(1 ,2))
userinput = float (input("Бинго! Ты почти победил, выбирай скорее числа! 1 или 2?"))
strodds = str(2)
intodds = float(2)
 
if userinput > 2:
    falsefun()
else:
    truefun()
# Раунд 6
input("Компьютер целиться в тебя и говорит")
input("Одурманенный, ты, блядь, еблан последний")
input("Ведь ты был глух к несомой мною хуете")
input("И вот он тот твой самый краткий жребий")
input("Ты прерываешь его и хватаешь за его большую пушку! Борись за жизнь, лох!")
 
input(trig)
 
ranint = (random.randint(1 ,3))
if ranint == 3:
    input("*БАХ!* От табуретки ножка в ссаном животе. Компьютер победил и забрал у тебя все!!!")
    sys.exit()
else:
    input("*БАХ!* ПОБЕДА, ПОБЕДА, ПОСЛЕ ОБЕДА!! Ты настолько сильный, что кинул компьютер на прогиб, а-ка хабиб, заломал руку и последним патроном вышиб ему все железные мозги, а ты молодец!.")
