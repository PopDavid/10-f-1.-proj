import time, sys, os
from random import randint
Eweapon = 0
EShield = 0
Earmor = 0
ertek = 0
piros = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 ]

def egeszszambekeres(szoveg) -> int:
    szam = ''
    while not szam.isdecimal():
        szam = input(szoveg)
    return int(szam)

def cont():
     input('Press ENTER to continue')

def rangeEgeszszambekeres(szoveg = ' ', min = 0, max = 10000):
    szam = ' '
    while True:
        szam = egeszszambekeres(szoveg)
        if szam < min or szam >max:
            pass
        else:
            break
    return int(szam)

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
    szam = randint(0, 36)
    print(f'a sorsolt szám: {szam}')
    return szam 

def oddEven():
    egyenleg = 0
    print('1...Páros')
    print('2...Páratlan')
    print('0...Vissza')
    tipus = rangeEgeszszambekeres(szoveg = 'Melyiket válassza', min = 0, max = 2)
    torles(money)

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
    torles(money)
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
    torles(money)

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
    torles(money)
    return egyenleg

def tucat():
    egyenleg = 0
    print('1...1-12')
    print('2...13-24')
    print('3...25-36')
    print('0...Vissza')

    tipus = rangeEgeszszambekeres(szoveg = 'Melyiket válassza', min = 0, max = 3)
    torles(money)

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
    torles(money)
    return egyenleg

def oszlop():
    egyenleg = 0
    print('1...1. Oszlop')
    print('2...2. Oszlop')
    print('3...3. Oszlop')
    print('0...Vissza')

    tipus = rangeEgeszszambekeres(szoveg = 'Melyiket válassza', min = 0, max = 3)
    torles(money)

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
    torles(money)
    return egyenleg
    
def oneNumber():
    egyenleg = 0
    tipus = rangeEgeszszambekeres('Melyik számra szeretne tenni: ', min = 0, max = 36)
    torles(money)

    Tet = tet()
    nyeroszam = sorsolas()
    if nyeroszam != tipus:
        egyenleg -= Tet
        print('vesztettél')
    else:
        egyenleg += Tet * 35
        print('Nyertél')
    cont()
    torles(money)
    return egyenleg

def redBlack():
    egyenleg = 0
    print('1...Piros')
    print('2...Fekete')
    tipus = rangeEgeszszambekeres('Melyik szinre szeretne tenni: ', min = 0, max = 2)
    torles(money)

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
    torles(money)
    return egyenleg

def casino():
    global money
    torles(money)
    if money > 0:
        tipus = menu()
        torles(money)
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
                torles(money)
                castle()
        money += valt
    casino()

class characters: #sablon

    def __init__(self) -> None:
        self.hp = 100
        self.strength = 1
        self.agility = 1
        self.speed = 1
        self.weapon = 0
        self.shield = 0
        self.damage = self.strength * self.weapon
        self.rep = 0

class Enemies:
    def __init__(self, name, hp, strength, speed, shield) -> None:
        self.name = name
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.shield = shield
    def __str__(self) -> str:
        return self.name
    
class weapon:
    def __init__(self, name, damage, price) -> None:
        self.damage = damage
        self.price = price
        self.name = name

    def __str__(self):
        return self.name

class shield:
    def __init__(self, name, shield, price) -> None:
        self.shield = shield
        self.price = price
        self.name = name

    def __str__(self):
        return self.name

class armor:
    def __init__(self, name,shield, price) -> None:
        self.shield = shield
        self.price = price
        self.name = name

    def __str__(self):
        return self.name

def mountain():
    global isdragonalive
    if nowplace != 'mountain':
        goto('mountain')
    val = input('szeretnél megküzdeni a sárkánnyal?')
    if val != 'nem':
        if isdragonalive:
            if not len(BOSSES):
                fight(dragon)
                isdragonalive = False
            else:
                print('még vannak máshol is bossok, amiket nem ártana legyőzni.')
        else:
            print('Már meghalt a sárkány.')
    print('Vissza a várba ENTER-rel')
    
def field():
    torles(money)
    if not nowplace == 'field':
        goto('field')
    print('1...gyógynövényt szedni')
    if 'fieldboss' in BOSSES:
        print('2...legyőzni a bosst')
    print('0...Vissza a várba')
    val = ' '
    if 'fieldboss' in BOSSES:
        while val not in map(str, range(0, 3)):
            val = input('Mit szeretnél csinálni: ')
    else:
        while val not in map(str, range(0, 2)):
            val = input('Mit szeretnél csinálni: ')
    torles(money)
    match val:
        case '1':
            fieldMiniGame()
        case '2':
            fight(fieldboss)
            BOSSES.remove('fieldboss')
        case '0':
            goto('city')
            return 0
    field()
            
