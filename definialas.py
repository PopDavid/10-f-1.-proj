import os
from classes import *
from variables import *
import time

Eweapon = 0
EShield = 0
Earmor = 0


def displayerstat():
    print('---------------------------------------')
    print(f'HP: {player.hp}, Védésém: {player.shield}, Fegyver: {player.weapon} Erő: {player.strength}\nSebesseg {player.speed}, éberség: {player.eberseg}, ügyesseg: {player.agility}')
    print('---------------------------------------')


displayerstat()

def getItem(type, item):
    global Eweapon, EShield, Earmor, money

    match type:
        case 'weapon':
            if not item in WEAPON:
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
            if not item in ARMOR:
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
            if not item in SHIELD:
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
    displayerstat()

def Slowtype(text):
    for i in text:
        print(i, end='')
        time.sleep(0.1)
    print()

