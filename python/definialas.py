import os
import time
from variables import *
import sys
from bosses import *
import random
from minigames import *

foszereplo = 'Játékos'

Eweapon = 0
EShield = 0
Earmor = 0

piros = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 ]


def torles():
    os.system('cls')



def menu():
    print('1...Páros, páratlan')
    print('2...kicsi, vagy nagy')
    print('3...Tucatok')
    print('4...3-mal oszthatóság ')
    print('5...szamok')
    print('6...Piros, Fekete')
    print('0...Kilépés')
    tipus = rangeEgeszszambekeres(szoveg = 'Melyiket válassza', min = 0, max = 6)
    return tipus

def sorsolas():
    szam = random.randint(0, 36)
    print(f'a sorsolt szám: {szam}')
    return szam 


def oddEven():
    egyenleg = 0
    print('1...Páros')
    print('2...Páratlan')
    print('0...Vissza')
    tipus = rangeEgeszszambekeres(szoveg = 'Melyiket válassza', min = 0, max = 2)
    torles()

    match tipus:
        case 0:
            pass
        
        case 1:
            Tet = tet()
            nyeroszam = sorsolas()
            if nyeroszam % 2 != 0 or nyeroszam == 0:
                egyenleg -= Tet
                print('vesztettél')
            else:
                egyenleg += Tet
                print('Nyertél')
        case 2: 
            Tet = tet()
            nyeroszam = sorsolas()
            if nyeroszam % 2 == 0:
                egyenleg -= Tet
                print('vesztettél')
            else:
                egyenleg += Tet
                print('Nyertél')
    cont()
    torles()
    return egyenleg
def tet():
    tet = rangeEgeszszambekeres('Mennyi a tét? ')
    print(f' \nA tét:{tet}')
    return tet

def smallBig():
    egyenleg = 0
    print('1...Kicsi(1-18)')
    print('2...Nagy(19-36)')
    print('0...Vissza')

    tipus = rangeEgeszszambekeres(szoveg = 'Melyiket válassza', min = 0, max = 2)
    torles()

    match tipus:
        case 0:
            pass
        
        case 1:
            Tet = tet()
            nyeroszam = sorsolas()
            if nyeroszam < 1 or nyeroszam > 18:
                egyenleg -= Tet
                print('vesztettél')
            else:
                egyenleg += Tet
                print('Nyertél')
        case 2: 
            Tet = tet()
            nyeroszam = sorsolas()
            if nyeroszam < 19 or nyeroszam > 36:
                egyenleg -= Tet
                print('vesztettél')
            else:
                egyenleg += Tet
                print('Nyertél')
    cont()
    torles()
    return egyenleg

def tucat():
    egyenleg = 0
    print('1...1-12')
    print('2...13-24')
    print('3...25-36')
    print('0...Vissza')

    tipus = rangeEgeszszambekeres(szoveg = 'Melyiket válassza', min = 0, max = 3)
    torles()

    match tipus:
        case 0:
            pass
        case 1:
            Tet = tet()
            nyeroszam = sorsolas()
            if nyeroszam < 0 or nyeroszam >12:
                egyenleg -= Tet
                print('vesztettél')
            else:
                egyenleg += Tet * 2
                print('Nyertél')
        case 2:
            Tet = tet()
            nyeroszam = sorsolas()
            if nyeroszam < 12 or nyeroszam >24:

                egyenleg -= Tet
                print('vesztettél')
            else:
                egyenleg += Tet * 2
                print('Nyertél')            
        case 3:
            Tet = tet()
            nyeroszam = sorsolas()
            if nyeroszam < 24 or nyeroszam >36:

                egyenleg -= Tet
                print('vesztettél')
            else:
                egyenleg += Tet * 2
                print('Nyertél')
    cont()
    torles()
    return egyenleg