def forest():
    torles(money)
    if not nowplace == 'forest':
        goto('forest')
    print('1...fát vágni')
    if 'forestboss' in BOSSES:
        print('2...legyőzni a bosst')
    if not isdragonalive:
        print('2...Elhagyni a környéket')
    print('0...Vissza a várba')
    val = ' '
    if 'forestboss' in BOSSES or not isdragonalive:
        while val not in map(str, range(0, 3)):
            val = input('Mit szeretnél csinálni: ')
    else:
        while val not in map(str, range(0, 2)):
            val = input('Mit szeretnél csinálni: ')
    torles(money)
    match val:
        case '1':
            forestMiniGame()
        case '2':
            if 'forestboss' in BOSSES:
                fight(forestboss)
                BOSSES.remove('forestboss')
            else:
                print('elhagytad a környéket')
                print('NYERTÉL')
                print('━━━━━━━━━━━━━━━━━━━━━━')
                print('VÉGE A JÁTÉKNAK.')
                print('━━━━━━━━━━━━━━━━━━━━━━')
                sys.exit()


        case '0':
            goto('city')
            return 0
    forest()

def collectmoney():
    global money
    torles(money)
    print('Még kéne egy kis pénz')
    print('1...lopni')
    print('2...kéregetni')
    print('3...dolgozni')
    val = input('Hogyam szeretnél pénzt szerezni')
    while val not in map(str, range(1, 4)):
        val = input('Hogyam szeretnél pénzt szerezni')
    match val:
        case '1':
            cmoney = steal()
        case '2':
            cmoney = begging()
        case '3':
            cmoney = work()
    money += cmoney
    input('Vissza a várba ENTER-rel')
    torles(money)
    castle()

def steal():
    global money
    happening = randint(1, 100)
    if happening in range(1, 6):
        print('megloptál egy haljéktalant, nem vett észre.')
        money += 20
        ido(15)
        return 20
    elif happening in range(6, 21):
        print('megloptál egy haljéktalant, felismert. Csökkent a megítélésed.')
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
            input('Tovább ENTER-rel')
            torles(money)
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
    global Palvolt, pal, PAL, money
    torles(money)
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
        money += rew
        Palvolt = True
    else:
        Slowtype(f'özvegy: Nagyon jól teljesítettél.\nözvegy pontosan {score} szót mondtál helyesen')
    input('Vissza a várba ENTER-rel')

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

def hunting():
    global currentquest, money
    esely = 4 - player.agility
    if esely < 1:
        esely = 1
    print('a vadászok előrementek a mezőre, neked is oda kéne menned.')
    input('Indulás ENTER-rel')
    torles(money)
    goto('field')
    Slowtype('vadászok: a cél 5 vadat elejteni.')
    input('ENTER-rel kezdődik a vadászat')
    vadak = 0
    while vadak != 5:
        torles(money)
        while randint(1, 4) != 1:
            print('vársz')
            ido(5)
            time.sleep(1.5)
            ido(10)
        torles(money)
        print('meglátsz egy prédát')
        time.sleep(2)
        print('rácélzol')
        time.sleep(2)
        print('lösz')
        time.sleep(2)
        if randint(1, esely-1) == 1:
            vadak += 1
            print(f'Eltaláltad, már csak {5-vadak} prédát kell meglőnöd.')
        else:
            print(f'Nem találtad el, még {5-vadak} prédát kell meglőnöd.')
        input('Következő keresése ENTER-rel')
    print('eladtad a vadat a vadászoknak, kaptál érte 50 pénzt')
    money += 50
    currentquest = 'gyűjtőgetés'
    print('a vadászok visszakísértek a városba')
    input('indulás ENTER-rel')

def collecting():
    global currentquest, money
    print('A király fia megint beteg.\ntalán ha szednék neki egy kis gyógyfüzet a mezőről kapnék egy kis jutalmat.')
    input('Indulás a mezőrr ENTER-rel.')
    torles(money)
    if nowplace != 'field':
        goto('field')
    torles(money)
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
            input('Következő keresése ENTER-rel')
            torles(money)
        else:
            need = 0
            print(f'találtál {find} növényt ami neked kell. Megvan amiért jöttél')
            input('Tovább ENTER-rel')
            torles(money)
            print('Vissza kéne menni a városba.')
            goto('city')
            print('Leadtad a gyógynövényeket, kaptál érte 50 pénzt')
            money += 50
            currentquest = 'ogrevadászat'


