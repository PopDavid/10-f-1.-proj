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
    os.system('cls')

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

    print('Sikeresen megérkeztél ide: vár')



bev()