def oszlop():
    egyenleg = 0
    print('1...1. Oszlop')
    print('2...2. Oszlop')
    print('3...3. Oszlop')
    print('0...Vissza')

    tipus = rangeEgeszszambekeres(szoveg = 'Melyiket válassza', min = 0, max = 3)
    torles()

    match tipus:
        case 0:
            pass
        
        case 1:
            Tet = tet()
            nyeroszam = sorsolas()
            if nyeroszam %3 !=1:
                egyenleg -= Tet
                print('vesztettél')
            else:
                egyenleg += Tet * 2
                print('Nyertél')
        case 2:
            Tet = tet()
            nyeroszam = sorsolas()
            if nyeroszam %3 !=2:
                egyenleg -= Tet
                print('vesztettél')
            else:
                egyenleg += Tet * 2
                print('Nyertél')            
        case 3:
            Tet = tet()
            nyeroszam = sorsolas()
            if nyeroszam % 3 ==0 and nyeroszam != 0:
                egyenleg -= Tet
                print('vesztettél')
            else:
                egyenleg += Tet * 2
                print('Nyertél')
    cont()
    torles()
    return egyenleg
    
def oneNumber():
    egyenleg = 0
    tipus = rangeEgeszszambekeres('Melyik számra szeretne tenni: ', min = 0, max = 36)
    torles()

    Tet = tet()
    nyeroszam = sorsolas()
    if nyeroszam != tipus:
        egyenleg -= Tet
        print('vesztettél')
    else:
        egyenleg += Tet * 35
        print('Nyertél')
    cont()
    torles()
    return egyenleg

def cont():
     input('Press ENTER to continue')

def torles():
    os.system('cls')

def rangeEgeszszambekeres(szoveg = ' ', min = 0, max = 10000):
    szam = ' '
    while True:
        szam = egeszszambekeres(szoveg)
        if szam < min or szam >max:
            pass
        else:
            break
    return int(szam)
def egeszszambekeres(szoveg) -> int:
    szam = ''
    while not szam.isdecimal():
        szam = input(szoveg)
    return int(szam)

def redBlack():
    egyenleg = 0
    print('1...Piros')
    print('2...Fekete')
    tipus = rangeEgeszszambekeres('Melyik szinre szeretne tenni: ', min = 0, max = 2)
    torles()

    Tet = tet()
    nyeroszam = sorsolas()
    match tipus:
        case 0:
            pass
        case 1:
            if nyeroszam in piros:
                egyenleg += Tet 
                print('Nyertél')
            else:
                egyenleg -= Tet
                print('vesztettél')
        case 2:
            if nyeroszam not in piros:
                egyenleg += Tet 
                print('Nyertél')
            else:
                egyenleg -= Tet
                print('vesztettél')
    cont()
    torles()
    return egyenleg
def casino():
    egyenleg = 10000
    while egyenleg > 0:
        tipus = menu()
        os.system('cls')
        match tipus:
            case 1:
                valt = oddEven()
            case 2:
                valt = smallBig()
            case 3:
                 valt = tucat()
            case 4:
                valt = oszlop()
            case 5:
                valt = oneNumber()
            case 6:
                valt = redBlack()
            case 0:
                sys.exit()
        egyenleg += valt
        print(f'Az egyenlege: {egyenleg}')

def displayerstat(money):
    print('━━━━━━━━━━━━━━━━━━━━━━')
    print(f'HP: {player.hp}, Védésém: {player.shield}, Fegyver: {player.weapon} Erő: {player.strength}\nSebesség: {player.speed}, Éberség: {player.eberseg}, Ügyesseg: {player.agility}')
    print('Pénz:', money)
    print('━━━━━━━━━━━━━━━━━━━━━━')
    print('\n')
    print('━━━━━━━━━━━━━━━━━━━━━━')
    print(f'HP: {player.hp}, Védésém: {player.shield}, Fegyver: {player.weapon} Erő: {player.strength}\nSebesség: {player.speed}, Éberség: {player.eberseg}, Ügyesseg: {player.agility}')
    print('Pénz:', money)
    print('━━━━━━━━━━━━━━━━━━━━━━')
    print('\n')


def heal(amount):
    if amount + player.hp > 100:
        player.hp = 100
    else:
        player.hp += amount


