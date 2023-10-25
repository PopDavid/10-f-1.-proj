from classes import *
from variables import *
from definialas import *
from random import choice
import time


def collectmoney():
    print('Még kéne egy kis pénz')
    print('1...lopni')
    print('2...kéregetni')
    print('3...dolgozni')
    val = input('Hogyam szeretnél pénzt szerezni')
    match val:
        case '1':
            cmoney = steal()
        case '2':
            cmoney = begging()
        case '3':
            cmoney = work()
    return cmoney


def steal():
    global money
    happening = randint(1, 100)
    if happening in range(1, 6):
        print('megloptál egy haljéktalant, nem vett észre.')
        money += 20
        ido(15)
        return 20
    elif happening in range(6, 21):
        print('megloptál egy haljéktalant, felismert. Csökkent a negítélésed.')
        money += 20
        player.rep -= 30
        ido(15)
        return 20
    elif happening in range(21, 51):
        print('Megprobáltál lopni, nem sikerült.')
        player.rep -= 30
        ido(15)
        return 0
    elif happening in range(51, 81):
        print('megpróbáltál lopni, elkaptak, megvertek')
        player.rep -= 30
        player.hp -= 20
        ido(15)
        return 0

    elif happening in range(81, 96):
        print('Elkaptak, megvertek, elvettek töled egy kevés pénzt')
        player.hp -= 20
        money -= 30
        player.rep -= 30
        ido(15)
        return -30

    elif happening in range(96, 101):
        print('megprobáltal lopni egy hajléktalantól, nem sikerült.\njól megvert, és ő vette el a te pénzed, csökkent a megítélésed.')
        player.hp -= 30
        money -= 50
        player.rep -= 30
        ido(15)
        return -50


def begging():
    global money

    print('1...idő')
    print('2...pénz')
    type = input('Meddig szeretnél kéregetni?')
    vmin = 0
    vhour = 0
    match type:
        case '1':
            cMoney = 0
            print(cMoney)
            kmin, khour = input('Mennyi időt szeretnél kéregetni? (perc ora)').split()
            kmin, khour = int(kmin), int(khour)

            while kmin >= 60:
                kmin -= 60
                khour += 0
            while kmin > vmin or khour > vhour:
                randomszam = randint(1, 3)
                if randomszam == 1:
                    cMoney += 2
                vmin += 5
                ido(5, 0, 0)
                while vmin >= 60:
                    vmin -= 60
                    vhour += 1
            print(cMoney, 'pénz szereztél')
            money += cMoney
            input('Press enter')
            torles()
        case '2':
            cMoney = 0
            print(cMoney)
            gMoney = int(input('Mennyi pénz szeretnél gyűjteni? '))
            while cMoney < gMoney:
                randomszam = randint(1, 3)
                if randomszam == 1:
                    cMoney += 2
                vmin += 5
                ido(5, 0, 0)
                while vmin >= 60:
                    vmin -= 60
                    vhour += 1
            print(f'{vmin} perc, {vhour} óra telt el')
    return cMoney


def work():
    global money
    if player.rep < 50:
        print('Nem kaptál munkát mert nem jó a megítélésed')
        return 0
    if player.rep <= 60:
        print('vécépucoló lettél, kevés fizetéssel (10 / óra)')
        payment = 5
    elif player.rep <= 70:
        print('takarítási munkákat vállaltál áll relatíív kevés fizetéssél (20 / óra)')
        payment = 20
    elif player.rep <= 85:
        print('papírmunkát végzel egy nagy banknak, relatív nagy fizetésért (35 / óra)')
        payment = 35
    elif player.rep <= 100:
        print('helyet kaptál a király személyes védőkárdájában, nagy fizetésért. (50 / óra)')
        payment = 50
    whour = int(input('hány órát szeretnél dolgozni? '))
    cMoney = whour * payment
    print(cMoney, 'pénz szereztél')
    money += cMoney
    ido(0, whour)
    return cMoney