def ogrehunt():
    global currentquest, money
    torles(money)
    print('A hegység el van árasztva ogrével.\noda kéne menni, egy kicsit szétcsapni közöttük.')
    goto('mountain')
    print('mások is vannak itt, besegítek nekik')
    needKillogre = 3
    while needKillogre != 1:
        fight(ogre)
        needKillogre -= 1
        print(f'ez nehéz küzdelem volt. már csak {needKillogre} ogrét kell megöljek')
        input('ENTER-rel megküzdés a következővel')
        torles(money)
    fight(ogre)
    print('Ezek nehéz küldelmek voltak. A helybéliektől kaptál 75 pénzt a segítségért.')
    money += 75
    input('Vissza kéne indulni a várba.')
    currentquest = 'király kísérés'

def kingfollow():
    global money, currentquest, nowplace
    torles(money)
    print('a király el szeretne látogatni a bányába. Őrséget keres maga mellé.')
    print('Jó pénzt ígér ha én is segítek megvédelni.')
    print('jelentkeztél, elindultatok')
    for _ in range(randint(3, 5)):
        print('Mentek')
        time.sleep(1)
    time.sleep(2)
    torles(money)
    print('az úton egy csapat jól felfegyverkezet bandita támadt rátok.')
    needKillBandit = 5
    while needKillBandit != 1:
        fight(bandit)
        needKillBandit -= 1
        print(f'ez nehéz küzdelem volt. Már csak {needKillBandit} banditát kell megöljek')
        input('ENTER-rel megküzdés a következővel')
        torles(money)
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
        input('ENTER-rel megküzdés a következővel.')
        torles(money)
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
    nowplace = 'mine'
    mine()
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
    if player.speed > 3 and player.agility > 5:
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
    if player.speed > 4 and player.agility > 3:
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
        input('Vissza a várba ENTER-rel')
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
    input('Tovább ENTER-rel')
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
    torles(money)
    print('1...', currentquest)
    i = 1
    for quest in universialquest:
        i += 1
        print(f'{i}...{quest}')
    print('0...Vissza a várba')
    val = ''
    while val not in map(str, range(0, i+1)):
        val = input('Melyiket szeretnéd megcsinálni? ')
    questindex = int(val)-2


    match questindex:
        case -1:
            sidequest()
        case 0:
            PALjatek()

        case 1:
            swordInStone()
        case 2:
            sleepingdragon()
        case 3:
            stealFromDragon()
        case 0:
            pass

def collectingFirst():
    global currentquest, money
    Slowtype('[SZOLGA]: A király fia megbetegedett! Mai feladatod, hogy gyógynövényeket szedj neki a mezőn!')
    time.sleep(1)
    Slowtype('(Gondolat): Remélem ezért jutalomban fogok részesülni!')
    time.sleep(2)
    nowplace = 'field'
    print('Megérkeztél a mezőre.')
    input('Keresgéléshez nyomj ENTER-t')
    
    torles(money)
    esely = 5  - player.speed
    if esely < 1:
       esely = 1
    need = 20
    while need != 0:
        while randint(1, esely) != 1:
            print('Gyógynövény után kutatsz.')
            time.sleep(1.5)
        find = randint(1, 3)
        if need - find > 0:
            need -= find
            print(f'Találtál {find} növényt, melyre szükséged is van. Már csak {need} növényt kell találnod.')
            input('További keresése ENTER-rel')
            torles(money)
        else:
            need = 0
            Slowtype(f'[{foszereplo}]Megtaláltam a {find} növényt. Megvan amiért jöttem!')
            time.sleep(1)
            nowplace = 'city'
            print('Leadtad a gyógynövényeket, 50 pénz üti markod.')
            input('\nVisszatérés a városba az ENTER megnyomásával >>')
            money += 50
            torles(money)

