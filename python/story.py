import time
import os
from definialas import Slowtype

foszereplo = input('Mi a neved? ')
# def alom():
#     Slowtype('[JÁTÉKOS]: Végre elérkezett a nap!')
#     time.sleep(2)
#     Slowtype('[JÁTÉKOS]: Eljött az én időm!')
#     time.sleep(2)
#     Slowtype('[???]: Jó reggelt!')
#     time.sleep(1.5)
#     Slowtype('ZzZzZzZzZzZz')
#     time.sleep(1.5)
#     Slowtype('[JÁTÉKOS]: Megtöröm a gonosz sárkány uralmát!')
#     time.sleep(2)
#     Slowtype('[???]: Ébresztő!')
#     time.sleep(1.5)
#     Slowtype('ZzZzZzZzZzZz')
#     time.sleep(1)
#     input('\nENTERrel tovább')
#     os.system('cls')

def bev():
    Slowtype('[JÁTÉKOS]: Végre elérkezett a nap!')

    time.sleep(2)
    Slowtype('[JÁTÉKOS]: Eljött az én időm!')
    time.sleep(2)
    Slowtype('[???]: Jó reggelt!')
    time.sleep(1.5)
    Slowtype('ZzZzZzZzZzZz')
    time.sleep(1.5)
    Slowtype('[JÁTÉKOS]: Megtöröm a gonosz sárkány uralmát!')
    time.sleep(2)
    Slowtype('[???]: Ébresztő!')
    time.sleep(1.5)
    Slowtype('ZzZzZzZzZzZz')
    time.sleep(1)
    input('\nFelébredés az ENTER megnyomásával >>')

    time.sleep(1)
    Slowtype('[]: Jó reggelt 7 alvók, ideje felkelni.')
    time.sleep(2)
    Slowtype('Csövesszálló vezetője: Emlékeztető: aki nem dolgozik elég keményen mehet az utcára aludni.')
    time.sleep(1.5)
    Slowtype('Csövesszálló vezetője: Most meg mindenki munkára')
    input('\nENTERrel tovább')
    os.system('cls')


    
def elk():
    Slowtype(f'{foszereplo}: Megint unalmas nap ahol a többiek által széna közé dobált tűket kell keresgélnem')
    time.sleep(1)
    Slowtype('Csövesszálló vezetője: A lakhelyed tulaja nem talál túl hasznosnak, ki vagy rúgva a szállásból')
    time.sleep(1)
    input('\nENTERrel tovább')
    os.system('cls')

def kikialtas():
    Slowtype('*dobszó* *dobszó*')
    time.sleep(1.5)
    Slowtype('Dobos: Nagy veszély fenyegeti a várost, a sárkány el akarja pusztítani.')
    Slowtype('Dobos: Aki megmenti a várost megitésése a legnagyobb lesz, pénzzel soha nem lesz dolga.')
    time.sleep(3)
    Slowtype(f'{foszereplo}: Én fogom legyözni a sárkányt. ')
    Slowtype(f'{foszereplo}: A sárkányt 5 kristály köti az élethez, minden tájon egy.')
    Slowtype(f'{foszereplo}: Egy a mezőn, egy az erdőben, egy a bányában, egy kazamatában, egy a sárkány vermében. ')
    time.sleep(2)
    





# alom()
bev()
elk()
kikialtas()