def PALjatek():
    global Palvolt, pal, PAL
    torles()
    Slowtype('Játék: Odamegy hozzád egy öreg özvegy néni.')
    Slowtype('özvegy: Jó napot fiatal ember.\nözvegy: Ön nagyon hasonlít a férjemre. Őt Bogáncs Pálnak hívták.\nTiszteletére megkérlek, hogy mondjál annyi szót PÁLlal, amennyit csak tudsz 1 perc alatt.')
    input('ENTERrel kezdés')
    startTime = time.time()
    score = 0
    while time.time() - startTime < 60:
        val = input('Szó:').lower()
        if val in pal:
            score += 1
            pal.remove(val)
            print(f'Helyes')
        elif val in PAL:
            print('Volt már')
        else:
            print(f'Helytelen')
    pal = []
    for elem in PAL:
        pal.append(elem)
    if not Palvolt:
        Slowtype('özvegy: Nagyon jól teljesítettél.\nözvegy: Itt van egy kis pénz a szórakozásért')
        rew = score * 3
        Slowtype(f'játék: kaptál {rew} pénzt a banyától.')
        Palvolt = True
    else:
        Slowtype(f'özvegy: Nagyon jól teljesítettél.\nözvegy pontosan {score} szót mondtál helyesen')


def sidequest():
    match currentquest:
        case 'pénzgyűjtés fegyverre':
            collectmoneyquest()
        case 'vadászat':
            hunting()
        case 'gyűjtőgetés':
            collecting()
        case 'ogrevadászat':
            ogrehunt()
        case 'király kísérés':
            kingfollow()
        # case 'kard a kőben':
        #     swordInStone()


def hunting():
    global currentquest, money
    esely = 4 - player.agility
    if esely < 1:
        esely = 1
    print('a vadászok előrementek a mezőre, neked is oda kéne menned.')
    goto('field')
    Slowtype('vadászok: a cél 10 vadat elejteni.')
    input('ENTER-rel kezdődik a vadászat')
    vadak = 0
    while vadak != 5:
        torles()
        while randint(1, 4) != 1:
            print('vársz')
            ido(5)
            time.sleep(1.5)
            ido(10)
        torles()
        print('meglátsz egy prédát')
        time.sleep(2)
        print('rácélzol')
        time.sleep(2)
        print('lösz')
        time.sleep(2)
        if randint(1, esely) == 1:
            vadak += 1
            print(f'Eltaláltad, már csak {5-vadak} prédát kell meglőnöd.')
        else:
            print(f'Nem találtad el, még {5-vadak} prédát kell meglőnöd.')
        input('ENTER')
    print('eladtad a vadat a vadászoknak, kaptál érte 50 pénzt')
    money += 50
    currentquest = 'gyűjtőgetés'


def collecting():
    global currentquest, money
    print('A király fia beteg.\ntalán ha szednék neki egy kis gyógyfüzet a mezőről kapnék egy kis jutalmat.')
    if nowplace != 'field':
        goto('field')
    torles()
    esely = 5 - player.speed
    if esely < 1:
        esely = 1
    need = 20
    while need != 0:
        while randint(1, esely) != 1:
            print('nézelődsz')
            time.sleep(1.5)
        find = randint(1, 3)
        if need - find > 0:
            need -= find
            print(f'találtál {find} növényt ami neked kell. Már csak {need} növényt kell keresni')
            input('ENTER')
            torles()
        else:
            need = 0
            print(f'találtál {find} növényt ami neked kell. Megvan amiért jöttél')
            input('ENTER')
            torles()
            print('Vissza kéne menni a városba.')
            goto('city')
            print('Leadtad a gyógynövényeket, kaptál érte 50 pénzt')
            money += 50
           #  currentquest = 'ogrevadászat'