def bev():
    global nowplace, foszereplo, money
    
    print('━━━━━━━━━━━━━━━━━━━━━━')
    print('Medieval City Game')
    print('━━━━━━━━━━━━━━━━━━━━━━')
    time.sleep(3)
    Slowtype('\nEz a játék a középkorba repíti vissza a játékost,\nki a főszereplő útját bejárva próbál harcossá, \nvalamint a város hősévé válni.')
    input('\nTovábbhaladás az ENTER megnyomásával >>')
    
    torles(money)
    time.sleep(3)
    os.system('cls')
    time.sleep(2)
    
    Slowtype(f'[{foszereplo}]: Végre elérkezett a nap!')
    time.sleep(2)
    Slowtype(f'[{foszereplo}]: Eljött az én időm!')
    time.sleep(2)
    Slowtype('[???]: Jó reggelt!')
    time.sleep(1.5)
    Slowtype('ZzZzZzZzZzZz')
    time.sleep(1.5)
    Slowtype(f'[{foszereplo}]: Megtöröm a gonosz sárkány uralmát!')
    time.sleep(2)
    Slowtype('[???]: Ébresztő!')
    time.sleep(1.5)
    Slowtype('ZzZzZzZzZzZz')
    time.sleep(1)
    input('\nFelébredés az ENTER megnyomásával >>')
    os.system('cls')

    time.sleep(1)
    Slowtype('[SZOLGA]: Jó reggelt hétalvók, ideje felkelni.')
    time.sleep(2)
    Slowtype('[SZOLGA]: Ki nem dolgozik elég keményen mehet az utcára aludni! Ez a király üzenete!')
    time.sleep(1.5)
    Slowtype('[SZOLGA]: Most pedig irány munkára!')
    time.sleep(1)
    input('\nTovábbhaladás az ENTER megnyomásával >>')
    torles(money)

    nowplace = 'field'

    collectingFirst()




    print('*dobpergés*')
    time.sleep(1.5)
    Slowtype('[DOBOS]: Figyelem, figyelem! Közhírré tétetik a király szava.')
    time.sleep(1)
    print('*dobpergés*')
    time.sleep(1)
    Slowtype('[DOBOS]: Városunkat ismét a sárkány visszatérése fenyegeti!')
    time.sleep(2)
    Slowtype('[DOBOS]: Ki van oly merész, hogy városunk védelmére kel, s megküzd a sárkánnyal, pénzzel gondja soha nem lesz!')
    time.sleep(3)
    Slowtype(f'[{foszereplo} gondolatai]: Mióta erről álmodok! Én lennék a város hőse!')
    time.sleep(2)
    Slowtype('[DOBOS]: Ki vállalkozni szeretne e nemes feladatra a király elé járuljék!')
    
    input('\nKirály elé járulás az ENTER megnyomásával >>')
    
    torles(money)

    print('Sikeresen megérkeztél várba.')



    Slowtype(f'[Király]: Őrök! Hívják be a következő látogatót!')
    time.sleep(3)
    Slowtype(f'[Őrök]: Jöjjön be a következő!')
    time.sleep(1)

    print('\nHogy köszöntöd a királyt?')
    print('━━━━━━━━━━━━━━━━━━━━━━')
    print('1...Felséges királyom, életem-halálom kezedbe ajánlom!')
    print('2...Hallod-e, király?')
    print('3...[Nem köszöntöd]')
    print('━━━━━━━━━━━━━━━━━━━━━━')
    
    val = ''
    while val != str(1 or 2 or 3):
        val = input('Választásod: ')
        match val:
            case '1':
                Slowtype(f'Felséges királyom, életem-halálom kezedbe ajánlom! Vállalkoznék a sárkány legyőzésére!')
                repchange(2)
                time.sleep(1)
                print('A királlyal mindig tisztelettel beszélj!')
                time.sleep(1)
            
            case '2':
                Slowtype(f'[{foszereplo}]: Hallod-e király? Vállalkoznék a sárkány legyőzésére!')
                time.sleep(1)
                Slowtype(f'[Őr]: A király nem ilyen hangnemet érdemel!')
                time.sleep(1)
                print(f'Megütött az őr, ezzel 2-t sebezve.')
                takeDamage(2)
                repchange(-10)
                time.sleep(1)
                print('A királlyal mindig tisztelettel beszélj!')
                time.sleep(1)
            
            case '3':
                Slowtype(f'[{foszereplo}]: Vállalkoznék a sárkány legyőzésére!')
                time.sleep(1)
                Slowtype(f'[Őr]: Kihez beszélsz?')
                time.sleep(1)
                Slowtype(f'[{foszereplo}]: Őfelségéhez.')
                time.sleep(1)
                Slowtype(f'[Őr]: Akkor köszöntsd a királyt!')
                time.sleep(1)

                print('\nHogy köszöntöd a királyt?')
                print('━━━━━━━━━━━━━━━━━━━━━━')
                print('1...Felséges királyom, életem-halálom kezedbe ajánlom!')
                print('2...Hallod-e, király?')
                print('━━━━━━━━━━━━━━━━━━━━━━')

                val = ''
                while val != str(1 or 2):
                    val = input('Választásod: ')

                    match val:
                        case '1':
                            Slowtype(f'Felséges királyom, életem-halálom kezedbe ajánlom! Vállalkoznék a sárkány legyőzésére!')
                            repchange(2)
                            time.sleep(1)
                            print('A királlyal mindig tisztelettel beszélj!')
                            time.sleep(1)
                        
                        case '2':
                            Slowtype(f'[{foszereplo}]: Hallod-e király? Vállalkoznék a sárkány legyőzésére!')
                            time.sleep(1)
                            Slowtype(f'[Őr]: A király nem ilyen hangnemet érdemel!')
                            time.sleep(1)
                            print(f'Megütött az őr, ezzel 2-t sebezve.')
                            takeDamage(2)
                            repchange(-10)
                            time.sleep(1)
                            print('A királlyal mindig tisztelettel beszélj!')
                            time.sleep(1)

                        case _:
                            time.sleep(1)
                            Slowtype(f'[Őr]: Mit hablatyolsz? Beszélj érthetően!')
                            time.sleep(1)

            case _:
                time.sleep(1)
                Slowtype(f'[Őr]: Mit hablatyolsz? Beszélj érthetően!')
                time.sleep(1)
                
    Slowtype('[Király]: Hogy hívnak, bátor kalandor?')
    time.sleep(1)
    foszereplo = 'Játékos'
    while foszereplo in  ['Játékos' ,  '' ,  ' ' ,  '   ' ,  '    ' ,  '     ' ,  '      ']:
        foszereplo = Slowtype(input(f'[{foszereplo}]: Királyom, az én becses nevem nem más, mint '))
        if foszereplo in  ['Játékos' ,  '' ,  ' ' ,  '   ' ,  '    ' ,  '     ' ,  '      ']:
            Slowtype(f'[Király]: Milyen tökkelütöttnek nézel, hogy elhiggyem, téged valóban így hívnak?')
            repchange(-1)
            time.sleep(1)

    time.sleep(1)
    Slowtype(f'[Király]: {foszereplo}, áldásomat adom küldetésedre. Járj szerencsével!')
    time.sleep(1)
    Slowtype('[Király]: Kapsz 100 pénzt, okosan gazdálkodj vele!')
    time.sleep(1)
    Slowtype('[Király]: Ha meghalsz, családod a 10-szeresét fizeti vissza nekem!')
    money += 100

    input('\nTerem elhagyása az ENTER megnyomásával >>')
    torles(money)
    nowplace = 'city'
    castle()

