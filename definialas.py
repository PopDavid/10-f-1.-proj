import os
from classes import *
from variables import *

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
                itemindex = UCshield.index(item)

                UCshield.remove(item)
                Cshield.append(item)
                if Eshield == '':
                    pass
                else:
                    item = ''
                    for shield in Cshield:
                        print(shield.name)

                    while not item in [weapon.name for weapon in Cshield]:
                        item = input('Melyiket szeretnéd használni? (a pajzs védelme): ')

                    itemindex = [weapon.name for weapon in Cshield].index(item)
                Eshield = Cweapon[itemindex].shield
                Earmor = Cweapon[itemindex].shield
                player.shield = Earmor + Eshield


def shop():
    global money
    list = 0
    os.system('cls')
    # print('1...Vásárolni')
    # print('2...Eladni')
    # while act != '1' and act != '2':
    #     act = input('Mit szeretnél csinálni?')
    print('1...Fegyver')
    print('2...pajzs')
    print('3...páncél')

    while list != '1' and list != '2' and list != '3':
        list = input('Mit szeretnél vásárolni? ')
    match list:
        case '1':
            for i in UCweapons:
                print(i, 'price:', i.price)
            item = 0
            run = True
            while run:
                item = input('Melyiket szeretnéd? (a fegyver sebzése): ')

                # Check if the input matches the name of a weapon in UCweapons
                matching_weapons = [weapon for weapon in UCweapons if weapon.name == item]

                if matching_weapons:
                    # If there's a match, assume the first matching weapon is the selected one
                    selected_weapon = matching_weapons[0]

                    if selected_weapon.price <= money:
                        # Check if the selected weapon's price is within the budget
                        item = selected_weapon
                        run = False
                    else:
                        print("Nincs elég pénzed ehhez a fegyverhez!")
                else:
                    print("Nincs ilyen fegyver a listán. Kérlek válassz egy létező fegyvert.")
            getItem('weapon', item)
        case '3':
            for i in UCarmor:
                print(i, 'price:', i.price)
            item = 0
            run = True
            while run:
                item = input('Melyiket szeretnéd? (a páncél védelme): ')

                # Check if the input matches the name of a weapon in UCarmor
                matching_armor = [weapon for weapon in UCarmor if weapon.name == item]

                if matching_armor:
                    # If there's a match, assume the first matching weapon is the selected one
                    selected_weapon = matching_armor[0]

                    if selected_weapon.price <= money:
                        # Check if the selected weapon's price is within the budget
                        item = selected_weapon
                        run = False
                    else:
                        print("Nincs elég pénzed ehhez a páncélhoz!")
                else:
                    print("Nincs ilyen fegyver a listán. Kérlek válassz egy létező fegyvert.")
            getItem('armor', item)
        case '2':
            for i in UCshield:
                print(i, 'price:', i.price)
            item = 0
            run = True
            while run:
                item = input('Melyiket szeretnéd? (a pajzs védelme): ')

                # Check if the input matches the name of a weapon in UCarmor
                matching_armor = [weapon for weapon in UCshield if weapon.name == item]

                if matching_armor:
                    # If there's a match, assume the first matching weapon is the selected one
                    selected_weapon = matching_armor[0]

                    if selected_weapon.price <= money:
                        # Check if the selected weapon's price is within the budget
                        item = selected_weapon
                        run = False
                    else:
                        print("Nincs elég pénzed ehhez a fegyverhez!")
                else:
                    print("Nincs ilyen fegyver a listán. Kérlek válassz egy létező fegyvert.")
            getItem('shield', item)

def hospital():
    global money
    print('pénzed: ', money)
    print('Életerőd: ', player.hp)
    print('1...Szeretnék meggyógyulni')
    print('0... Semmit')
    valasz = input('Mit szeretnél csinálni? ')
    if valasz != '1':
        pass
    else:
        healprice = int((100 - player.hp) * 1.5)
        if healprice <= money:
            player.hp = 100
            money -= healprice


def gym():
    global money
    print('pénzed:', money)
    print(f'erő: {player.strength}, ügyesség: {player.agility}, sebesség: {player.speed}')
    needMSr = int(player.strength * 2.5 + 5)
    needMA = int(player.agility * 2.5 + 5)
    needMSp = int(player.speed * 2.5 + 5)
    print(f'1...erő (ár: {needMSr})')
    print(f"2...ügyesség (ár: {needMA})")
    print(f"3...sebesség (ár: {needMSp})")
    val = input('Melyiket szeretnéd választani? ')
    match val:
        case '1':
            needmoney = needMSr
        case '2':
            needmoney = needMA
        case '3':
            needmoney = needMSp

    if money >= needmoney:
        money -= needmoney
        match val:
            case '1':
                player.strength += 1
            case '2':
                player.agility += 1
            case '3':
                player.speed += 1
    else:
        print('Nincs elég pénzed')
    
def questboard():
    pass

def leaveCity():
    pass

def city():
    print('1...kereskedőház')
    print('2...Korház')
    print('3...gym')
    print('4...küldetésfal')
    print('0...Ki a városból')
    
    choise = input('Hová szeretnék menni? ')
    match choise:
        case '1':
            shop()
        case '2':
            hospital()
        case '3':
            gym()
        case '4':
            questboard()
        case '0':
            leaveCity()
    print('NEKNGk')




if __name__ == '__main__':
    city()