def collectingFirst():
    global currentquest, money
    Slowtype('[SZOLGA]: A király fia megbetegedett! Mai feladatod, hogy gyógynövényeket szedj neki a mezőn!')
    time.sleep(1)
    Slowtype('(Gondolat): Remélem ezért jutalomban fogok részesülni!')
    time.sleep(2)
    nowplace = 'field'
    print('Sikeresen megérkeztél ide: {nowplace}')
    torles()
    esely = 5  - player.speed
    if esely < 1:
       esely = 1
    need = 20
    while need != 0:
        while randint(1, esely) != 1:
            print('Gyógynövény után kutatsz.')
            time.sleep(1.5)
        find = randint(1, 3)
        if need -find > 0:
            need -= find
            print(f'Találtál {find} növényt, melyre szükséged is van. Már csak {need} növényt kell találnod.')
            input('ENTER')
            torles()
        else:
            need = 0
            Slowtype(f'[]Megtaláltam a {find} növényt. Megvan amiért jöttem!')
            time.sleep(1)
            input('\Visszatérés a városba az ENTER megnyomásával >>')
            torles()
            nowplace = 'city'
            print('Leadtad a gyógynövényeket, 50 pénz üti markod.')
            money += 50
           


def knightquest():
    if not lo:
        print('nincs lovad, gyere vissza ha lesz.')


def ogrehunt():
    global currentquest, money
    print('A hegy kség el van árasztva ogrével.\noda kéne menni, egy kicsit szétcsapni közöttük.')
    goto('mountain')
    print('mások is vannak itt, besegítek nekik')
    needKillogre = 3
    while needKillogre != 1:
        fight(ogre)
        needKillogre -= 1
        print(f'ez nehéz küzdelem volt. már csak {needKillogre} ogrét kell megöljek')
        input('ENTER')
    fight(ogre)
    print('Ezek nehéz küldelmek voltak. A helybéliektől kaptál 75 pénzt a segítségért.')
    money += 75
    currentquest = 'király kísérés'


def kingfollow():
    global money, currentquest
    print('a király el szeretne látogatni a bányába. Őrséget keres maga mellé.')
    print('Jó pénzt ígér ha én is segítek megvédelni.')
    print('jelentkeztél, elindultatok')
    for _ in range(randint(3, 5)):
        print('Mentek')
        time.sleep(1)
    time.sleep(2)
    print('az úton egy csapat jól felfegyverkezet bandita támadt rátok.')
    needKillBandit = 5
    while needKillBandit != 1:
        fight(bandit)
        needKillBandit -= 1
        print(f'ez nehéz küzdelem volt. Már csak {needKillBandit} banditát kell megöljek')
        input('ENTER')
    fight(bandit)
    print('ezek nehéz küldelmek voltak. A király bátorító beszédet tartott, megköszönte a védelmet.')
    Slowtype('király: Hálám jeléül minden vitéz harcos, aki túlélte a támadást kap 50 pénzt pluszba.')
    Slowtype('király: Az meghalt vitézek családjai 150 arany kárpótlást kapnak elesett családjukért, akik vitézül harcoltak.')
    money += 50
    print('továbbindultatok.')
    for _ in range(randint(5, 10)):
        print('Mentek')
        time.sleep(1)
    print('már majdnem célba értetek amikor egy falka cerberus támadt rátok.')
    needKillCerberus = 10
    while needKillCerberus != 1:
        fight(cerberus)
        needKillCerberus -= 1
        print(f'ez nehéz küzdelem volt. Már csak {needKillCerberus} cerberust kell megöljek')
        input('ENTER')
    fight(cerberus)
    print('ezek nehéz küzdelmek voltak. A király megint megdícsért minket')
    Slowtype('király: Hálám jeléül minden vitéz harcos, aki túlélte a támadást kap 75 pénzt pluszba.')
    Slowtype('király: Az meghalt vitézek családjai 225 arany kárpótlást kapnak elesett családjukért, akik vitézül harcoltak.')
    money += 75
    for _ in range(randint(3, 5)):
        print('mentek ')
        time.sleep(1)
    print('célba értetek.')
    Slowtype('király:Bátran harcoltatok vitéz zsoldosaim, mindenki fizetsége legyen 150 arany az útért.')
    money += 150
    currentquest = None


