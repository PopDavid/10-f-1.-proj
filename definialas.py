from foszereplo import *
from items import *
from random import choice

Eweapon = True
EShield = False
Earmor = False
def displayerstat():
    print(f'Hp: {player.hp}, erő: {player.strength}, pajzs: {player.shield},sebesseg {player.speed}, éberség: {player.eberseg}, ügyesseg: {player.agility}')

def getItem():
    choiceItem = ''
    choiceList = choice(UCItems)
    choiceList = UCweapons
    getItemkey, getItemValue = choice(list(choiceList.items())) 
    del UCweapons[getItemkey] 
    Cweapon[getItemkey] = getItemValue
    
    match str(choiceList):
        case 'UCweapon':
            if Eweapon == False:
                pass
            else:
                for i in Cweapon:
                    print(i)
                while not choiceItem in Cweapon:
                    choiceItem = input('Melyiket szeretné? (a fegyver sebzése): ')
            value = Cweapon.get(choiceItem)
            player.weapon = value
        case 'UCarmor':
            if Eweapon == False:
                pass
            else:
                for i in Cweapon:
                    print(i)
                while not choiceItem in Cweapon:
                    choiceItem = input('Melyiket szeretné? (a fegyver sebzése): ')
            value = Cweapon.get(choiceItem)
            player.weapon = value
        
getItem()
print(player.weapon)



            