def takeDamage(value):
    player.hp -= value
    if player.hp < 1:
        print('Belehaltál sérüléseidbe.')
        time.sleep(2)
        print('\n')
        print('━━━━━━━━━━━━━━━━━━━━━━')
        print('VÉGE A JÁTÉKNAK.')
        print('━━━━━━━━━━━━━━━━━━━━━━')
        
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
                        print(i, '...', weapon.name)
                        i += 1
                    itemindex = 9999
                    while not itemindex < len(Cweapon):
                        itemindex = int(input('Melyiket szeretnéd használni? (a fegyver sebzése): ')) - 1
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
                        print(i, '...', armor.name)
                        i += 1
                    itemindex = 9999
                    while not itemindex < len(Carmor):
                        itemindex = int(input('Melyiket szeretnéd használni? (A pajzs védelme): ')) - 1
                Earmor = Carmor[itemindex].shield
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
                    print(i, '...', shield.name)
                    i += 1
                itemindex = 9999
                while not itemindex < len(Cshield):
                    itemindex = int(input('Melyiket szeretnéd használni? (A pajzs védelme): ')) - 1
            EShield = Cshield[itemindex].shield
            player.shield = EShield + Earmor


def torles(money):
    os.system('cls')
    displayerstat(money)

def tovabblepes():
    print('\n\n\n')
    displayerstat(money)


def Slowtype(text):

    for i in text:
        print(i, end='')
        time.sleep(0.05)
    print()


def ido(eltMinute=0, eltHour=0, eltDay=0):
    global hour, minute, day
    minute += eltMinute
    hour += eltHour
    day += eltDay
    while minute >= 60:
        minute -= 60
        hour += 1

    if not hour < 22:
        if nowplace == 'city' or 'castle':
            print('Elmentél a szállásra aludni.')
            player.eberseg = 100
        else:
            print('A vadonban aludtál.')
            player.eberseg == 75
        hour = 6
        minute = 0


def repchange(amount):
    player.rep += amount
    if amount < 0:
        print(f'Megbecsültséged ennyivel csökkent: {-amount}.')
    if amount > 0:
        print(f'Megbecsültséged ennyivel nőtt: {amount}.')
    if player.rep < -50:
        # prison()
        pass
        sys.exit()


def fight(enemy):
    global money, goblin, ogre, bandit, cerberus, vampir
    print(money)
    while enemy.hp >= 0:
        print(f'ellenfeled hp: {enemy.hp}, sebessége: {enemy.speed}, ereje: {enemy.strength}, védelme: {enemy.shield}')
        if player.speed <= enemy.speed:
            print('Ő a gyorsabb ő támad először')
            enemydamage = enemy.strength - player.shield
            if enemydamage < 0:
                enemydamage = 0
            print(f'az ellenfeled-et {enemydamage}-et  sebzett.')
            if str(enemy) == 'vampir':
                enemy.hp += enemydamage
            playerdamage = player.strength * player.weapon - enemy.shield + randint(-2, 2)
            if playerdamage < 0:
                playerdamage = 0
            print(f'Te {playerdamage}-et sebeztél.')
            takeDamage(enemydamage)
            enemy.hp -= playerdamage
            input('ENTER-rel tovább')
            torles(money)

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
            input('ENTER-rel tovább')
            torles(money)
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
    # if not str(place) in PLACE:
    #     print(f'{place} not in PLACE')
    #     return 0
    if nowplace == place:
        print('Már ott vagy')
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
        if randint(1, 3) == 1:
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
    print('Sikeresen megérkeztél ide: {nowplace}')
    input('ENTER')
    torles()


def field():
    if nowplace == 'field':
        goto('field')
    print('1...gyógynövényt szedni')
    print('1...Legyőzni a bosst')
    val = input('Mit szeretnél csinálni')
    match val:
        case '1':
            fieldMiniGame()
        case '2':
            fieldBossFight()


def forest():
    if nowplace == 'forest':
        goto('forest')
    print('1..fát vágni')
    print('2...legyőzni a bosst')
    val = input('Mit szeretnél csinálni')
    match val:
        case '1':
            forestMiniGame()
        case '2':
            forestBossFight()


def mine():
    if nowplace == 'mine':
        goto('mine')
    print('1..válogatni')
    print('2...legyőzni a bosst')
    val = input('Mit szeretnél csinálni')
    match val:
        case '1':
            mineMiniGame()
        case '2':
            mineBossFight()
        
if __name__ == '__main__':
    player.strength = 5
    player.weapon = 7
    fight(vampir)
