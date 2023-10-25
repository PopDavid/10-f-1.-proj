from classes import *
from variables import*
from definialas import *
from quest import *
from random import *

def shop():
    global money
    list = 0
    torles()
    displayerstat(money)

    print('pénz:', money)
    # Slowtype('1...Vásárolni')
    # Slowtype('2...Eladni')
    # while act != '1' and act != '2':
    #     act = input('Mit szeretnél csinálni?')
    print('1...fegyver')
    print('2...pajzs')
    print('3...páncél')

    while list != '1' and list != '2' and list != '3':
        list = input('Mit szeretnél vásárolni? ')
    torles()
    displayerstat(money)

    match list:
        case '1':
            i = 1
            for weapon in WEAPON:
                print(i,'...', weapon.name, 'price:', weapon.price)
                i += 1
            itemindex = 9999
            while not itemindex < len(WEAPON):
                itemindex = int(input('Melyiket szeretnéd Megvenni? (a fegyver sebzése): '))-1
            item = WEAPON[itemindex]
            if item.price <= money:
                money -= item.price
                torles()
                displayerstat(money)

                getItem(type='weapon', item = item)
            else:
                print(text='Nincs pénzed erre a fegyverre')
           
                
        case '2':
            i = 1
            for weapon in SHIELD:
                print(i,'...', weapon.name, 'price:', weapon.price)
                i += 1
            itemindex = 9999
            while not itemindex < len(SHIELD):
                itemindex = int(input('Melyiket szeretnéd Megvenni? (a páncél védelme): '))-1
            item = SHIELD[itemindex]
            if item.price <= money:
                money -= item.price
                torles()
                displayerstat(money)

                getItem(type='shield', item = item)
            else:
                print(text='Nincs pénzed erre a páncélra')
        case '3':
            i = 1
            for weapon in ARMOR:
                print(i,'...', weapon.name, 'price:', weapon.price)
                i += 1
            itemindex = 9999
            while not itemindex < len(ARMOR):
                itemindex = int(input('Melyiket szeretnéd Megvenni? (a pajzs védelme): '))-1
            item = ARMOR[itemindex]
            if item.price <= money:
                money -= item.price
                torles()
                displayerstat(money)

                getItem(type='armor', item = item)
            else:
                print(text='Nincs pénzed erre a pajzsra')

def hospital():
    global money
    torles()
    displayerstat(money)

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
    torles()
    displayerstat(money)


    print('pénzed:', money)
    print(f'erő: {player.strength}, ügyesség: {player.agility}, sebesség: {player.speed}')
    needMSr = int(player.strength *15 + 5)
    needMA = int(player.agility * 15 + 5)
    needMSp = int(player.speed * 15 + 5)
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

def leaveCity():
    pass

def city():
    print('1...kereskedőház')
    print('2...Korház')
    print('3...gym')
    print('4...küldetésfal')
    print('5...pénz gyüjteni a városban')
    print('0...Ki a városból')
    
    choice = ''

    while not choice in opcio5:
        choice = input('Hová szeretnék menni? ')
    match choice:
        case '1':
            shop()
        case '2':
            gym()
        case '3':
            questboard()
        case '4':
            questboard()
        case '5':
            collectmoney()
        case '0':
            leaveCity()

def castle():
    print('1...Szállás')
    print('2...Edzőterem')
    print('3...Kaszinó')
    print('4...Várkert')
    print('5...Kincstár')
    print('6...Kórház')
    print('7...Kereskedőház')
    print('8...Küldetésfal')
    print('9...Várbörtön')
    print('0...Vár elhagyása')
    
    choice = ''

    while not choice in opcio5:
        choice = input('Hová szeretnék menni? ')
    match choice:
        case '1':
            hostel()
        case '2':
            gym()
        case '3':
            casino()
        case '4':
            questboard()
        case '5':
            treasury()
        case '6':
            hospital()
        case '7':
            shop()
        case '8':
            questboard()
        case '9':
            prison()
        case '0':
            city()



def hostel():
    pass

def casino():
    pass

def treasury():
    pass

def prison():
    pass



if __name__ == '__main__':
    money = 1000
    while True:
        city()
