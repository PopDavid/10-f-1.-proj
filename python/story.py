from city import *
del money
from variables import money

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
            input('ENTER')
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
    global nowplace, foszereplo
    foszereplo = input('Mi a neved: ')
    print('━━━━━━━━━━━━━━━━━━━━━━')
    print('Medieval City Game')
    print('━━━━━━━━━━━━━━━━━━━━━━')
    Slowtype('\nEz a játék a középkorba repíti vissza a játékost,\nki a főszereplő útját bejárva próbál harcossá, \nvalamint a város hősévé válni.')
    input('\nTovábbhaladás az ENTER megnyomásával >>')
    torles(money)
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
    
    torles(money)

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
    while val != str(1 or 2 or 3):
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
                Slowtype(f'[ŐR]: Akkor köszöntsd a királyt!')

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
    Slowtype('[Király]: Áldásomat adom küldetésedre, próbáld meg.')
    input('Kimenés a várba ENTER megnyomásával.')
    torles(money)


if __name__ == '__main__':
    bev()




