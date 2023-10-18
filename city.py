from classes import *
from variables import *
from definialas import *

def shop():
    global money
    list = 0
    torles()
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
                getItem(type='weapon', item = item)
            else:
                Slowtype(text='Nincs pénzed erre a fegyverre')
           
                
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
                getItem(type='shield', item = item)
            else:
                Slowtype(text='Nincs pénzed erre a páncélra')
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
                getItem(type='armor', item = item)
            else:
                Slowtype(text='Nincs pénzed erre a pajzsra')

def hospital():
    global money
    torles()
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

if __name__ == '__main__':
    money = 1000
    city()
    print(money)
    displayerstat()
    input('efae')