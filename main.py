import os, random, sys

piros = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 ]


def egeszszambekeres(szoveg) -> int:
    szam = ''
    while not szam.isdecimal():
        szam = input(szoveg)
    return int(szam)

def cont():
     input('Press ENTER to continue')

def torles():
    os.system('cls')

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
    szam = random.randint(0, 36)
    print(f'a sorsolt szám: {szam}')
    return szam 


def oddEven():
    egyenleg = 0
    print('1...Páros')
    print('2...Páratlan')
    print('0...Vissza')
    tipus = rangeEgeszszambekeres(szoveg = 'Melyiket válassza', min = 0, max = 2)
    torles()

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
    torles()
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
    torles()

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
    torles()
    return egyenleg

def tucat():
    egyenleg = 0
    print('1...1-12')
    print('2...13-24')
    print('3...25-36')
    print('0...Vissza')

    tipus = rangeEgeszszambekeres(szoveg = 'Melyiket válassza', min = 0, max = 3)
    torles()

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
    torles()
    return egyenleg
def oszlop():
    egyenleg = 0
    print('1...1. Oszlop')
    print('2...2. Oszlop')
    print('3...3. Oszlop')
    print('0...Vissza')

    tipus = rangeEgeszszambekeres(szoveg = 'Melyiket válassza', min = 0, max = 3)
    torles()

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
    torles()
    return egyenleg
    
def oneNumber():
    egyenleg = 0
    tipus = rangeEgeszszambekeres('Melyik számra szeretne tenni: ', min = 0, max = 36)
    torles()

    Tet = tet()
    nyeroszam = sorsolas()
    if nyeroszam != tipus:
        egyenleg -= Tet
        print('vesztettél')
    else:
        egyenleg += Tet * 35
        print('Nyertél')
    cont()
    torles()
    return egyenleg

def redBlack():
    egyenleg = 0
    print('1...Piros')
    print('2...Fekete')
    tipus = rangeEgeszszambekeres('Melyik szinre szeretne tenni: ', min = 0, max = 2)
    torles()

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
    torles()
    return egyenleg
def main():
    egyenleg = 10000
    while egyenleg > 0:
        tipus = menu()
        os.system('cls')
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
                sys.exit()
        egyenleg += valt
        print(f'Az egyenlege: {egyenleg}')



main()

