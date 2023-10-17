import time
import os
foszereplo = input('Mi a neved? ')
def alom():
    print('Végre itt a nap')
    time.sleep(2)
    print('Eljött az én időm')
    time.sleep(2)
    print('Megvan a felszerelésem is')
    time.sleep(1.5)
    print('ZzZzZzZzZzZz')
    time.sleep(1.5)
    print('Megtöröm a gonosz sárkány uralmát')
    time.sleep(2)
    print('Eljött a harc ideje.')
    time.sleep(1.5)
    print('ZzZzZzZzZzZz')
    time.sleep(1)
    input('\nENTERrel tovább')
    os.system('cls')

def bev():
    time.sleep(1)
    print('Csövesszálló vezetője: Jó reggelt 7 alvók, ideje felkelni.')
    time.sleep(2)
    print('Csövesszálló vezetője: Emlékeztető: aki nem dolgozik elég keményen mehet az utcára aludni.')
    time.sleep(1.5)
    print('Csövesszálló vezetője: Most meg mindenki munkára')
    input('\nENTERrel tovább')
    os.system('cls')


    
def elk():
    print(f'{foszereplo}: Megint unalmas nap ahol a többiek által széna közé dobált tűket kell keresgélnem')
    time.sleep(1)
    print('Csövesszálló vezetője: A lakhelyed tulaja nem talál túl hasznosnak, ki vagy rúgva a szállásból')
    time.sleep(1)
    input('\nENTERrel tovább')
    os.system('cls')

def kikialtas():
    print('*dobszó* *dobszó*')
    time.sleep(1.5)
    print('Dobos: Nagy veszély fenyegeti a várost, a sárkány el akarja pusztítani.')
    print('Dobos: Aki megmenti a várost megitésése a legnagyobb lesz, pénzzel soha nem lesz dolga.')
    time.sleep(3)
    print(f'{foszereplo}: Én fogom legyözni a sárkányt. ')
    print(f'{foszereplo}: A sárkányt 5 kristály köti az élethez, minden tájon egy.')
    print(f'{foszereplo}: Egy a mezőn, egy az erdőben, egy a bányában, egy kazamatában, egy a sárkány vermében. ')
    time.sleep(2)
    





alom()
bev()
elk()