def collectmoneyquest():
    global currentquest
    cmoney = 0 + money
    while cmoney < 35:
        cmoney += collectmoney()
        print(cmoney)
    print('megvetted a kardot, amiért eddig fáradoztál')
    getItem('weapon', marvanykard)
    currentquest = 'vadászat'


def sleepingdragon():
    global money
    print('el kéne eltatni a sárkányt, hogy később támadjon a városra. ')
    goto('dragonlayer')
    if player.eberseg > 90 and player.speed > 3 and player.agility > 5:
        print('Sikerült elaltatni a sárkányt, később fog a városra támadni.')
        print('a város 150 pénzel jutalmazott')
        money += 150
        universialquest.remove('elaltatni a sárkányt')
    else:
        print('Miközben megpróbáltad elaltatni a sárkányt az felkelt, megsebzett.')
        takeDamage(50)
    goto('city')


def stealFromDragon():
    global money
    print('Meg kéne lopni a sárkányt, így később fog a városra támadni.')
    goto('dragonlayer')
    if player.eberseg > 90 and player.speed > 4 and player.agility > 3:
        print('Sikerült meglopni a sárkányt,időt kell töltenie a vadászattal, később fog a városra támadni.')
        print('a város 100 pénzel jutalmazott')
        money += 100
        universialquest.remove('elaltatni a sárkányt')
    else:
        print('Miközben megpróbáltad elaltatni a sárkányt az felkelt, megsebzett.')
        takeDamage(50)
    goto('city')


def swordInStone():
    global money
    if player.strength < 5:
        print('Nem vagy elég erős ehhez. Lefáradtál a nagy próbálkozásban.')
        player.eberseg -= 25
        return 0
    print('nagy erőlködés után sikerült kihúzni a kardot.')
    if player.strength == 5:
        ido(0, 3)
        print('A karddal 3 órát szerencsétlenkedtél')
    if player.strength == 6:
        ido(0, 2)
        print('A karddal 2 órát szerencsétlenkedtél')
    if player.strength == 7:
        ido(0, 1)
        print('A karddal 1 órát szerencsétlenkedtél')
    if player.strength > 7:
        ido(30)
        print('A karddal 30 percet szerencsétlenkedtél')
    input('ENTER')
    print('1...eladod a kardot pénzért (65)')
    print('2...lemosod, és kiderül, hogy milyen erős')
    val = input('Melyiket választod? ')
    match val:
        case '1':
            money += 65
        case '2':
            rand = randint(1, 10)
            if rand in range(1, 3):
                print('Egy fakard volt')
                getItem('weapon', fakard)
            elif rand in range(3, 6):
                print('Egy márványkard volt')
                getItem('weapon', marvanykard)
            elif rand in range(6, 8):
                print('Egy vaskard volt')
                getItem('weapon', vaskard)
            elif rand in range(8, 10):
                print('egy obszidiánél volt')
                getItem('weapon', obszidianel)


def questboard():
    print('1... ', currentquest)
    i = 1
    for quest in universialquest:
        i += 1
        print(i, '...', quest)
    questindex = int(input('Melyiket szeretnéd megcsinálni? ')) - 2

    # while questindex > len(universialquest):
    # questindex = int(input('Melyiket szeretnéd megcsinálni? '))-2
    match questindex:
        case -1:
            sidequest()
        case 0:
            PALjatek()
        case 1:
            knightquest()
        case 2:
            swordInStone()
        case 3:
            sleepingdragon()
        case 4:
            stealFromDragon()


if __name__ == '__main__':
    player.strength = 5
    getItem(type='weapon', item=obszidianel)
    getItem(type='armor', item=obszidianpancel)
    getItem(type='shield', item=obszidianpajzs)
    while True:
        questboard()