if 'stat ' == 'stat ':
    treasuryMap = False
    key = False
    foszereplo = 'JÁTÉKOS'
    foszereplo = 'Játékos'
    player = characters()

    fakard = weapon('fakard (1)', 1, 0)
    marvanykard = weapon(name='márványkard (3)', damage=3, price=35)
    vaskard = weapon(name='vaskard (6)', damage=6, price=55)
    obszidianel = weapon(name='obszidiánél (11)', damage=11, price=110)

    fapancel = armor(name='fapáncél (1)', shield=1, price=55)
    marvanypancel = armor(name='marvanypáncél (2)', shield=2, price=105)
    vaspancel = armor(name='vaspáncél (5)', shield=5, price=210)
    obszidianpancel = armor(name='obszidianpáncél (11)', shield=11, price=320)

    fapajzs = shield(name='fapáncél (1)', shield=1, price=25)
    marvanypajzs = shield(name='marvanypáncél (2)', shield=2, price=55)
    vaspajzs = shield(name='vaspáncél (5)', shield=5, price=105)
    obszidianpajzs = shield(name='obszidiánpajzs (11)', shield=11, price=210)

    goblin = Enemies(name='goblin', hp=5, strength=4, speed=2, shield=5)
    ogre = Enemies(name='ogre', hp=15, strength=7, speed=4, shield=10)
    bandit = Enemies(name='bandit', hp=20, strength=15, speed=5, shield=12)
    cerberus = Enemies(name='cerberus', hp=30, strength=16, speed=3, shield=15)
    vampir = Enemies(name='vampir', hp=50, strength=14, speed=2, shield=20)

    mineboss = Enemies(name='Bánya boss', hp=50, strength=30, speed=4, shield=35)
    forestboss = Enemies(name='erdő boss', hp=100, strength=35, speed=2, shield=45)
    fieldboss = Enemies(name='mező boss', hp=75, strength=37, speed=6, shield=40)
    dragon = Enemies(name='sárkány', hp=250, strength=45, speed=10, shield=60)

    isdragonalive = True
    money = 0
    nowplace = 'city'
    hour = 6
    minute = 0
    day = 0
    Palvolt = False
    lo = False

    WEAPON = [
        fakard,
        marvanykard,
        vaskard,
        obszidianel
    ]

    ARMOR = [
        fapancel,
        marvanypancel,
        vaspancel,
        obszidianpancel
    ]

    SHIELD = [
        fapajzs,
        marvanypajzs,
        vaspajzs,
        obszidianpajzs,
    ]

    Cshield = [

    ]

    Cweapon = [
        fakard
    ]

    Carmor = [

    ]

    BOSSES = [
        'mineboss',
        'forestboss',
        'fieldboss',
    ]

    QUESTS = [
        'pénzgyűjtés fegyverre',
        'vadászat',
        'gyűjtőgetés',
        'ogrevadászat',
        'király kísérés'
    ]

    universialquest = [
        'özvegy néni férje',
        'kard a kőben',
        'elaltatni a sárkányt',
        'meglopni a sárkányt'
    ]

    Dquest = [

    ]

    PAL = [
        'opál',
        'kapál',
        'kalimpál',
        'kalapál',
        'gyepál',
        'pálca',
        'pálinka',
        'pálma',
        'pálmafa',
        'pálfordulás',
        'pumpál',
        'nepál',
        'bepáll',
        'pipál',
        'kupál',
        'bekrepál',
        'strapál',
        'rúgkapál',
        'kupál',
        'szlopál'
    ]

    pal = [
        'opál',
        'kapál',
        'kalimpál',
        'kalapál',
        'gyepál',
        'pálca',
        'pálinka',
        'pálma',
        'pálmafa',
        'pálfordulás',
        'pumpál',
        'nepál',
        'bepáll',
        'pipál',
        'kupál',
        'bekrepál',
        'strapál',
        'rúgkapál',
        'kupál',
        'szlopál'
    ]

    PLACE = [
        'mine',
        'mountain'
        'forest',
        'kazamata',
        'dragonlayel',
        'field',
        'city'
    ]

    aranyBoundle = [
        'szén',
        'vas',
        'szén',
        'vas',
        'arany'
    ]

    vasBoundle = [
        'arany',
        'szén',
        'arany',
        'arany',
        'vas'
    ]

    szenBoundle = [
        'szén',
        'vas',
        'szén',
        'vas',
        'arany'
    ]

    currentquest = QUESTS[1]

