import os
from classes import *
from variables import *
from random import randint, choice

Eweapon = 0
EShield = 0
Earmor = 0

def displayerstat():
    print(f'Hp: {player.hp}, erő: {player.strength}, pajzs: {player.shield},sebesseg {player.speed}, éberség: {player.eberseg}, ügyesseg: {player.agility}')


def getItem(type, item):
    global Eweapon, EShield, Earmor, money

    match type:
        case 'weapon':
            if not item in UCweapons:
                money += item.price
            else:
                itemindex = UCweapons.index(item)

                UCweapons.remove(item)
                Cweapon.append(item)
                if Eweapon == '':
                    pass
                else:
                    item = ''
                    for weapon in Cweapon:
                        print(weapon.name)

                    while not item in [weapon.name for weapon in Cweapon]:
                        item = input('Melyiket szeretnéd használni? (a fegyver sebzése): ')

                    itemindex = [weapon.name for weapon in Cweapon].index(item)
                Eweapon = Cweapon[itemindex].damage
                player.weapon = Eweapon

        case 'armor':
            if not item in UCarmor:
                money += item.price
            else:
                itemindex = UCarmor.index(item)

                UCarmor.remove(item)
                Carmor.append(item)
                if Earmor == '':
                    pass
                else:
                    item = ''
                    for armor in Carmor:
                        print(armor.name)

                    while not item in [weapon.name for weapon in Carmor]:
                        item = input('Melyiket szeretnéd használni? (a páncél védelme): ')

                    itemindex = [weapon.name for weapon in Carmor].index(item)
                Earmor = Cweapon[itemindex].shield
                player.shield = Earmor + Eshield

        case 'shield':
            if not item in UCshield:
                money += item.price
            else:
                for i in Cshield:
                    print(i)
                while not choiceItem in Cshield:
                    choiceItem = input('Melyiket szeretné? (a pajzs sebzése): ')
            value = Cshield.get(choiceItem)
            player.shield += value
            Earmor = True



            
