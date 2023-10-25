import os
from classes import *
import time
from variables import *
import sys

Eweapon = 0
EShield = 0
Earmor = 0


def displayerstat(money):
    print('---------------------------------------')
    print(f'HP: {player.hp}, Védésém: {player.shield}, Fegyver: {player.weapon} Erő: {player.strength}\nSebesseg {player.speed}, éberség: {player.eberseg}, ügyesseg: {player.agility}')
    print('pénz:', money)
    print('---------------------------------------')

def heal(amount):
    if amount + player.hp > 100:
        player.hp = 100
    else:
        player.hp += amount

def takeDamage(value):
    player.hp -= value
    if player.hp < 1:
        print('az életerőd lement 0 alá')
        print('elkezdtél szédülni')
        print('elálmosodtál')
        print('elaludtál')
        print('Nem keltél fel megint')
        print('Vége')
        sys.exit()

def getItem(type, item):
    global Eweapon, EShield, Earmor, money

    match type:
        case 'weapon':
            if item in Cweapon:
                money += item.price
            else:
                itemindex = WEAPON.index(item)

                Cweapon.append(item)
                if Eweapon == '':
                    pass
                else:
                    item = ''
                    i = 1
                    for weapon in Cweapon:
                        print(i,'...', weapon.name)
                        i += 1
                    itemindex = 9999
                    while not itemindex < len(Cweapon):
                        itemindex = int(input('Melyiket szeretnéd használni? (a fegyver sebzése): '))-1
                Eweapon = Cweapon[itemindex].damage
                player.weapon = Eweapon

        case 'armor':
            if item in Carmor:
                money += item.price
            else:
                itemindex = ARMOR.index(item)

                Carmor.append(item)
                if Earmor == '':
                    pass
                else:
                    item = ''
                    i = 1
                    for armor in Carmor:
                        print(i,'...', armor.name)
                        i += 1
                    itemindex = 9999
                    while not itemindex < len(Carmor):
                        itemindex = int(input('Melyiket szeretnéd használni? (A pajzs védelme): '))-1
                EShield = Carmor[itemindex].shield
                player.shield = Earmor + EShield
        case 'shield':
            if item in Cshield:
                money += item.price
            else:
                itemindex = SHIELD.index(item)
            Cshield.append(item)
            if EShield == '':
                pass
            else:
                item = ''
                i = 1
                for shield in Cshield:
                    print(i,'...', shield.name)
                    i += 1
                itemindex = 9999
                while not itemindex < len(Cshield):
                    itemindex = int(input('Melyiket szeretnéd használni? (A pajzs védelme): '))-1
            EShield = Cshield[itemindex].shield
            player.shield = EShield + EShield

def torles():
    os.system('cls')

def Slowtype(text):
    for i in text:
        print(i, end='')
        time.sleep(0.05)
    print()

def ido(eltMinute = 0, eltHour = 0, eltDay = 0):
    global hour, minute, day
    minute += eltMinute
    hour += eltHour
    day += eltDay
    while minute >= 60:
        minute -=  60
        hour += 1

    if not hour < 22:
        if nowplace == 'city':
            print('elmentél a szállásra aludni.')
            player.eberseg = 100
        else:
            print('A vadonban aludtál')
            player.eberseg ==  75
        hour = 6
        minute = 0

def repdec(amount):
    player.rep -= amount
    if player.rep < 50:
        print('Annyira utálnak az emberek, hogy elküldtek egy különös helyre zuhanyozni.')
        print('Víz helyett valami furcsa gáz jött a csapból.')
        print('elálmosodtál')
        print('elaludtál')
        print('soha többé nem keltél fel.')
        print('Vége')
        for i in range(1):
            print('r garbjefjoafjabfja')
        sys.exit()

def fight(enemy):
    global money, goblin, ogre, bandit, cerberus, vampir
    while enemy.hp >=  0:
        print(f'ellenfeled hp: {enemy.hp}, sebessége: {enemy.speed}, ereje: {enemy.strength}, védelme: {enemy.shield}')
        if player.speed <= enemy.speed :
            print('Ő a gyorsabb ő támad először')
            enemydamage = enemy.strength - player.shield
            print(f'az ellenfeled-et {enemydamage}-et  sebzett.')
            if str(enemy) == 'vampir':
                enemy.hp += enemydamage
            playerdamage = player.strength * player.weapon - enemy.shield + randint(-2, 2)
            if playerdamage < 0:
                playerdamage = 0
            print(f'te {playerdamage} -et sebeztél')
            takeDamage(enemydamage)
            enemy.hp -= playerdamage
            input('ENTER')
        else:
            print('te vagy a gyorsabb te támadsz először')
            enemydamage = enemy.strength - player.shield
            playerdamage = player.strength * player.weapon - enemy.shield + randint(-2, 2)

            print(f'te {playerdamage} -et sebeztél')
            enemy.hp -= playerdamage
            if enemy.hp <= 0:
                break
            print(f'a {enemydamage}-et sebzett.')
            takeDamage(enemydamage)
            input('ENTER')
    ido(5)
    match enemy.name:
        case 'goblin':
            foundmoney = randint(5, 15)
            print(f'találtál a legyőzőtt goblinnál {foundmoney} pénzt')
            goblin.hp = 5

        case 'ogre':
            foundmoney = randint(10, 20)
            print(f'találtál a legyőzőtt ogrénél {foundmoney} pénzt')
            ogre.hp = 10

        case 'bandit':
            foundmoney = randint(15, 30)
            print(f'találtál a legyőzőtt banditánál {foundmoney} pénzt')
            bandit.hp = 7

        case 'cerberus':
            foundmoney = 0
            print('nincs pénz nincs cerberusoknál')
            cerberus.hp = 15

        case 'vampir':
            foundmoney = randint(20, 30)
            print(f'találtál a legyőzőtt vámpírnál {foundmoney} pénzt')
            vampir.hp = 20

    money += foundmoney

def goto(place):
    global nowplace
    if not str(place) in PLACE:
        print('place not in PLACE')
        return 0
    match place:
        case 'forest':
            distance = 50
        case 'field':
            distance = 30
        case 'mine':
            distance = 75
        case 'kazamata':
            distance = 85
        case 'mountain':
            distance = 65
        case 'city':
             match nowplace:
                case 'forest':
                    distance = 50
                case 'field':
                    distance = 30
                case 'mine':
                    distance = 75
                case 'kazamata':
                    distance = 85
                case 'mountain':
                    distance = 65
    while distance >= 0:
        if lo:
            distance -= 15
            print('lovagolsz')
        else:
            distance -= 5
            print('gyalogolsz')
            time.sleep(1)
        if randint(1, 3) ==  1:
            rand = randint(1, 10)            
            if rand in range(1, 5):
                print('egy goblin állja az utad')
                fight(goblin)

            if rand in range(5, 8):
                print('egy ogre állja az utad')
                fight(ogre)
            if rand in range(8, 10):
                print('egy bandita állj az utad')
                fight(bandit)
            if rand == 10:
                print('egy vámpír állj az utad')
                fight(vampir)
        ido(30)
    nowplace = place
    print('elérted célod')
    input('ENTER')
    torles()




if __name__ == '__main__':
    getItem(type='weapon',item =  obszidianel)
    player.strength = 3
    goto('forest')