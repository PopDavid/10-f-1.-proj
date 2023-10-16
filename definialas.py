from Entities import *
from variables import *
from random import randint, choice

Eweapon = False
EShield = False
Earmor = False

def displayerstat():
    print(f'Hp: {player.hp}, erő: {player.strength}, pajzs: {player.shield},sebesseg {player.speed}, éberség: {player.eberseg}, ügyesseg: {player.agility}')

def randgetItem():
    global Eweapon, EShield, Earmor
    choiceItem = ''
    choiceList = choice(UCItems)
    choiceList = UCweapons
    getItemkey, getItemValue = choice(list(choiceList.items())) 
    del choiceList[getItemkey]
    Cweapon[getItemkey] = getItemValue
    match str(choiceList):
        case 'UCweapon':
            if Eweapon == False:
                pass
            else:
                for i in Cweapon:
                    print(i)
                while not choiceItem in Cweapon:
                    choiceItem = input('Melyiket szeretné? (a fegyver sebzése): ')
            value = Cweapon.get(choiceItem)
            player.weapon = value
            Eweapon = True
        case 'UCarmor':
            if Earmor == False:
                pass
            else:
                for i in Carmor:
                    print(i)
                while not choiceItem in Carmor:
                    choiceItem = input('Melyiket szeretné? (a páncél sebzése): ')
            value = Carmor.get(choiceItem)
            player.shield += value
            Earmor = True
        case 'UCshield':
            if EShield == False:
                pass
            else:
                for i in Cshield:
                    print(i)
                while not choiceItem in Cshield:
                    choiceItem = input('Melyiket szeretné? (a pajzs sebzése): ')
            value = Cshield.get(choiceItem)
            player.shield += value
            Earmor = True

def getItem(type, item):
    global Eweapon, EShield, Earmor
    choiceItem = ''
    match type:
        case 'weapon':
            choiceList = UCItems[0]
        case 'shield':
            choiceList = UCItems[1]
        case 'armor':
            choiceList = UCItems[2]
    getItemkey = item
    getItemValue = choiceList[item]

    del choiceList[getItemkey]
    Cweapon[getItemkey] = getItemValue
    match type:
        case 'weapon':
            if Eweapon == False:
                pass
            else:
                for i in Cweapon:
                    print(i)
                while not choiceItem in Cweapon:
                    choiceItem = input('Melyiket szeretné? (a fegyver sebzése): ')
            value = Cweapon.get(choiceItem)
            player.weapon = value
            Eweapon = True
        case 'armor':
            if Earmor == False:
                pass
            else:
                for i in Carmor:
                    print(i)
                while not choiceItem in Carmor:
                    choiceItem = input('Melyiket szeretné? (a páncél sebzése): ')
            value = Carmor.get(choiceItem)
            player.shield += value
            Earmor = True
        case 'shield':
            if EShield == False:
                pass
            else:
                for i in Cshield:
                    print(i)
                while not choiceItem in Cshield:
                    choiceItem = input('Melyiket szeretné? (a pajzs sebzése): ')
            value = Cshield.get(choiceItem)
            player.shield += value
            Earmor = True



            