def mine():
    torles(money)
    if not nowplace == 'mine':
        goto('mine')
    print('1...válogatni')
    if 'mineboss' in BOSSES:
        print('2...legyőzni a bosst')
    print('0...Vissza a várba')
    val = ' '
    if 'mineboss' in BOSSES:
        while val not in map(str, range(0, 3)):
            val = input('Mit szeretnél csinálni: ')
    else:
        while val not in map(str, range(0, 2)):
            val = input('Mit szeretnél csinálni: ')
    torles(money)
    match val:
        case '1':
            mineMiniGame()
        case '2':
            fight(mineboss)
            BOSSES.remove('mineboss')
        case '0':
            goto('city')
            return 0
    mine()

def forestMiniGame():
    score = 0
    global money
    fa = 0

    print('elkezdtél fát vágni')
    startTime = time.time()
    while time.time() - startTime < 10:
        input('hogy folytasd nyomj ENTER-t')
        score += 1
        if score % 10 == 0:
            fa += 1
            os.system('cls')
            print(f'sikerült kivágni egy fát, már {fa} fát vágtál ki.')
    print(f'a fákért {fa * 5} pénzt kaptál')
    money += fa * 5
    val = ''
    while val == '':
        val = input('írj bármit, csak ne semmit')

def fieldMiniGame():
    global ertek, money
    print('Válaszd ki a növény közül a jót.')
    print('gyömbér kell')
    print('macskafű kell')
    print('pitypang nem kell')
    input('Játék indítása ENTER-rel')
    os.system('cls')
    startTime = time.time()
    while time.time() - startTime < 30:
        rand = randint(1, 3)
        if rand == 3:
            if randint(1, 2) == 1:
                print('pitypang')
            else:
                print('gaznövény')
            if input() == 'kell':
                ertek -= 3
        else:
            if randint(1, 2) == 1:
                print('gyömbér')
            else:
                print('macskafű')
            if input() == 'kell':
                ertek += 1
        os.system('cls')
    print(f'sikerült {ertek} értékű növény összeszedned, kapsz {ertek *3} pénzt')
    money += ertek * 3
    val = ''
    while val == '':
        val = input('írj bármit, csak ne semmit')

def mineMiniGame():
    global aranyBoundle, vasBoundle, szenBoundle
    print('Válogasd szét az aranyat, a szenet, és a vasat')
    kesz = False
    while not kesz:
        os.system('cls')
        kesz = True
        print('\n\n')
        print('aranycsomag:', end='')
        for i in aranyBoundle:
            print(i, end=' ')
        print('\n')
        print('vascsomag:', end='')
        for i in vasBoundle:
            print(i, end=' ')
        print('\n')
        print('széncsomag:', end='')
        for i in szenBoundle:
            print(i, end=' ')
        print('\n')
        eb, ee, mb, me = 0, 0, 0, 0
        while eb not in map(str, range(1, 4)):
            eb = input('Melyikből')
        while ee not in map(str, range(1, 6)):
            ee = input('Melyik elem')
        while mb not in map(str, range(1, 4)):
            mb = input('Melyikből')
        while me not in map(str, range(1, 6)):
            me = input('Melyik elem')
        ee, me = int(ee), int(me)
        match eb:
            case '1':
                boundle1 = aranyBoundle
            case '2':
                boundle1 = vasBoundle
            case '3':
                boundle1 = szenBoundle
        match mb:
            case '1':
                boundle2 = aranyBoundle
            case '2':
                boundle2 = vasBoundle
            case '3':
                boundle2 = szenBoundle
        item1 = boundle1[ee - 1]
        item2 = boundle2[me - 1]
        boundle1.remove(item1)
        boundle2.append(item1)
        boundle2.remove(item2)
        boundle1.append(item2)
        if not 'szen' in aranyBoundle and not 'vas' in aranyBoundle:
            pass
        else:
            kesz = False
        if not 'szen' in vasBoundle and not 'arany' in vasBoundle:
            pass
        else:
            kesz = False
        if not 'arany' in szenBoundle and not 'vas' in szenBoundle:
            pass
        else:
            kesz = False
    os.system('cls')
    print('Fáradságodért kapsz 50 pénzt.')
    val = ''
    while val == '':
        val = input('írj bármit, csak ne semmit')
