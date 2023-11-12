from definialas import *
del money
from variables import money

ertek = 0


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
    input('ENTER')
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


if __name__ == '__main__':
    mineMiniGame()
