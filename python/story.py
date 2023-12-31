from city import *
del money
from variables import money

foszereplo = 'Játékos'

def collectingFirst():
    global currentquest, money
    Slowtype('[Szolga]: A király fia megbetegedett! Mai feladatod, hogy gyógynövényeket szedj neki a mezőn!')
    time.sleep(1)
    Slowtype('(Gondolat): Remélem ezért jutalomban fogok részesülni!')
    time.sleep(2)
    nowplace = 'field'
    print('Megérkeztél a mezőre.')
    input('Keresgélés az ENTER megnyomásával >>')
    
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
            Slowtype(f'[{foszereplo}]: Megtaláltam a {find} növényt. Megvan amiért jöttem!')
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

    while foszereplo == ('Játékos' or '' or ' ' or '   ' or '    ' or '     ' or '      '):
        foszereplo = Slowtype(input(f'[{foszereplo}]: Királyom, az én becses nevem nem más, mint '))
        if foszereplo == ('Játékos' or '' or ' ' or '   ' or '    ' or '     ' or '      '):
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
    castle()


if __name__ == '__main__':
    bev()