def displayerstat(money):
    print('━━━━━━━━━━━━━━━━━━━━━━')
    print(f'HP: {player.hp}, Védésém: {player.shield}, Fegyver: {player.weapon} Erő: {player.strength}\nSebesség: {player.speed}, Megítélés: {player.rep}, Ügyesseg: {player.agility}')
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
        os.system('cls')
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
                print('már megvetted')
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
                val = ' '
                while val not in map(str, range(1, len(Cweapon)+1)):
                    val = input('Melyiket szeretnéd Megvenni? (a fegyver sebzése): ')
                itemindex = int(val) - 1
                Eweapon = Cweapon[itemindex].damage
                player.weapon = Eweapon

        case 'armor':
            if item in Carmor:
                money += item.price
                print('már megvetted.')
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
                val = ' '
                while val not in map(str, range(1, len(Carmor) +1)):
                    val = input('Melyiket szeretnéd Megvenni? (a páncél védelme): ')
                itemindex = int(val) - 1                
                Earmor = Carmor[itemindex].shield
                player.shield = Earmor + EShield
        case 'shield':
            if item in Cshield:
                money += item.price
                print('már megvetted')
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
                val = ' '
                while val not in map(str, range(1, len(Cshield) +1)):
                    val = input('Melyiket szeretnéd Megvenni? (a páncél védelme): ')
                itemindex = int(val) - 1
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
        else:
            print('A vadonban aludtál.')
        hour = 6
        minute = 0

def repchange(amount):
    player.rep += amount
    if amount < 0:
        print(f'Megbecsültséged ennyivel csökkent: {-amount}.')
    if amount > 0:
        print(f'Megbecsültséged ennyivel nőtt: {amount}.')
    if player.rep < -50:
        print('Annyire utálnak, hogy bebörtönöztek')
        time.sleep(2)
        print('Innen nincs kiút')
        time.sleep(2)
        print('Legközelebb legyél jóban velük.')
        time.sleep(2)
        print('\n')
        print('━━━━━━━━━━━━━━━━━━━━━━')
        print('VÉGE A JÁTÉKNAK.')
        print('━━━━━━━━━━━━━━━━━━━━━━')
        sys.exit()

def fight(enemy):
    global money, goblin, ogre, bandit, cerberus, vampir
    while enemy.hp >= 0:
        print(f'ellenfeled hp: {enemy.hp}, sebessége: {enemy.speed}, ereje: {enemy.strength}, védelme: {enemy.shield}')
        if player.speed <= enemy.speed:
            print('Ő a gyorsabb ő támad először')
            enemydamage = enemy.strength - player.shield
            if enemydamage < 0:
                enemydamage = 0
            print(f'az ellenfeled {enemydamage}-et  sebzett.')
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

            if enemydamage < 0:
                enemydamage = 0
            playerdamage = player.strength * player.weapon - enemy.shield + randint(-2, 2)

            print(f'te {playerdamage} -et sebeztél')
            enemy.hp -= playerdamage
            if enemy.hp <= 0:
                break
            print(f'az ellenfeled {enemydamage}-et sebzett.')
            takeDamage(enemydamage)
            input('ENTER-rel tovább')
            torles(money)
    ido(5)
    foundmoney = 0
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
            print('nincs pénz a cerberusoknál')
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
        case 'dragonlayer':
            distance = 80
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
                case 'dragonlayer':
                    distance = 80
    while distance >= 0:
        if lo:
            distance -= 15
            print('lovagolsz')
            time.sleep(1)

        else:
            distance -= 5
            print('gyalogolsz')
            time.sleep(1)
        if randint(1, 5) == 1:
            
            if hour >= 18: 
                rand = randint(1, 10)
            else: 
                rand = randint(1, 9)
            
            if rand in range(1, 5):
                print('Egy goblin állja utadat.')
                input('A küzdelem megkezdéséhez nyomj ENTER-t')
                torles(money)

                fight(goblin)

            if rand in range(5, 8):
                print('Egy ogre állja utadat.')
                input('A küzdelem megkezdéséhez nyomj ENTER-t')
                torles(money)

                fight(ogre)

            if rand in range(8, 10):
                print('Egy bandita állja utadat.')
                input('A küzdelem megkezdéséhez nyomj ENTER-t')
                torles(money)

                fight(bandit)

            if rand == 10:
                print('Egy vámpír állja utadat.')
                input('A küzdelem megkezdéséhez nyomj ENTER-t')
                torles(money)

                fight(vampir)

        ido(30)
    nowplace = place
    print(f'Sikeresen megérkeztél ide: {nowplace}')
    input('ENTER-rel belépsz')
    torles(money)

