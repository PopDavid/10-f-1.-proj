from quest import *
del money
from variables import money
def shop():
    global money
    list = 0
    torles(money)

    # Slowtype('1...Vásárolni')
    # Slowtype('2...Eladni')
    # while act != '1' and act != '2':
    #     act = input('Mit szeretnél csinálni?')
    print('1...fegyver')
    print('2...pajzs')
    print('3...páncél')

    while list != '1' and list != '2' and list != '3':
        list = input('Mit szeretnél vásárolni? ')
    torles(money)


    match list:
        case '1':
            i = 1
            for weapon in WEAPON:
                print(i,'...', weapon.name, 'price:', weapon.price)
                i += 1
            itemindex = 9999
            val = ' '
            while val not in map(str, range(1, 5)):
                val = input('Melyiket szeretnéd Megvenni? (a fegyver sebzése): ')
            itemindex = int(val)-1
            item = WEAPON[itemindex]
            if item.price <= money:
                money -= item.price
                torles(money)

                getItem(type='weapon', item = item)
            else:
                print('Nincs pénzed erre a fegyverre')
           
                
        case '2':
            i = 1
            for weapon in SHIELD:
                print(i,'...', weapon.name, 'price:', weapon.price)
                i += 1
            itemindex = 9999
            while val not in map(str, range(1, 5)):
                val = input('Melyiket szeretnéd Megvenni? (a fegyver sebzése): ')
            itemindex = int(val)-1
            item = SHIELD[itemindex]
            if item.price <= money:
                money -= item.price
                torles(money)

                getItem(type='shield', item = item)
            else:
                print('Nincs pénzed erre a páncélra')
        case '3':
            i = 1
            for weapon in ARMOR:
                print(i,'...', weapon.name, 'price:', weapon.price)
                i += 1
            itemindex = 9999
            while val not in map(str, range(1, 5)):
                val = input('Melyiket szeretnéd Megvenni? (a fegyver sebzése): ')
            itemindex = int(val)-1
            item = ARMOR[itemindex]
            if item.price <= money:
                money -= item.price


                getItem(type='armor', item = item)
            else:
                print('Nincs pénzed erre a páncél')
    input('Vissza a várba ENTER-rel')
    torles(money)
    castle()

def hospital():
    global money
    torles(money)
    print('1...Szeretnék meggyógyulni')
    print('0... Semmit')
    valasz = input('Mit szeretnél csinálni? ')
    if valasz != '1':
        input('Vissza a Várba ENTER-rel')
    else:
        healprice = int((100 - player.hp) * 1.5)
        if healprice <= money:
            player.hp = 100
            money -= healprice
        input('Meggyógyultál, Vissza a Várba ENTER-rel')
    torles(money)
    castle()

def gym():
    global money
    torles(money)
    print(f'erő: {player.strength}, ügyesség: {player.agility}, sebesség: {player.speed}')
    needMSr = int(player.strength *15 + 5)
    needMA = int(player.agility * 15 + 5)
    needMSp = int(player.speed * 15 + 5)
    print(f'1...erő (ár: {needMSr})')
    print(f"2...ügyesség (ár: {needMA})")
    print(f"3...sebesség (ár: {needMSp})")
    print(f"0...Vissza a várba")

    val = input('Melyiket szeretnéd választani? ')
    while val not in map(str, range(0, 4)):
        val = input('Melyiket szeretnéd választani? ')

    match val:
        case '1':
            needmoney = needMSr
        case '2':
            needmoney = needMA
        case '3':
            needmoney = needMSp
    if val != '0':
        if money >= needmoney:
            money -= needmoney
            match val:
                case '1':
                    player.strength += 1
                    print('Erősebb lettél')                    
                case '2':
                    player.agility += 1
                    print('Ügyesebb lettél')
                case '3':
                    player.speed += 1
                    print('Gyorsabb lettél')
        else:
            print('Nincs elég pénzed')
        input('Városba visszatérés ENTER-rel')
    torles(money)
    castle()

def leaveCity():
    torles(money)
    print('1...Erdő')
    print('2...Mező')
    print('3...Bánya')
    print('4...Hegység')
    print('0...Vissza a városba')
    val = input('Hová szeretnél menni: ')
    while val not in map(str, range(0, 5)):
        val = input('Hová szeretnél menni: ')
    torles(money)
    match val:
        case '1':
            print(money)
            forest()
        case '2':
            field()
        case '3':
            mine()
        case '4':
            mountain()
    castle()


def castle():
    if nowplace != 'city':
        goto('city')
    print('1...Szállás')
    print('2...Edzőterem')
    print('3...Kaszinó')
    print('4...Várkert')
    print('5...Kincstár')
    print('6...Kórház')
    print('7...Kereskedőház')
    print('8...Küldetésfal')
    print('9...Várbörtön')
    print('10...Állatkereskedő')
    print('0...Vár elhagyása')
    
    choice = ''

    while choice not in map(str,range(0, 11)):
        choice = input('Hová szeretnék menni? ')
    match choice:
        case '1':
            hostel()
        case '2':
            gym()
        case '3':
            casino()
        case '4':
            castlegarden()
        case '5':
            treasury()
        case '6':
            hospital()
        case '7':
            shop()
        case '8':
            questboard()
            torles(money)
            castle()
        case '9':
            prison()
        case '10':
            animaltrader()
        case '0':
            leaveCity()

def animaltrader():
    global money, lo
    torles(money)
    print('1...lovat (300)')
    print('2...disznót (200)')
    print('0...semmit (0)')
    val = input('Mit szeretnél venni? ')
    while val not in map(str, range(0,3 )):
        val = input('Mit szeretnél venni? ')
    match val:
        case '1':
            if not lo:
                lo = True
                print('Sikeresen vettél egy lovat')
                money -= 300
            else:
                if input('már van lovad, biztosan veszel mégegyet? ') != 'nem':
                    print('Sikeresen vettél még egy lovat')
                    money -= 300

        case '2':
            print('sikeresen vettél egy disznót')
            money -= 200
    input('Vissza a várba ENTER-rel')
    torles(money)
    castle()

def castlegarden():
    torles(money)
    if lo:
        if isdragonalive:
            print('a lovagi torna a sárkány legyőzése után kerül megrendezésre')
        elif bool(input('Szeretnél benevezni a lovagi tornára? ')):
            print('megvan az elegendő versenyző, indul a küzdelem')
        else:
            print('Majd gyere vissza ha van kedved')
            knight()
    else:
        print('Ló nélkül nehéz lesz LÓvagi tornán részt venni')
    input('Vissza a városba ENTER-rel')
    torles(money)
    castle()
            
def knight():
    pass
                
def hostel():
    torles(money)
    print('Munka van nem a pihenés ideje')
    input('Vissza a várba ENTER-rel')
    torles(money)
    castle()

def casino():
    pass

def treasury():
    torles(money)
    if isdragonalive:
        print('Bárcsak sok pénzem lenne itt.')
    input('Vissza a várba ENTER-rel')
    torles(money)
    castle()

def prison():
    torles(money)
    print('Bizz bennem, nem szeretnél ide jutni')
    input('Vissza a várba ENTER-rel')
    torles(money)
    castle()



if __name__ == '__main__':
    money = 10000
    player.shield = 16
    player.weapon = 11
    player.strength = 5
    torles(money)
    castle()
