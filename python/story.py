import time
import os
from variables import *
from definialas import *
from quest import *
from main import *
from classes import *
from city import *

foszereplo = 'JÁTÉKOS'

def bev():
    # print('━━━━━━━━━━━━━━━━━━━━━━')
    # print('Játék címe')
    # print('━━━━━━━━━━━━━━━━━━━━━━')
    # Slowtype('\nEz a játék a középkorba repíti vissza a játékost,\nki a főszereplő útját bejárva próbál harcossá, \nvalamint a város hősévé válni.')
    # time.sleep(5)
    # os.system('cls')
    # time.sleep(2)

    # Slowtype(f'[{foszereplo}]: Végre elérkezett a nap!')

    # time.sleep(2)
    # Slowtype(f'[{foszereplo}]: Eljött az én időm!')
    # time.sleep(2)
    # Slowtype('[???]: Jó reggelt!')
    # time.sleep(1.5)
    # Slowtype('ZzZzZzZzZzZz')
    # time.sleep(1.5)
    # Slowtype(f'[{foszereplo}]: Megtöröm a gonosz sárkány uralmát!')
    # time.sleep(2)
    # Slowtype('[???]: Ébresztő!')
    # time.sleep(1.5)
    # Slowtype('ZzZzZzZzZzZz')
    # time.sleep(1)
    # input('\nFelébredés az ENTER megnyomásával >>')
    # os.system('cls')

    # time.sleep(1)
    # Slowtype('[SZOLGA]: Jó reggelt hétalvók, ideje felkelni.')
    # time.sleep(2)
    # Slowtype('[SZOLGA]: Ki nem dolgozik elég keményen mehet az utcára aludni! Ez a király üzenete!')
    # time.sleep(1.5)
    # Slowtype('[SZOLGA]: Most pedig irány munkára!')
    # time.sleep(1)
    # input('\nTovábbhaladás az ENTER megnyomásával >>')
    torles()

    nowplace = 'field'

    collectingFirst()

    kikialtas()

def kikialtas():
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
    
    torles()

    print('Sikeresen megérkeztél várba.')

    Slowtype(f'[KIRÁLY]: Őrök! Hívják be a következő látogatót!')
    Slowtype(f'[ŐRÖK]: Kérem jöjjön be a következő!')


    print('\nHogy köszöntöd a királyt?')
    print('━━━━━━━━━━━━━━━━━━━━━━')
    print('1...Felséges királyom, életem-halálom kezedbe ajánlom!')
    print('2...Hallod-e, király?')
    print('3...[Nem köszöntöd]')
    print('━━━━━━━━━━━━━━━━━━━━━━')
    
    val = ''
    while val != (1 or 2 or 3):
        val = input('Választásod: ')
        match val:
            case '1':
                Slowtype(f'Felséges királyom, életem-halálom kezedbe ajánlom! Vállalkoznék a sárkány legyőzésére!')
                repchange(2)
                print('A királlyal mindig tisztelettel beszélj!')
            
            case '2':
                Slowtype(f'[{foszereplo}]: Hallod-e király? Vállalkoznék a sárkány legyőzésére!')
                Slowtype(f'[ŐR]: A király nem ilyen hangnemet érdemel!')
                print(f'Megütött az őr, ezzel 2-t sebezve.')
                takeDamage(2)
                
                repchange(-10)
                print('A királlyal mindig tisztelettel beszélj!')
            
            case '3':
                Slowtype(f'[{foszereplo}]: Vállalkoznék a sárkány legyőzésére!')
                Slowtype(f'[ŐR]: Kihez beszélsz?')
                Slowtype(f'[{foszereplo}]: Őfelségéhez.')
                Slowtype(f'[{foszereplo}]: Akkor köszöntsd a királyt!')

                print('\nHogy köszöntöd a királyt?')
                print('━━━━━━━━━━━━━━━━━━━━━━')
                print('1...Felséges királyom, életem-halálom kezedbe ajánlom!')
                print('2...Hallod-e, király?')
                print('━━━━━━━━━━━━━━━━━━━━━━')

                val = ''
                while val != (1 or 2):
                    val = input('Választásod: ')

                    match val:
                        case '1':
                            Slowtype(f'Felséges királyom, életem-halálom kezedbe ajánlom! Vállalkoznék a sárkány legyőzésére!')
                            repchange(2)
                            print('A királlyal mindig tisztelettel beszélj!')
                        
                        case '2':
                            Slowtype(f'[{foszereplo}]: Hallod-e király? Vállalkoznék a sárkány legyőzésére!')
                            Slowtype(f'[ŐR]: A király nem ilyen hangnemet érdemel!')
                            print(f'Megütött az őr, ezzel 2-t sebezve.')
                            takeDamage(2)
                            
                            repchange(-10)
                            print('A királlyal mindig tisztelettel beszélj!')

                        case _:
                            print('Érvénytelen választ adtál meg!')

            case _:
                print('Érvénytelen választ adtál meg!')
bev()