def shop():
    global money
    list = 0
    torles(money)
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
            val = input('Melyiket szeretnéd Megvenni? (a fegyver sebzése): ')
            while val not in map(str, range(1, 5)):
                val = input('Melyiket szeretnéd megvenni? (a fegyver sebzése): ')
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
            val = input('Melyiket szeretnéd Megvenni? (a fegyver sebzése): ')

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
    print('0...Semmit')
    valasz = input('Mit szeretnél csinálni? ')
    if valasz != '1':
        input('Vissza a Várba ENTER-rel')
    else:
        healprice = int((100 - player.hp) * 1.5)
        if healprice <= money:
            player.hp = 100
            money -= healprice
        else:
            print('nincs elég pénzed')
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
    while choice not in map(str,range(0, 12)):
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
        case '11':
            collectmoney()
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
            print('A lovagi torna a sárkány legyőzése után kerül megrendezésre')
        elif input('Szeretnél részt venni a lovagi tornán? '):
            print('Még nincs elegendő versenyző a torna megkezdésére.')
        else:
            print('Majd gyere vissza ha van kedved')
    else:
        print('Ló nélkül nehéz lesz LÓvagi tornán részt venni')
    input('Vissza a városba ENTER-rel')
    torles(money)
    castle()            
def hostel():
    torles(money)
    print('Munka van nem a pihenés ideje')
    input('Vissza a várba ENTER-rel')
    torles(money)
    castle()
def treasury():
    torles(money)
    if isdragonalive:
        print('Bárcsak sok pénzem lenne itt.')
    else:
        robTheTreasury()
    input('Vissza a várba ENTER-rel')
    torles(money)
    castle()
def robTheTreasury():
    global treasuryMap, key, money
    i = 1
    if not treasuryMap:
        print(f'{i}...Megszerezni a térképet')
        i += 1
    if not key:
        print(f'{i}...Megszerezni a kulcsot')
        i += 1
    print(f'{i}...kirabolni a bankot a mostani cuccaimmal')
    val = input('Mit szeretnél csinálni: ')
    while val not in map(str, range(1, i+1)):
        val = input('Mit szeretnél csinálni: ')
    torles(money)
    match val: 
        case '1':
            if treasuryMap and key: 
                robbing()
            elif treasuryMap :
                if randint(player.speed, 10)  == 10:
                    print('sikeresen megszerezted a kulcsokat.')
                    key = True
                else:
                    print('megpróbáltad megszerezni a kulcsokat, nem sikerült.')
                    repchange(-10)
            else:
                if randint(player.agility, 10)  == 10:
                    print('sikeresen megszerezted a bank térképét.')
                    treasuryMap = True
                else:
                    print('megpróbáltad megszerezni a bank térképét, nem sikerült.')
                    repchange(-10)
            input('Tovább ENTER-rel')
            torles(money)
            robTheTreasury()
        case '2':
            if key:
                robbing()
            elif randint(player.agility, 10)  == 10:
                print('sikeresen megszerezted a bank kulcsát.')
                treasuryMap = True
            else:
                print('megpróbáltad megszerezni a bank kulcsát, nem sikerült.')
                repchange(-10)
        case '3':
            robbing()
            torles(money)
    robTheTreasury()
def robbing():
    global treasuryMap, key, money
    help = treasuryMap + key
    if randint(help*2, 5):
        print('sikeren  kiraboltad a bankot, szereztél 10000 pénzt')
        money += 10000
    else:
        print('megpróbáltad kirabolni a bankot, nem sikerült.')
        repchange(-20)
    input('Vissza a városba ENTER-rel')
    torles(money)
    castle()
def prison():
    torles(money)
    print('Bizz bennem, nem szeretnél ide jutni')
    input('Vissza a várba ENTER-rel')
    torles(money)
    castle()
if __name__ == '__main__':
    # bev()
    money = 1500
    torles(money)
    castle()