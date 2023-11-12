from definialas import *
from bosses import *
from minigames import *
del money
from variables import money

# from 
def mountain():
    val = input('szeretnél megküzdeni a sárkánnyal?')
    if val != 'nem':
        if isdragonalive:
            if not len(BOSSES):
                dragonfight()
            else:
                print('még vannak máshol is bossok, amiket nem ártana legyőzni.')
        else:
            print('Már meghalt a sárkány.')
    



def field():
    if not nowplace == 'field':
        goto('field')
    print('1...gyógynövényt szedni')
    print('2...Legyőzni a bosst')
    print('0...Vissza a várba')
    val = ' '
    while val not in map(str, range(0, 3)):
        val = input('Mit szeretnél csinálni')
    torles(money)
    match val:
        case '1':
            fieldMiniGame()
        case '2':
            fieldBossFight()
        case '0':
            goto('city')
            return 0
    field()
            
        

def forest():
    print(money)
    if not nowplace == 'forest':
        goto('forest')
    print('1..fát vágni')
    print('2...legyőzni a bosst')
    print('0...Vissza a várba')
    val = ' '
    while val not in map(str, range(0, 3)):
        val = input('Mit szeretnél csinálni')
    torles(money)
    match val:
        case '1':
            forestMiniGame()
        case '2':
            forestBossFight()
        case '0':
            goto('city')
            return 0
    forest()

def mine():
    if not nowplace == 'mine':
        goto('mine')
    print('1...válogatni')
    print('2...legyőzni a bosst')
    print('0...Vissza a várba')
    val = ' '
    while val not in map(str, range(0, 3)):
        val = input('Mit szeretnél csinálni')
    torles(money)
    match val:
        case '1':
            mineMiniGame()
        case '2':
            mineBossFight()
        case '0':
            goto('city')
            return 0
    mine()